# -*- coding: utf-8 -*-

from common.convert import class2json
from common.convert import redisstr2list
from config.const.redisPrefix import teachDeptPrefix
from db.RedisConn import redisConn
from logic.Base import BaseLogic
from model.logic.Department import Department
from model.oracle.models import *
from repository.BaseRepository import BaseRepository


class DepartmentLogic(BaseLogic):
    def __init__(self):
        from logic.common.Cache import CacheLogic
        self.cache = CacheLogic()
        self.collectionName = str(Department().COLLECTION_NAME)
        self.baseRepository = BaseRepository(collectionname=self.collectionName)

    def get_all_teach_dept_from_db(self):
        query = {r"is_teach_dept": 1}
        sort = '+_id'
        result, num, msg = self.search_no_page(query=query, sort=sort)
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
        self.cache.refresh_department()
        return result, num, msg

    def oracle2mongo(self):
        from db.OracleConn import DBSession
        session = DBSession()
        res = session.query(Xydmb).all()
        # print(len(res))
        result = []
        if res is not None and len(res) > 0:
            depts, nums, msg = self.baseRepository.get_all_no_page()

            for xydmb in res:
                dept = Department()
                dept.code = xydmb.xydm
                dept.name = xydmb.xymc

                if depts is not None and len(depts) > 0:
                    findit = False
                    id = ''
                    # print(id)
                    # print(findit)
                    for depttofind in depts:
                        if str(depttofind.get('code')) == str(xydmb.xydm):
                            findit = True
                            id = str(depttofind.get('_id'))
                            if id is not None and len(id) > 0:
                                self.baseRepository.update_by_id(id, dept.__dict__)
                                break
                    if findit is False:
                        # print(dict(dept))
                        self.baseRepository.insert_one(dept)
                else:
                    dept.othername = xydmb.xymc
                    dept.is_teach_dept = False
                    self.baseRepository.insert_one(dept)
            self.cache.refresh_department()
            return res
