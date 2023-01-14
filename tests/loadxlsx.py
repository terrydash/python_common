import unittest

import os
import xlrd

from enviroment import project_dir


class mytest(unittest.TestCase):
    # setUp()初始化,
    def setUp(self):
        pass

    # 销毁
    def tearDown(self):
        pass

    def test_get_course_info_and_scheme(self):
        filename = project_dir + os.sep + "ty-makexin.xlsx"
        data = xlrd.open_workbook(filename)
        table = data.sheets()[0]
        nrows = table.nrows
        print(nrows)

        from logic.jwxt.TeachTask import TeachTaskLogic
        ttl = TeachTaskLogic()
        result, num, msg = ttl.get_all_fromdb()
        tc: dict = result[0]
        tc.pop('_id')
        tcs = list()
        for x in range(2, nrows):
            row = table.row_values(x)
            print(table.row_values(x))
            tc['kcdm'] = str(float(str(row[0]).strip()))
            tc['kkxy'] = str(row[8]).strip()
            tc['jszgh'] = str(float(str(row[2]).strip()))
            tc['jsxm'] = str(row[3]).strip()
            tc['qsz'] = 4
            tc['jsz'] = 16
            tc['kcxz'] = str(row[9]).strip()
            tc['cdbs'] = str(row[6]).strip()
            tc['bjmc'] = str(row[5]).strip()
            tc['bjrs'] = '0'
            tc['xkkh'] = '(2018-2019-2)-' + str(tc['kcdm'])  + '-' + str(tc['jszgh'])  + '-1'
            tc['kcmc'] = str(row[1]).strip()
            tc['isimport']=1
            print(tc)
            ttl.baseRepository.insert_one(tc)


if __name__ == '__main__':
    unittest.main(2)
