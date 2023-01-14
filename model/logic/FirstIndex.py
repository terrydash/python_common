# *_*coding:utf-8 *_*
# 一级指标
from faker import Faker
from model.base.MongoDBEntity import MongoDBEntity
from bson import ObjectId, dbref


class FirstIndex(MongoDBEntity):
    # 指标名称
    name = ''
    # 指标说明
    description = ''
    # 包含二级指标数
    secondIndexNum = 0
    # 备注
    remarks = ''
    # 所属课程类别
    courseEvaluate = {}
    # 二级指标是否为单选
    secondIndexIsSingle = False
    # 该一级指标的核算比例
    proportion = 0
    secondIndexType=1
    @staticmethod
    def FakeOne():
        __f = Faker(locale='zh_CN')
        fi = FirstIndex()
        fi.name = __f.name()
        fi.secondIndexNum = __f.random_int(max=100, min=5)
        fi.description = __f.text()
        fi.remarks = __f.sentence()

        cl = fi.__COLLECTION_NAME__()

        ce = dbref.DBRef(collection=cl, id=ObjectId())
        fi.courseEvaluate = ce

        return fi
