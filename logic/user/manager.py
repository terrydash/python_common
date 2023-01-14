from logic.Base import BaseLogic
from model.logic.Manager import Manager
from repository.BaseRepository import BaseRepository


class ManagerLogic(BaseLogic):
    def __init__(self):
        from logic.common.Cache import CacheLogic
        self.cache = CacheLogic()
        self.collectionName = 'manager'
        self.baseRepository = BaseRepository(
            collectionname=self.collectionName)

    def insert_one(self, m:Manager):
        query = {'zgh': m.zgh}
        result, num, msg = self.baseRepository.search_no_page(
            query=query, sort=None)
        print(result)
        print(result is None)
        if result is not None and len(result)==0:
            return self.baseRepository.insert_one(m)
        return None, 0, '职工号重复！'

    def get_passwd_by_zgh(self, zgh):
        query = {'zgh': zgh}
        result, num, msg = self.baseRepository.search_no_page(
            query=query, sort=None)
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
        result, num, msg = self.baseRepository.search_no_page(
            query=query, sort=None)
        if result is not None and len(result) > 0:
            passwd = result[0].get('mm')
            from logic.common.Password import prpcrypt
            if mm == prpcrypt.password_decrypt(passwd):
                return result, 1, '正常'
        result = None
        num = 0
        msg = '用户名或者密码!'
        return result, num, msg
