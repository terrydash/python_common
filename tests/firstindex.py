# -*- coding: utf-8 -*-
# @Time    : 2018/8/11 下午8:27
# @Author  : Aries
# @Site    :
# @File    : admin.py
# @Software: PyCharm

import unittest

from common.convert import class2json
from logic.course_evaluate.FirstIndex import FirstIndexLogic
from model.logic.Admin import Admin


class mytest(unittest.TestCase):
    # setUp()初始化,
    def setUp(self):
        pass

    # 销毁
    def tearDown(self):
        pass

    def test_firstindex(self):
        fil=FirstIndexLogic()
        datas,num,msg=fil.get_all_fromdb()
        for fi in datas:
            fi['secondIndexType']=3
            fil.baseRepository.update_by_id(fi["_id"],fi)
        print(class2json(datas))

