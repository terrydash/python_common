# -*- coding: utf-8 -*-
# @Time    : 2018/8/11 下午8:27
# @Author  : Aries
# @Site    : 
# @File    : admin.py
# @Software: PyCharm

import unittest

from common.convert import class2json
from logic.user.admin import AdminLogic
from model.logic.Admin import Admin


class mytest(unittest.TestCase):
    # setUp()初始化,
    def setUp(self):
        pass

    # 销毁
    def tearDown(self):
        pass

    def test_insert_supervision(self):
        al = AdminLogic()
        admin = Admin()
        admin.username = 'admin'
        admin.mm = 'admin'
        admin.bm = '质保处'
        admin.truename = 'Admin'
        admin.powers = []
        result, num, msg = al.insert_one(admin)
        #print(class2json(result), num, msg)
        self.assertTrue(result is not None)

    # def test_get_supervision(self):
    #     sl = AdminLogic()
    #     from logic.common.Password import prpcrypt
    #     result, num, msg = sl.get_all_fromdb()
    #     for  r in result:
    #         print(r["username"])
    #         print(prpcrypt.password_decrypt(r["mm"]))
    #     self.assertTrue(result is not None)
