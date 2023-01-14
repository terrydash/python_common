from enum import Enum

from bson.json_util import dumps

from common.convert import class2json


# @todo 写枚举类型转json的转换方式
class ResponseCode(Enum):
    OK = 10000  # // 返回正常
    Not_login = 20000  # // 没有登录
    Power_limit = 30000  # // 没有权限
    Error = 40000  # // 服务器问题
    Validation_error = 40001  # // 提交的内容出现验证问题
    Data_Collision = 40002  # // 提交的数据与数据库冲突等问题


class JsonModel:
    def __init__(self, data=None, count=0, msg='', code=ResponseCode.OK):
        self.data = data
        self.count = count
        self.msg = msg
        self.code = code

    def to_json(self):
        r = class2json(self)
        return dumps(r, ensure_ascii=False)


def response_normal(data=None, count=0, msg='正常', code=ResponseCode.OK):
    j = JsonModel(data, count, msg, code)
    return j


def response_error(data=None, count=0, msg='发生错误,请联系管理员！', code=ResponseCode.Error):
    j = JsonModel(data, count, msg, code)
    return j


def response_notlogin(data=None, count=0, msg='登录信息失效，请重新登录！', code=ResponseCode.Not_login):
    j = JsonModel(data, count, msg, code)
    return j
