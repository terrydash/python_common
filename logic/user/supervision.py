from logic.Base import BaseLogic
from model.logic.Supervision import Supervision
from repository.BaseRepository import BaseRepository
from bson import ObjectId
from model.logic.Manager import Manager


class SupervisionLogic(BaseLogic):
    def __init__(self):
        from logic.common.Cache import CacheLogic
        self.cache = CacheLogic()
        self.collectionName = 'supervision'
        self.baseRepository = BaseRepository(collectionname=self.collectionName)

    def tomanager(self, id):
        query = {'_id': ObjectId(str(id))}
        result, num, msg = self.baseRepository.search_no_page(query=query, sort=None)
        if result is not None and num == 1:
            from logic.user.manager import ManagerLogic
            ml = ManagerLogic()
            m = dict(result[0])
            mm = Manager(m.get("zgh"), m.get("name"), m.get("xb"), m.get("bm"), m.get("mm"))
            ml.insert_one(mm)
            self.baseRepository.delete_one_by_id(id)
            return True, 1, "转移成功!"
        return False, 0, "ID不正确!"

    def insert_one(self, supervision: Supervision):
        query = {'zgh': supervision.zgh}
        result, num, msg = self.baseRepository.search_no_page(query=query, sort=None)
        print(result, num, msg)
        if len(result) > 0:
            return None, 0, '职工号重复！'

        return self.baseRepository.insert_one(supervision)

    def check_model(self, model: dict):
        finderr = False
        msg = '正常';
        if len(str(model.get("zgh")).strip()) <= 0:
            finderr = True
            msg = msg + "职工号不能为空"
        if len(str(model.get("mm")).strip()) <= 0:
            finderr = True
            msg = msg + "密码不能为空"
        if len(str(model.get("bm")).strip()) <= 0:
            finderr = True
            msg = msg + "部门不能为空"
        if len(str(model.get("name")).strip()) <= 0:
            finderr = True
            msg = msg + "姓名不能为空"
        if len(str(model.get("xb")).strip()) <= 0:
            finderr = True
            msg = msg + "性别不能为空"
        return finderr, msg

    def add_supervision(self, model: dict):
        query = {"zgh": str(model.get("zgh")).strip()}
        result, num, msg = self.baseRepository.search_no_page(query=query)
        if len(result) > 0 or num > 0:
            return False, 0, "职工号冲突！"
        sup = Supervision('', '', '', '', '')
        sup.zgh = str(model.get("zgh")).strip()
        sup.xb = str(model.get("xb")).strip()
        sup.name = str(model.get("name")).strip()
        from logic.common.Password import prpcrypt
        sup.mm = prpcrypt.password_encrypt(str(model.get("mm")).strip())
        sup.bm = str(model.get("bm")).strip()
        self.baseRepository.insert_one(sup)
        return True, 0, "正常"

    def get_passwd_by_zgh(self, zgh):
        query = {'zgh': zgh}
        result, num, msg = self.baseRepository.search_no_page(query=query, sort=None)
        if result is not None and len(result) > 0:
            passwd = result[0].get('mm')
            from logic.common.Password import prpcrypt
            return result, 1, prpcrypt.password_decrypt(passwd)
        result = None
        num = 0
        msg = '用户名或者密码!'
        return result, num, msg

    def get_by_zgh_and_passwd(self, zgh, mm):
        query = {'zgh': zgh}
        result, num, msg = self.baseRepository.search_no_page(query=query, sort=None)
        if result is not None and len(result) > 0:
            passwd = result[0].get('mm')
            from logic.common.Password import prpcrypt
            if mm == prpcrypt.password_decrypt(passwd):
                return result, 1, '正常'
        result = None
        num = 0
        msg = '用户名或者密码!'
        return result, num, msg
