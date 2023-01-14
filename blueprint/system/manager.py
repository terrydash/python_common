from flask import Blueprint

from logic.common.Password import prpcrypt
from logic.user.manager import ManagerLogic
from model.common.jsonModel import response_normal, response_error

mainbp = Blueprint('manager', __name__)


@mainbp.route('/get/<id>', methods=["GET"])
def GetSuperVision(id):
    if len(id) == 0 or id is None:
        return response_error(msg='id不能为空！').to_json()
    tl = ManagerLogic()
    result, num, msg = tl.get_by_id(id)
    s: dict = dict(result)
    s["mm"] = prpcrypt.password_decrypt(s.get("mm"))
    print(s)
    r = response_normal(data=s, count=num, msg=msg)

    return r.to_json()


@mainbp.route('/get', methods=["GET"])
def GetAllSuperVision():
    sl = ManagerLogic()
    results, num, msg = sl.get_all_fromdb()
    if results is not None:
        for x in results:
            if 'mm' in x:
                x.pop('mm')
    return response_normal(data=results, count=num, msg=msg).to_json()
