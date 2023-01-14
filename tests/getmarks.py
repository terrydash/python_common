import os
import unittest

from enviroment import project_dir


class mytest(unittest.TestCase):
    # setUp()初始化,
    def setUp(self):
        pass

    # 销毁
    def tearDown(self):
        pass

    def testgetmarks(self):
        from openpyxl import load_workbook
        filename = project_dir + os.sep + "all.xlsx"
        wb = load_workbook(filename)
        print(wb.get_sheet_names())
        for sname in wb.get_sheet_names():
            sheet = wb.get_sheet_by_name(sname)
            i = 0
            from db.OracleConn import DBSession
            from model.oracle.models import t_cjbmaxview
            session = DBSession()
            for row in list(sheet.rows)[1:]:
                if row[2].value is not None:
                    s = session.query(t_cjbmaxview).filter(
                        r"xh ='" + str(row[
                                           2].value) + r"' and (kcmc like '毕业设计' or kcmc like '毕业论文%' or kcmc like '毕业设计（Z）')").first()
                    if s is not None:
                        print(sname, row[2].value, row[3].value, s[8], s[5], sep=',')
                    else:
                        print(sname, row[2].value, row[3].value, '无', '无', sep=',')

                    i += 1
            print(i)


if __name__ == '__main__':
    unittest.main(2)
