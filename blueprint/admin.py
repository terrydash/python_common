from flask import Blueprint, request
from logic.user.admin import AdminLogic
from model.common.jsonModel import response_normal, response_error

adminbp = Blueprint('admin', __name__)


@adminbp.route('/info')
def getinfo():
    token = request.headers['Auth']
    # print(token)
    admininfo = {
        'roles': ['admin', 'teacher'],
        'name': '徐国旭',
        'avatar': 'http://125.222.144.16:8089/upload/6f5dbcec-ad0e-4acf-b689-bf6e479e70bc.png',
        'level': '系统管理员'
    }
    r = response_normal(data=admininfo)
    return r.to_json()


@adminbp.route('/getpage', methods=["GET"])
def GetAllSuperVisionByPage():
    page = 1
    if 'page' in request.values:
        page = int(request.values.get('page'))
    from logic.user.admin import AdminLogic
    sl = AdminLogic()
    results, num, msg = sl.get_all_page(page, 10, '+_id')
    for x in results:
        if 'mm' in x:
            x.pop('mm')
    return response_normal(data=results, count=num, msg=msg).to_json()


@adminbp.route('/get/<id>', methods=["GET"])
def GetSuperVision(id):
    if len(id) == 0 or id is None:
        return response_error(msg='id不能为空！').to_json()

    tl = AdminLogic()
    result, num, msg = tl.get_by_id(id)
    s: dict = dict(result)
    from logic.common.Password import prpcrypt
    s["mm"] = prpcrypt.password_decrypt(s.get("mm"))
    r = response_normal(data=s, count=num, msg=msg)
    return r.to_json()

@adminbp.route('/add', methods=["Post"])
def AddSuperVision():
    requestjson = request.json
    model: dict = dict(requestjson.get("model"))
    sl = AdminLogic()
    result, msg = sl.check_model(model)
    if result:
        response_error(msg == msg)
    result, num, msg = sl.add_admin(model)
    print(result, msg)
    if not result:
        return response_error(msg=msg).to_json()
    return response_normal(data=True, count=0, msg=msg).to_json()

@adminbp.route('/update', methods=["Post"])
def UpdateAdmin():
    requestjson = request.json
    model: dict = dict(requestjson.get("model"))
    sl = AdminLogic()
    result, msg = sl.check_model(model)
    if result:
        response_error(msg == msg)
    result, num, msg = sl.update_admin(model)
    print(result, msg)
    if not result:
        return response_error(msg=msg).to_json()
    return response_normal(data=True, count=0, msg=msg).to_json()