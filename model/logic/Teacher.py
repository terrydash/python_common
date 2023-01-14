from model.base.MongoDBEntity import MongoDBEntity


class Teacher(MongoDBEntity):
    zgh = ''  # 职工号
    name = ''  # 姓名
    xb = ''  # 性别
    bm = ''  # 部门
    mm = ''  # 密码
    token = ''
