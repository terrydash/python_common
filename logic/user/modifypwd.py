from logic.Base import BaseLogic


class ModifyPWDLogic(BaseLogic):
    def modify_pwd(self, tokenmodel: dict, userpwdmodel: dict):
        roleid = int(tokenmodel.get('roleid'))
        userid = str(tokenmodel.get('id'))
        oldpwd = str(userpwdmodel.get('opwd'))
        if self.check_pwd(oldpwd=oldpwd, roleid=roleid, userid=userid):
            newpwd = str(userpwdmodel.get('newpwd'))
            return self.do_modify(newpwd=newpwd, roleid=roleid, userid=userid)
        else:
            return None, 0, '原密码不正确！'

    def do_modify(self, newpwd, roleid, userid):
        from logic.common.Password import prpcrypt
        newpwd = prpcrypt.password_encrypt(newpwd)
        entity = {'mm': newpwd}
        try:
            if roleid == 1:
                from logic.jwxt.Teacher import TeacherLogic
                tl = TeacherLogic()
                return tl.baseRepository.update_by_id(userid, entity)
            elif roleid == 2:
                from logic.user.supervision import SupervisionLogic
                svl = SupervisionLogic()
                return svl.baseRepository.update_by_id(userid, entity)
            elif roleid == 3:
                from logic.user.deptmanager import DeptMangerLogic
                dml = DeptMangerLogic()
                return dml.baseRepository.update_by_id(userid, entity)
            elif roleid == 4:
                from logic.user.admin import AdminLogic
                al = AdminLogic()
                return al.baseRepository.update_by_id(userid, entity)
            elif roleid == 5:
                from logic.user.manager import ManagerLogic
                al = ManagerLogic()
                return al.baseRepository.update_by_id(userid, entity)
            else:
                return None, 0, '角色类型不正确'
        except Exception as err:
            return None, 0, err.__str__()

    def check_pwd(self, oldpwd, roleid, userid):

        from logic.common.Password import prpcrypt

        if roleid == 1:
            from logic.jwxt.Teacher import TeacherLogic
            tl = TeacherLogic()
            teacher,num,msg = tl.get_by_id(userid)
            pwdindb = prpcrypt.password_decrypt(str(teacher.get('mm')))
        elif roleid == 2:
            from logic.user.supervision import SupervisionLogic
            svl = SupervisionLogic()
            supervision,num,msg = svl.get_by_id(userid)
            pwdindb = prpcrypt.password_decrypt(str(supervision.get('mm')))
        elif roleid == 3:
            from logic.user.deptmanager import DeptMangerLogic
            dml = DeptMangerLogic()
            deptmanager,num,msg = dml.get_by_id(userid)
            pwdindb = prpcrypt.password_decrypt(str(deptmanager.get('mm')))
        elif roleid == 4:
            from logic.user.admin import AdminLogic
            al = AdminLogic()
            admin,num,msg = al.get_by_id(userid)
            pwdindb = prpcrypt.password_decrypt(str(admin.get('mm')))
        elif roleid == 5:
            from logic.user.manager import ManagerLogic
            al = ManagerLogic()
            manager, num, msg = al.get_by_id(userid)
            print(manager)
            pwdindb = prpcrypt.password_decrypt(str(manager.get('mm')))
            print(pwdindb)
        else:
            return False
        return pwdindb == oldpwd
        pass
