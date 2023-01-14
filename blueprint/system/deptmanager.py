from flask import Blueprint

from logic.user.deptmanager import DeptMangerLogic
from model.common.jsonModel import response_normal, response_error

mainbp = Blueprint('deptmanager', __name__)


@mainbp.route('/get/<id>', methods=["GET"])
def Getdeptmanager(id):
    if len(id) == 0 or id is None:
        return response_error(msg='id不能为空！').to_json()
    dl = DeptMangerLogic()
    result, num, msg = dl.get_by_id(id)
    r=dict(result)
    from logic.common.Password import prpcrypt
    r['mm']=prpcrypt.password_decrypt(r.get('mm'))
    r = response_normal(data=r, count=num, msg=msg)
    return r.to_json()


@mainbp.route('/get', methods=["GET"])
def GetAlldeptmanager():
    dl = DeptMangerLogic()
    results, num, msg = dl.get_all_fromdb()
    for x in results:
        if 'mm' in x:
            x.pop('mm')
    return response_normal(data=results, count=num, msg=msg).to_json()
