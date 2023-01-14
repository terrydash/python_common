# *_*coding:utf-8 *_*
# *_*coding:utf-8 *_*
# 一级指标

from model.base.MongoDBEntity import MongoDBEntity
from enum import Enum, unique


@unique
class SchemeType(Enum):
    ABCDE = 1  # ABCDE形式
    Single = 2  # 单选
    FiveLevel = 3  # 五级分制 优秀 中等 良好 及格 不及格
    FourLevel = 4  # 四级分制 优秀 良好 合格
    FiveStar = 5  # 五级分制 优秀 中等 良好 及格 不及格
    Text = 6  # 文字形式

class SecondIndex(MongoDBEntity):
    # 指标名称
    name = ''
    # 指标说明
    description = ''
    order = 0
    # 教师是否可看
    is_teacher_can_see = False
    # 教师是否可回复
    is_teacher_can_reply = False
    # 部门管理者是否可看
    is_department_can_see = False
    # 部门管理者是否可回复
    is_department_can_reply = False
    # 该指标的等价分数
    value = 0
    # 该指标的选择结果 比如五星 选择的星数 4级分制的优秀 良好等
    result = ''
    scheme_type = SchemeType.FiveStar
    # 备注
    remarks = ''
    # 作为文字形式的前端高度
    height = 500
    # 作为文字形式的前端宽度
    width = 500
    # 所属课程评价方案
    courseEvaluate = {}
    courseEvaluateID=''
    # 所属一级指标
    firstIndex = {}
    firstIndexID=''



