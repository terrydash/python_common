import unittest

from logic.user.supervision import SupervisionLogic
from model.logic.Supervision import Supervision
from enviroment import project_dir
import os
import xlrd
class mytest(unittest.TestCase):
    # setUp()初始化,
    def setUp(self):
        pass

    # 销毁
    def tearDown(self):
        pass

    def test_insert_supervisions(self):
        from common.convert import class2json
        filename = project_dir + os.sep + "dd.xlsx"
        data = xlrd.open_workbook(filename)
        table = data.sheets()[0]
        nrows = table.nrows
        sl = SupervisionLogic()
        for x in range(0, nrows):
            row = table.row_values(x)
            if row[0] is not None and row[1] is not None:
                ddname=str(row[0]).strip()
                ddusername=str(row[1]).strip()
                query = {"name": ddname}
                result, n, m = sl.search_no_page(query=query)
                if n<1:
                    sp = Supervision(zgh=ddusername, name=ddname, xb='未填写', bm='督导委', mm='a123456')
                    sl.insert_one(sp)
                    print(class2json(sp))
        '''
        sp = Supervision(zgh='ddyzd', name='于忠得', xb='未填写', bm='督导委', mm='a123456')
        result, num, msg = sl.insert_one(sp)
        result, num, msg = sl.insert_one(sp)
        print(class2json(result))
        '''
        # print(result,num,msg)
        self.assertTrue(n>0)

    def test_insert_supervision(self):
        from common.convert import class2json
        sl = SupervisionLogic()
        sp = Supervision(zgh='xldcrs', name='蔡若松', xb='男', bm='校领导', mm='a123456')
        result, num, msg = sl.insert_one(sp)
        self.assertTrue(num > 0)

    def test_get_supervision(self):
        sl = SupervisionLogic()
        result, num, msg = sl.get_passwd_by_zgh('ddmx')
        print(result[0]['mm'])
        from logic.common.Password import prpcrypt
        prpcrypt.password_decrypt(str(result[0]['mm']))
        ##print(prpcrypt.password_decrypt(result["mm"]))
        print(msg)
        print(result)

        self.assertTrue(result is not None)
