# -*- coding: utf-8 -*-

import re

from common.convert import class2json
from common.convert import redisstr2list
from config.const.redisPrefix import teachDeptPrefix
from db.RedisConn import redisConn
from logic.Base import BaseLogic
from model.logic.Teacher import Teacher
from model.oracle.models import *
from repository.BaseRepository import BaseRepository


class TeacherLogic(BaseLogic):
    def __init__(self):
        from logic.common.Cache import CacheLogic
        self.cache = CacheLogic()
        self.collectionName = str(Teacher().COLLECTION_NAME)
        self.baseRepository = BaseRepository(collectionname=self.collectionName)

    def get_pass_by_id(self, _id):
        result, num, msg = self.baseRepository.get_by_id(_id)
        print(result)
        if result is not None:
            passwd = result.get('mm')
            from logic.common.Password import prpcrypt
            mm = prpcrypt.password_decrypt(passwd)
            result['mm'] = mm
        else:
            return None, 0, 'id不正确'
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

    def get_by_zgh(self, zgh):
        query = {'zgh': str(zgh).strip()}
        result, num, msg = self.baseRepository.search_no_page(query=query, sort=None)
        if result is not None and len(result) > 0:
            return result[0], 1, '正常'
        result = None
        num = 0
        msg = '未找到指定工号的教师'
        return result, num, msg

    def get_all_teach_dept_from_db(self):
        query = {r"is_teach_dept": 1}
        sort = '+_id'
        result, num, msg = self.search_no_page(query=query, sort=sort)
        return result, num, msg

    def search_page(self, page, pagesize, query: dict, sort):
        querystr = {}
        name = query.get('name')
        dept = query.get('dept')
        if name is not None and len(name) > 0:
            querystr['name'] = re.compile(str(name));
        if dept is not None and len(dept) > 0:
            querystr['bm'] = str(dept)
        # print(querystr)
        result, num, msg = self.baseRepository.search_page(page, pagesize, querystr, sort)
        return result, num, msg

    def get_all_teach_dept(self):
        if redisConn.exists(teachDeptPrefix):
            r = redisConn.get(teachDeptPrefix)
            result = redisstr2list(r)
            num = len(result)
            msg = '正常'
        else:
            result, num, msg = self.baseRepository.get_all_no_page()
            from logic.common.Cache import CacheLogic
            self.cache.refresh_department()
        return result, num, msg

    def update(self, id, entity):
        result, num, msg = self.baseRepository.update_by_id(id, class2json(entity))
        # self.cache.refresh_second_index()
        # from logic.course_evaluate.FirstIndex import FirstIndexLogic
        # FirstIndexLogic().refresh_second_index_num(entity.firstIndexID)
        # self.cache.refresh_department()
        return result, num, msg

    def oracle2mongo(self):
        from db.OracleConn import DBSession
        session = DBSession()
        res = session.query(Jsxxb).all()
        # print(len(res))
        result = []
        if res is not None and len(res) > 0:
            teachers, nums, msg = self.baseRepository.get_all_no_page()

            for jsxxb in res:
                teacher = Teacher()
                teacher.zgh = jsxxb.zgh
                teacher.name = jsxxb.xm
                teacher.bm = jsxxb.bm
                teacher.xb = jsxxb.xb if jsxxb.xb is not None else '未填写'
                t: Yhb = session.query(Yhb).filter(Yhb.yhm == jsxxb.zgh).first()
                from logic.common.Password import prpcrypt
                teacher.mm = prpcrypt.password_encrypt(str(t.jsmm))
                if teachers is not None and len(teachers) > 0:
                    findit = False
                    id = ''
                    # print(id)
                    # print(findit)
                    for teachertofind in teachers:
                        if str(teachertofind.get('zgh')) == str(jsxxb.zgh):
                            findit = True
                            id = str(teachertofind.get('_id'))
                            if id is not None and len(id) > 0:
                                self.baseRepository.update_by_id(id, teacher.__dict__)
                                break
                    if findit is False:
                        # print(teacher.__dict__)
                        self.baseRepository.insert_one(teacher)
                else:

                    self.baseRepository.insert_one(teacher)
            return res
