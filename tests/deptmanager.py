import unittest

from logic.user.deptmanager import DeptMangerLogic
from model.logic.DeptManager import DeptManager


class mytest(unittest.TestCase):
    # setUp()初始化,
    def setUp(self):
        pass

    # 销毁
    def tearDown(self):
        pass

    def test_insert_deptmanager(self):
        sl = DeptMangerLogic()
        sp = DeptManager(zgh='000015', name='数字技术学院', xb='男', bm='数字技术学院',mm='000000')
        result, num, msg = sl.insert_one(sp)
        print(result, num, msg)
        self.assertTrue(result is not None)

    def test_get_deptmanager(self):
        sl = DeptMangerLogic()
        deptms, num, msg = sl.get_all_fromdb()
        ls = []
        for d in deptms:
            result, num, msg = sl.get_by_zgh(d['zgh'])
            ls.append(result)

        self.assertTrue(result is not None)

    def test_dept_oracle2mongo(self):
        from logic.jwxt.Department import DepartmentLogic
        DepartmentLogic().oracle2mongo()

    def test_teachtask_oracle2mong(self):
        from logic.jwxt.TeachTask import TeachTaskLogic
        ttl = TeachTaskLogic()
        ttl.oracle2mongo()
