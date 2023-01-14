# -*- coding: utf-8 -*-
# @Time    : 2018/8/11 下午8:27
# @Author  : Aries
# @Site    :
# @File    : admin.py
# @Software: PyCharm

import unittest

from common.convert import class2json
from logic.jwxt.Teacher import TeacherLogic
from model.logic.Admin import Admin


class teacher(unittest.TestCase):
    # setUp()初始化,
    def setUp(self):
        pass

    # 销毁
    def tearDown(self):
        pass

    def test_gettaecherfromorace(self):
        tl=TeacherLogic()
        tl.oracle2mongo()

