# 部分负责人

from logic.common.Password import prpcrypt
from model.base.MongoDBEntity import MongoDBEntity


class DeptManager(MongoDBEntity):
    zgh = ''  # 职工号
    name = ''  # 姓名
    xb = ''  # 性别
    bm = ''  # 部门
    mm = ''  # 密码

    def __init__(self, zgh, name, xb, bm, mm):
        self._COLLECTION_NAME = self.__class__.__name__.lower()
        self.zgh = zgh  # 职工号
        self.name = name  # 姓名
        self.xb = xb  # 性别
        self.bm = bm  # 部门
        self.mm = prpcrypt.password_encrypt(mm)  # 密码
        self.token = ''
