# *_*coding:utf-8 *_*
from faker import Faker
from model.base.MongoDBEntity import MongoDBEntity


# 评价分类,用于制定该门课程使用哪些分类的
class CourseEvaluate(MongoDBEntity):
    # 标准名称
    name = ''
    # 说明
    description = ''
    # 包含一级指标
    firstIndex = []
    # 包含一级指标数
    firstIndexNum = 0

    # 包含二级指标
    secondIndex = []
    # 包含二级指标数
    secondIndexNum = 0
    # 关联的课程
    course = []
    # 关联的课程数量
    courseNum = 0
    # 备注
    remarks = ''

    # 所属课程类别

    @staticmethod
    def FakeOne():
        __f = Faker(locale='zh_CN')
        ce = CourseEvaluate()
        ce.name = __f.name()
        ce.secondIndexNum = __f.random_int(max=100, min=5)
        ce.firstIndexNum = __f.random_int(max=100, min=5)
        ce.description = __f.sentence()
        ce.remarks = __f.sentence()
        ce.courseNum = __f.random_int(max=500, min=50)
        return ce
