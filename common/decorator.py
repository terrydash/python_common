# -*- coding: utf-8 -*-
# @Time    : 2018/8/13 下午5:12
# @Author  : Aries
# @Site    : 
# @File    : decorator.py
# @Software: PyCharm
from functools import wraps

from flask import request

from model.common.jsonModel import response_error, ResponseCode




def admin_power(power_name: str):
    pass
'''
用来检查用户是否为指定角色
'''

def need_power(roles: list):
    if roles is None or len(roles) <= 0:
        raise Exception('权限检查参数不能为空！')

    def _decorated_function(f):
        @wraps(f)
        def __decorated_function(*args, **kws):
            # 需要在登录状态调用, 检查是否为有admin权限的用户登录，
            # 如果不是，返回错误码；
            if 'Auth' in request.headers.keys():
                auth_token = request.headers['Auth']
                from db.RedisConn import redisConn
                if len(auth_token) > 0 and redisConn.exists(auth_token):
                    from model.common.Common import RoleType
                    if RoleType.ALL.value in roles:
                        return f(*args, **kws)
                    from common.convert import redisstr2list
                    tokenlist = redisstr2list(redisConn.get(auth_token))
                    token = {}
                    if isinstance(tokenlist, list) and len(tokenlist) > 0:
                        token: dict = tokenlist[0]
                    elif isinstance(tokenlist, dict):
                        token: dict = tokenlist
                    if 'roleid' in token:
                        roleid = int(token.get('roleid'))
                        # print(roles)
                        if roleid in roles:
                            return f(*args, **kws)
                        else:
                            return response_error(msg='您的角色不具备权限！', code=ResponseCode.Power_limit).to_json()

            return response_error(msg='登录信息失效，请重新登录！', code=ResponseCode.Not_login).to_json()

        return __decorated_function

    return _decorated_function
