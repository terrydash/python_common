from logic.Base import BaseLogic
from model.logic.DeptManager import DeptManager
from repository.BaseRepository import BaseRepository


class DeptMangerLogic(BaseLogic):
    def __init__(self):
        from logic.common.Cache import CacheLogic
        self.cache = CacheLogic()
        self.collectionName = 'deptmanager'
        self.baseRepository = BaseRepository(collectionname=self.collectionName)

    def insert_one(self, deptmanager: DeptManager):
        query = {'zgh': deptmanager.zgh}
        result, num, msg = self.baseRepository.search_no_page(query=query, sort=None)
        print(result, num, msg)
        if len(result) > 0:
            return None, 0, '职工号重复！'
        return self.baseRepository.insert_one(deptmanager)

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
        msg = '用户名或者密码错误!'
        return result, num, msg

    def get_by_zgh(self, zgh):
        query = {'zgh': zgh}
        result, num, msg = self.baseRepository.search_no_page(query=query, sort=None)
        if result is not None:
            from logic.common.Password import prpcrypt
            result[0]['jsmm'] = prpcrypt.password_decrypt(result[0].get('mm'))
        return result, num, msg
