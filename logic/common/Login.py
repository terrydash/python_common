import base64
import uuid
from io import BytesIO

import rsa

from common.convert import class2json, redisstr2list
from common.vcode import create_validate_code
from config.startupconfig import init_config
from db.RedisConn import redisConn
from model.common.Common import TokenModel, RoleType


def GetUserInfoFromToken():
    from flask import request
    if 'Auth' in request.headers.keys():
        auth_token = request.headers['Auth']
        from db.RedisConn import redisConn
        if len(auth_token) > 0 and redisConn.exists(auth_token):
            from model.common.Common import RoleType
            from common.convert import redisstr2list
            tokenlist = redisstr2list(redisConn.get(auth_token))
            token = {}
            if isinstance(tokenlist, list) and len(tokenlist) > 0:
                token: dict = tokenlist[0]
            elif isinstance(tokenlist, dict):
                token: dict = tokenlist
            if 'powers' in token.keys():
                token.pop('powers')
            return True, token
    return False, None


def CheckUUID(uuid):
    if redisConn.exists(uuid):
        return True
    else:
        return False


def GetUUID():
    guid = str(uuid.uuid4()).replace('-', '')
    redisConn.set(guid, '')
    redisConn.expire(guid, 36000)
    return guid


def GetVcode(uuid):
    if uuid is None or not redisConn.exists(str(uuid)):
        text = 'wrong'
    else:
        text = None
    code, img = create_validate_code(text=text)
    #print(code)
    if text is None:
        redisConn.set(uuid, code)
        redisConn.expire(uuid, 1000 * 60 * 30)
    buf = BytesIO()
    img.save(buf, 'JPEG', quality=70)
    return buf, code


def TeachLogin(username, password):
    from logic.jwxt.Teacher import TeacherLogic
    tl = TeacherLogic()
    result, num, msg = tl.get_by_zgh_and_passwd(username, password)
    if result is not None and len(result) > 0:
        teacher = result[0]
        tokenmodel = TokenModel(teacher.get('_id'), [], 'teacher', teacher.get('name'), teacher.get('bm'), 1)
        token = make_token(tokenmodel)
        return True, tokenmodel, token, '正常'
    return False, None, None, '用户名或者密码错误!';


def SuperVisionLogin(username, password):
    from logic.user.supervision import SupervisionLogic
    sl = SupervisionLogic()
    result, num, msg = sl.get_by_zgh_and_passwd(username, password)
    if result is not None and len(result) > 0:
        supervision: dict = result[0]
        tokenmodel = TokenModel(supervision.get('_id'), [], 'supervision', supervision.get('name'),
                                supervision.get('bm'), 2)
        token = make_token(tokenmodel)
        return True, tokenmodel, token, '正常'
    return False, None, None, '用户名或者密码错误!';


def DeptManagerLogin(username, password):
    from logic.user.deptmanager import DeptMangerLogic
    dl = DeptMangerLogic()
    result, num, msg = dl.get_by_zgh_and_passwd(username, password)
    if result is not None and len(result) > 0:
        supervision: dict = result[0]
        tokenmodel = TokenModel(supervision.get('_id'), [], 'deptmanager', supervision.get('name'),
                                supervision.get('bm'), 3)
        token = make_token(tokenmodel)
        return True, tokenmodel, token, '正常'
    return False, None, None, '用户名或者密码错误!'


def AdminLogin(username, password):
    from logic.user.admin import AdminLogic
    al = AdminLogic()
    result, num, msg = al.get_by_username_and_passwd(username, password)
    if result is not None and len(result) > 0:
        supervision: dict = result[0]
        tokenmodel = TokenModel(supervision.get('_id'), [], 'admin', supervision.get('truename'), supervision.get('bm'),
                                4)
        token = make_token(tokenmodel)
        return True, tokenmodel, token, '正常'
    return False, None, None, '用户名或者密码错误!'
def ManagerLogin(username, password):
    from logic.user.manager import ManagerLogic
    sl = ManagerLogic()
    result, num, msg = sl.get_by_zgh_and_passwd(username, password)
    if result is not None and len(result) > 0:
        supervision: dict = result[0]
        tokenmodel = TokenModel(supervision.get('_id'), [], 'manager', supervision.get('name'),
                                supervision.get('bm'), 5)
        token = make_token(tokenmodel)
        return True, tokenmodel, token, '正常'
    return False, None, None, '用户名或者密码错误!';


def CheckToken(token: str):
    if not redisConn.exists(token):
        return False, None, 'token不存在！'
    tokenmodelstr = redisConn.get(token)
    tokenmodellist = redisstr2list(tokenmodelstr)
    return True, tokenmodellist, '正常'


def CheckLogin(username, password, uuid, vcode, login_type):
    token = ''
    if uuid is not None and len(uuid) > 0 and vcode is not None and len(vcode) > 0:
        if str(redisConn.get(uuid)).upper() != str(vcode).upper():
            return False, None, None, '验证码不正确'
    else:
        return False, None, None, '参数错误！'

    if int(login_type) == RoleType.Teacher.value:
        return TeachLogin(username, password)
    elif int(login_type) == RoleType.SuperVision.value:
        return SuperVisionLogin(username, password)
    elif int(login_type) == RoleType.DeptManager.value:
        return DeptManagerLogin(username, password)
    elif int(login_type) == RoleType.Admin.value:
        return AdminLogin(username, password)
    elif int(login_type) == RoleType.Manager.value:
        return ManagerLogin(username, password)

    '''
    if str(username).lower() == 'admin' and str(password).lower() == 'admin':
        pubkey = init_config.rsa.publickey
        token = bytes.decode(
            base64.b64encode(rsa.encrypt(str(uudtool.uuid4()).encode('utf-8'), pubkey).__str__().encode('utf-8')),
            encoding='utf-8')
        data = token
        redisConn.set(token, 'powers')
        redisConn.expire(token, 1000 * 60 * 10)
        return True, data;
    '''
    return False, None, token, '用户名或者密码错误!';


def make_token(tokenmodel: TokenModel):
    pubkey = init_config.rsa.publickey
    tokenmodel = class2json(tokenmodel)
    guid = uuid.uuid1()
    token = bytes.decode(
        base64.b64encode(rsa.encrypt(str(guid).encode('utf-8'), pubkey).__str__().encode('utf-8')),
        encoding='utf-8')
    redisConn.set(token, str(tokenmodel))
    redisConn.expire(token, 1000 * 60 * 10)
    return token
