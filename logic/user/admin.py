# -*- coding: utf-8 -*-
# @Time    : 2018/8/11 下午7:54
# @Author  : Aries
# @Site    : 
# @File    : admin.py
# @Software: PyCharm
from common.convert import class2json
from logic.Base import BaseLogic
from model.logic.Admin import Admin
from repository.BaseRepository import BaseRepository


class AdminLogic(BaseLogic):
    def __init__(self):
        from logic.common.Cache import CacheLogic
        self.cache = CacheLogic()
        self.collectionName = 'administrator'
        self.baseRepository = BaseRepository(collectionname=self.collectionName)

    def check_model(self, model: dict):
        finderr = False
        msg = '正常';
        if len(str(model.get("username")).strip()) <= 0:
            finderr = True
            msg = msg + "用户名不能为空"
        if len(str(model.get("mm")).strip()) <= 0:
            finderr = True
            msg = msg + "密码不能为空"
        if len(str(model.get("truemname")).strip()) <= 0:
            finderr = True
            msg = msg + "真实姓名不能为空"
        if len(str(model.get("bm")).strip()) <= 0:
            finderr = True
            msg = msg + "部门不能为空"
        return finderr, msg

    def update_admin(self, model: dict):
        if len(str(model.get("_id")).strip()) <= 0:
            return False, 0, "ID不正确！"
        id = str(model.get("_id")).strip()

        result, num, msg = self.baseRepository.get_by_id(id)
        if result is None or num < 1:
            return False, 0, "ID不存在！"

        from bson import ObjectId
        query = {"username": str(model.get("username")).strip(), "_id": {'$ne':ObjectId(str(id))}}
        print(query)
        result, num, msg = self.baseRepository.search_no_page(query=query)
        if len(list(result)) >= 1 or num >= 1:
            return False, 0, "用户名冲突！"
        sup = Admin()
        sup.username = str(model.get("username")).strip()
        sup.truename = str(model.get("truename")).strip()
        sup.bm = str(model.get("bm")).strip()
        from logic.common.Password import prpcrypt
        sup.mm = prpcrypt.password_encrypt(str(model.get("mm")).strip())
        print(sup)
        self.baseRepository.update_by_id(_id=id,entity=class2json(sup))
        return True, 0, "正常"

    def add_admin(self, model: dict):
        query = {"username": str(model.get("username")).strip()}
        result, num, msg = self.baseRepository.search_no_page(query=query)
        if len(result) > 0 or num > 0:
            return False, 0, "用户名冲突！"
        sup = Admin()
        sup.username = str(model.get("username")).strip()
        sup.truename = str(model.get("truename")).strip()
        sup.bm = str(model.get("bm")).strip()
        from logic.common.Password import prpcrypt
        sup.mm = prpcrypt.password_encrypt(str(model.get("mm")).strip())
        self.baseRepository.insert_one(sup)
        return True, 0, "正常"

    def insert_one(self, admin: Admin):
        query = {'username': admin.username}

        result, num, msg = self.baseRepository.search_no_page(query=query, sort=None)
        if num > 0:
            return None, 0, '用户名重复！'
        from logic.common.Password import prpcrypt
        admin.mm = prpcrypt.password_encrypt(admin.mm)
        return self.baseRepository.insert_one(admin)

    def get_by_username_and_passwd(self, username, mm):
        query = {'username': username}
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
