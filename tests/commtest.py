import unittest

from common.convert import class2json
from config.startupconfig import init_config
from logic.common.Login import CheckToken


class mytest(unittest.TestCase):
    # setUp()初始化,
    def setUp(self):
        self.config = init_config
        from logic.common.Login import GetUUID, GetVcode
        self.uuid = GetUUID()
        buf, self.vcode = GetVcode(self.uuid)

    # 销毁
    def tearDown(self):
        pass

    # 具体的测试用例，以test开头
    def test_login_teacher(self):
        username = "070149"
        password = "52xuguoxu"
        logintype = "1"
        # print(self.uuid, self.vcode)
        from logic.common.Login import CheckLogin
        result, entity, token, msg = CheckLogin(username, password, self.uuid, self.vcode, logintype)
        # print(class2json(entity))
        # print(token)
        # print(msg)
        self.assertTrue(result)

    def test_update_activate(self):
        from logic.common.Config import ConfigLogic
        cl = ConfigLogic()
        cl.updateActiveCode('SSSHD1UZcMjwgxsJPAkhfq32NGcwcCz7yoNEqP8Ie1a06IrMvxZYA9FaFldLceyJ')

    def test_login_supervision(self):
        username = "000001"
        password = "000000"
        logintype = "2"
        # print(self.uuid, self.vcode)
        from logic.common.Login import CheckLogin
        result, entity, token, msg = CheckLogin(username, password, self.uuid, self.vcode, logintype)
        # print(class2json(entity))
        # print(token)
        # print(msg)
        self.assertTrue(result)

    def test_login_deptmanager(self):
        username = "000001"
        password = "000000"
        logintype = "3"
        # print(self.uuid, self.vcode)
        from logic.common.Login import CheckLogin
        result, entity, token, msg = CheckLogin(username, password, self.uuid, self.vcode, logintype)
        # print(class2json(entity))
        # print(token)
        # print(msg)
        self.assertTrue(result)

    def test_login_admin(self):
        username = "xuguoxu"
        password = "52xuguoxu"
        logintype = "4"
        # print(self.uuid, self.vcode)
        from logic.common.Login import CheckLogin
        result, entity, token, msg = CheckLogin(username, password, self.uuid, self.vcode, logintype)
        # print(class2json(entity))
        # print(token)
        # print(msg)
        self.assertTrue(result)

    def test_teacher_oracle2mongo(self):
        from logic.jwxt.Teacher import TeacherLogic
        tl = TeacherLogic()
        result = tl.oracle2mongo()
        self.assertIsNotNone(result)

    def test_get_teacher(self):
        from logic.jwxt.Teacher import TeacherLogic
        tl = TeacherLogic()
        result, num, msg = tl.get_by_zgh("080309")
        from model.common.jsonModel import response_normal
        print(response_normal(data=result).to_json())

    def test_getpassword(self):
        from logic.common.Password import prpcrypt
        print(prpcrypt.password_decrypt(r"b+L18FpGosexzvWmLZ1cFPKirKfQwMJjkTeKhW2NbNk=\n"))

    def test_check_token(self):
        username = "xuguoxu"
        password = "52xuguoxu"
        logintype = "4"
        # print(self.uuid, self.vcode)
        from logic.common.Login import CheckLogin
        result, entity, token, msg = CheckLogin(username, password, self.uuid, self.vcode, logintype)
        # print(token)
        result, entity, msg = CheckToken(token)
        # print(class2json(entity))
        # print(msg)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main(2)
