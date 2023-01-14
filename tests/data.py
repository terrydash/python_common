# -*- coding: utf-8 -*-
# @Time    : 2018/8/11 下午8:27
# @Author  : Aries
# @Site    :
# @File    : admin.py
# @Software: PyCharm

import unittest


class mytest(unittest.TestCase):
    # setUp()初始化,
    def setUp(self):
        pass

    # 销毁
    def tearDown(self):
        pass

    def test_makeActivateCode(self):
        from logic.common.Password import prpcrypt
        code = prpcrypt.password_encrypt("zuozhexuguoxu-2019-12-09")
        print(code)

    def test_exportdata(self):
        from logic.data.Export import DataExportLogic
        from logic.score.Score import ScoreLogic
        from io import BytesIO
        el = DataExportLogic()
        actyear = "2018-2019-2"
        sl = ScoreLogic()
        query = {"actyear": actyear}
        result, num, msg = sl.baseRepository.search_no_page(query=query)
        print('num=' + str(len(result)))
        bm = []
        for score in result:
            bm_name = str(score["kkxy"])
            if bm_name not in bm:
                print(bm_name)
                bm.append(bm_name)
                workbook = el.export_all_bm_score(teacher_name='', dept=bm_name, actyear=actyear, schemeid='')
                bio = BytesIO()
                workbook.save(bio)
                workbook.save(bm_name + '.xls')
