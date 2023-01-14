from flask import Blueprint, request

from logic.common.Password import prpcrypt
from logic.user.supervision import SupervisionLogic
from model.common.jsonModel import response_normal, response_error

mainbp = Blueprint('supervision', __name__)


@mainbp.route('/get/<id>', methods=["GET"])
def GetSuperVision(id):
    if len(id) == 0 or id is None:
        return response_error(msg='id不能为空！').to_json()
    tl = SupervisionLogic()
    result, num, msg = tl.get_by_id(id)
    s: dict = dict(result)
    s["mm"] = prpcrypt.password_decrypt(s.get("mm"))
    r = response_normal(data=s, count=num, msg=msg)
    return r.to_json()


@mainbp.route('/tomanager', methods=["POST"])
def ToManager():
    requestjson = request.json
    if requestjson is None:
        return response_error(str="id不能为空！").to_json()
    id = requestjson.get('id')
    if id is None:
        return response_error(str="id不能为空！").to_json()
    sl = SupervisionLogic()
    result, num, msg = sl.tomanager(id)
    if result:
        return response_normal(msg=msg).to_json()
    return response_error(msg=msg).to_json()


@mainbp.route('/get', methods=["GET"])
def GetAllSuperVision():
    sl = SupervisionLogic()
    results, num, msg = sl.get_all_fromdb()
    for x in results:
        if 'mm' in x:
            x.pop('mm')
    return response_normal(data=results, count=num, msg=msg).to_json()


@mainbp.route('/getpage', methods=["GET"])
def GetAllSuperVisionByPage():
    page = 1
    if 'page' in request.values:
        page = int(request.values.get('page'))
    sl = SupervisionLogic()
    results, num, msg = sl.get_all_page(page, 10, '+_id')
    for x in results:
        if 'mm' in x:
            x.pop('mm')
    return response_normal(data=results, count=num, msg=msg).to_json()


@mainbp.route('/add', methods=["Post"])
def AddSuperVision():
    requestjson = request.json
    model: dict = dict(requestjson.get("model"))
    sl = SupervisionLogic()
    result, msg = sl.check_model(model)
    if result:
        response_error(msg == msg)
    result, num, msg = sl.add_supervision(model)
    print(result, msg)
    if not result:
        return response_error(msg=msg).to_json()
    return response_normal(data=True, count=0, msg=msg).to_json()
