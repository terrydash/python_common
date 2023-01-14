# -*- coding: utf-8 -*-
# @Time    : 2018/8/11 下午8:20
# @Author  : Aries
# @Site    : 
# @File    : Common.py
# @Software: PyCharm
from enum import Enum


class RoleType(Enum):
    Teacher = 1  # 教师登录
    SuperVision = 2  # 督导登录
    DeptManager = 3  # 学院负责人登录
    Admin = 4  # 系统管理员登录
    Manager = 5  # 行政管理人员
    ALL = 0  # 具有所有管理员的权限


class TokenModel(object):
    def __init__(self, objectid: str, powers: list, role: str, name: str, bm: str, roleid: int):
        self.name = name
        self.bm = bm
        self.id = objectid
        self.role = role
        self.powers = powers
        self.roleid = roleid
