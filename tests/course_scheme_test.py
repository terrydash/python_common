import unittest

from bson import json_util

from common.convert import class2json
from config.startupconfig import init_config
from config.systemconfig import init as sys_config_init
from logic.common.Cache import CacheLogic
from logic.common.Config import ConfigLogic
from logic.course_evaluate.CourseEvaluate import CourseEvaluateLogic


class mytest(unittest.TestCase):
    # setUp()初始化,
    def setUp(self):
        self.config = init_config
        CacheLogic().init()
        sys_config_init()

    # 销毁
    def tearDown(self):
        pass

    # 具体的测试用例，以test开头
    def testjwxt(self):
        result, num, msg = CourseEvaluateLogic().get_all_and_firstindex()
        #print(json_util.dumps(class2json(result), ensure_ascii=False))
        self.assertIsNotNone(result, '测试成功!')

    def testgetconfig(self):
        cl = ConfigLogic()
        xn = cl.getCurrentXN()
        #print(xn)
        xq = cl.getCurrentXQ()
        #print(xq)
        actyear = cl.getCurrentActYear()
        #print(actyear)

    def test_teachtask_oracle2mongo(self):
        from logic.jwxt.TeachTask import TeachTaskLogic
        ttl = TeachTaskLogic()
        ttl.oracle2mongo()
    def test_xxkteachtask_oracle2mongo(self):
        from logic.jwxt.TeachTask import TeachTaskLogic
        ttl = TeachTaskLogic()
        ttl.xxkjxrw_oracle2mongo()
    def test_teacher_oracle2mongo(self):
        from logic.jwxt.Teacher import TeacherLogic
        TeacherLogic().oracle2mongo()

    def test_schedule_oracle2mongo(self):
        from logic.jwxt.Schedule import ScheduleLogic
        ScheduleLogic().oracle2mongo()

    def test_get_kcb(self):
        xkkh = '(2018-2019-1)-0030308051-070149-1'
        from logic.jwxt.Schedule import ScheduleLogic
        from common.convert import class2json
        sl = ScheduleLogic()
        result, num, msg = sl.get_schedule_by_xkkh(xkkh)
        # #print(result)
        for x in result:
            print(class2json(x))
        self.assertIsNotNone(result, msg)

    def test_copy_kcb(self):
        from logic.jwxt.Schedule import ScheduleLogic
        sl = ScheduleLogic()
        sl.oracle2mongo()
        result, num, msg = sl.get_all_fromdb()
        self.assertIsNotNone(result, msg)

    def test_get_dinstint_kcb(self):
        xkkh = '(2018-2019-1)-0030308051-070149-1'
        from logic.jwxt.Schedule import ScheduleLogic
        sl = ScheduleLogic()
        result, num, msg = sl.get_schedule_by_xkkh(xkkh)
        #print(class2json(result))
        self.assertIsNotNone(result)

    def test_rsa_encrypt_and_decrypt(self):
        mm = '52xuguoxu'
        from logic.common.Password import decrypt, encrypt
        c = encrypt(mm)
        #print(c)
        c = decrypt(c)
        self.assertEqual(mm, c)

    def test_aes_encrypt_and_decrypt(self):
        mm = '52xuguoxu'
        from logic.common.Password import prpcrypt
        c = prpcrypt.password_encrypt(mm)
        #print(c)
        w = prpcrypt.password_decrypt(c)
        #print(w)
        #print(len(w))
        #print(mm == w)
        self.assertEqual(mm, w)

if __name__ == '__main__':
    unittest.main(2)
