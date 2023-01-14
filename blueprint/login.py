from flask import Response, Blueprint, request

from db.RedisConn import redisConn
from init.init_logging import get_logger
from logic.common.Login import GetVcode, CheckLogin, GetUUID
from model.common.jsonModel import response_normal, response_error, response_notlogin

loginbp = Blueprint('login', __name__)
logger = get_logger(__name__)


@loginbp.route('/getvcode')
def getvcode():
    uuid = request.values.to_dict().get('uuid')
    buf, vcode = GetVcode(uuid)
    resp = Response(buf.getvalue(), mimetype="image/jpeg")
    return resp


@loginbp.route('/modifypwd', methods=["POST"])
def modifypwd():
    from logic.common.Login import GetUserInfoFromToken
    result, userinfo = GetUserInfoFromToken()
    print(userinfo)
    requestjson = request.json
    if result:
        userpwdmodel: dict = requestjson.get('user')
        if len(userpwdmodel.keys()) == 0 or userpwdmodel is None:
            return response_error(msg='参数错误！').to_json()

        if 'opwd' not in userpwdmodel.keys() or 'newpwd' not in userpwdmodel.keys() or 'replypwd' not in userpwdmodel.keys():
            return response_error(msg='参数字典错误！').to_json()

        if len(str(userpwdmodel.get('opwd'))) == 0 or len(str(userpwdmodel.get('newpwd'))) == 0 or len(
                str(userpwdmodel.get('replypwd'))) == 0:
            return response_error(msg='原密码或新密码长度需要大于0！').to_json()

        if str(userpwdmodel.get('newpwd')) != str(userpwdmodel.get('replypwd')):
            return response_error(msg='两次密码输入不同！').to_json()

        from logic.user.modifypwd import ModifyPWDLogic
        mpl = ModifyPWDLogic()
        result, num, msg = mpl.modify_pwd(tokenmodel=userinfo, userpwdmodel=userpwdmodel)
        if result is not None:
            r = response_normal(data=True, count=num, msg='修改成功！')
        else:
            r = response_error(data=None, count=0, msg=msg)
        return r.to_json()
    return response_notlogin().to_json()


@loginbp.route('/getuuid')
def getuuid():
    guid = GetUUID()
    r = response_normal(data=guid)
    return r.to_json()


@loginbp.route('/checktoken', methods=["POST"])
def checktoken():
    requestjson = request.json
    token = requestjson.get('token')
    result = False
    entity = {}
    msg = ''
    if redisConn.exists(token):
        from logic.common.Login import CheckToken
        result, entity, msg = CheckToken(token)
    r = response_normal(data={'result': result, 'entity': entity}, msg=msg)
    return r.to_json()


@loginbp.route('/getuuidcontent', methods=["POST"])
def getuuidcontent():
    requestjson = request.json
    guid = requestjson.get('uuid')
    content = ''
    if redisConn.exists(guid):
        content = redisConn.get(guid)
    r = response_normal(data=content)
    return r.to_json()


@loginbp.route('/logout', methods=["POST"])
def logout():
    if 'Auth' in request.headers.keys():
        token = str(request.headers.get('Auth'))
        # print(token)
        if len(token) > 0:
            if redisConn.exists(token):
                redisConn.delete(token)
                return response_normal(msg='退出成功!').to_json()
    return response_error(msg='参数错误！').to_json()


@loginbp.route('/checklogin', methods=["POST"])
def checklogin():
    requestjson = request.json
    username = requestjson.get('username')
    password = requestjson.get('password')
    useruuid = requestjson.get('uuid')
    vcode = requestjson.get('vcode')
    logintype = int(str(requestjson.get('logintype')).strip())

    # print(username, password, useruuid, vcode, logintype)
    # #print(uuid.get('uuid'))
    result, entity, token, msg = CheckLogin(username, password, useruuid, vcode, logintype)
    if not result:
        r = response_error(msg=msg)
    else:

        r = response_normal(data={'entity:': entity.__dict__, 'token': token})
    return r.to_json()
