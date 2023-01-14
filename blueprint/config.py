from flask import Blueprint, request

from common.convert import class2json
from config.systemconfig import get_allconfig
from init.init_logging import get_logger
from logic.common.Config import ConfigLogic
from model.common.jsonModel import response_normal, response_error

mainbp = Blueprint('config', __name__)

logger = get_logger(__name__)


@mainbp.route('/getall')
def getMongo():
    configs = get_allconfig().values()
    from logic.common.Login import GetUserInfoFromToken
    result, userinfo = GetUserInfoFromToken()
    # logger.debug(str(userinfo), '访问了/modifypwd')
    cons = []
    for c in configs:
        cons.append(c)
    return response_normal(data=cons, count=len(configs), msg='正常').to_json()


@mainbp.route('/getxnxq')
def getXNXQ():
    cl = ConfigLogic()
    xn = cl.getCurrentXN()
    xq = cl.getCurrentXQ()
    actyear = cl.getCurrentActYear()
    data = {'xn': xn, 'xq': xq, 'actyear': actyear}
    return response_normal(data=data, count=3, msg='正常').to_json()


@mainbp.route('/getbyid/<id>', methods=["GET"])
def GetDepartment(id):
    if len(id) == 0 or id is None:
        return response_error(msg='id不能为空！').to_json()
    print(id)
    dl = ConfigLogic()
    result, num, msg = dl.get_by_id(id)
    print(result)
    from config.systemconfig import sys_config_list
    for config in sys_config_list:
        if config["dbname"] == result["name"]:
            result["content"] = config["name"]
    r = response_normal(data=result, count=num, msg=msg)
    return r.to_json()


@mainbp.route('/update', methods=["POST"])
def UpdateConfig():
    requestjson = request.json
    if 'model' in requestjson:
        model = dict(requestjson.get('model'))
        dept = {}
        id = model.get('_id')
        if id is None or len(id) == 0:
            return response_error(msg='参数不正确!').to_json()
        cl = ConfigLogic()
        if 'value' in model.keys() and len(model.get('value')) > 0:
            dept = {'value': model.get('value')}
        else:
            return response_error(msg='别名不能为空！').to_json()
        result = cl.update(id, dept)
        if result:
            from config.systemconfig import init
            init()
            return response_normal(data=result, count=0, msg="正常").to_json()

        else:
            return response_error(data=result, count=0, msg="更新错误，请联系管理员！").to_json()

    return response_error(msg='参数不正确!').to_json()


@mainbp.route('/get/<configname>')
def getconfig(configname):
    from config.systemconfig import get_config
    result = get_config(configname)
    data = dict()
    data[str(configname)] = result
    return response_normal(data=data, count=3, msg='正常').to_json()


@mainbp.route('/getmywords')
def getmyywords():
    from config.systemconfig import get_config
    result = get_config('commitlog')
    print(result)
    return response_normal(data=result, count=3, msg='正常').to_json()


@mainbp.route('/getactyears')
def getactyearts():
    from config.systemconfig import sys_config
    r = sys_config.get("actyears")
    result: list = r["value"]
    return response_normal(data=result, count=len(result), msg='正常').to_json()


@mainbp.route('/refresh')
def refreshconfigs():
    from config.systemconfig import init
    init()
    return response_normal(data=1, count=1, msg='正常').to_json()


@mainbp.route('/activatecode', methods=["POST"])
def modifyactivatecode():
    requestjson = request.json
    _activateCode = ''
    if 'model' in requestjson:
        model = dict(requestjson.get('model'))
        if 'value' in model.keys() and len(model.get('value')) > 0:
            _activateCode = model.get('value')
        else:
            return response_error(msg='不能为空！').to_json()
        from logic.common.Config import ConfigLogic
        cl = ConfigLogic()
        result, message = cl.checkActivateCode(_activateCode)
        if result:
            cl.updateActiveCode(_activateCode)
            return response_normal(data=message[0:11]).to_json()
        else:
            return response_error(msg=message).to_json()
    return response_error(msg="参数错误!").to_json()
