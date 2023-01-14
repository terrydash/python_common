# -*-coding:utf-8-*-
from model.base.MongoDBEntity import MongoDBEntity


class Department(MongoDBEntity):
    code = ''  # 代码
    name = ''  # 部门名称
    othername = ''  # 别名
    is_teach_dept = False  # 是否为教学单位
