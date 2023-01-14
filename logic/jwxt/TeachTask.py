# -*- coding: utf-8 -*-

import re

from common.convert import class2json
from common.convert import redisstr2list
from common.helper import copy_obj_attr
from config.const.redisPrefix import teachDeptPrefix
from db.RedisConn import redisConn
from logic.Base import BaseLogic
from logic.common.Config import ConfigLogic
from logic.jwxt.Department import DepartmentLogic
from model.logic.TeachTask import TeachTask
from model.oracle.models import *
from repository.BaseRepository import BaseRepository


class TeachTaskLogic(BaseLogic):
    def __init__(self):
        from logic.common.Cache import CacheLogic
        self.cache = CacheLogic()
        self.collectionName = str(TeachTask().COLLECTION_NAME)
        self.baseRepository = BaseRepository(collectionname=self.collectionName)

    def loadxlsx(self, content):

        import xlrd
        data = xlrd.open_workbook(file_contents=content)
        table = data.sheets()[0]
        nrows = table.nrows
        print(nrows)
        # return False, '失败'
        from logic.jwxt.TeachTask import TeachTaskLogic
        cl = ConfigLogic()
        xn = str(cl.getCurrentXN()).strip()
        xq = str(cl.getCurrentXQ()).strip()
        print("当前学年:" + xn)
        print("当前学期:" + xq)
        ttl = TeachTaskLogic()
        result, num, msg = ttl.get_all_fromdb()
        if num>0:
            tc: dict = result[0]
            tc.pop('_id')
        else:
            tc={}
        for x in range(1, nrows):
            print(x)
            row = table.row_values(x)
            print(table.row_values(x))
            tc['kcdm'] = str(float(str(row[0]).strip())).replace(".0", "")
            tc['kkxy'] = str(row[8]).strip()
            jszgh = str(float(str(row[2]).strip())).replace(".0", "")
            if len(str(jszgh)) > 6:
                jszgh = jszgh[0:6]
            while len(str(jszgh)) < 6:
                jszgh = "0" + str(jszgh)
            tc['xn'] = str(xn)
            tc['xq'] = int(xq)
            tc['jszgh'] = jszgh
            tc['jsxm'] = str(row[3]).strip()
            tc['qsz'] = 1
            tc['jsz'] = 16
            tc['kcxz'] = str(row[9]).strip()
            tc['cdbs'] = str(row[6]).strip()
            tc['bjmc'] = str(row[5]).strip()
            tc['bjrs'] = 0
            tc['xkkh'] = '(' + xn + '-' + xq + ')-' + str(tc['kcdm']) + '-' + str(tc['jszgh']) + '-1'
            tc['kcmc'] = str(row[1]).strip()
            tc['isimport'] = 1
            print(tc)
            q = {'xkkh':str(tc['xkkh'])}
            r, m, n = ttl.baseRepository.search_no_page(query=q)
            if r is not None and len(r) > 0:
                teachtask = r[0]
                ttl.update(str(teachtask.get("_id")), tc)
            else:
                ttl.baseRepository.insert_one(tc)
        return True, '正常!'

    def get_all_teach_dept_from_db(self):
        query = {r"is_teach_dept": 1}
        sort = '+_id'
        result, num, msg = self.search_no_page(query=query, sort=sort)
        return result, num, msg

    def get_all_page(self, page, pagesize, sort):
        querystr = {}
        cl = ConfigLogic()
        xn = str(cl.getCurrentXN()).strip()
        xq = str(cl.getCurrentXQ()).strip()
        querystr['xn'] = xn
        querystr['xq'] = int(xq)
        # print(querystr)
        result, num, msg = self.baseRepository.search_page(page, pagesize, querystr, sort)
        return result, num, msg

    def search_page(self, page, pagesize, query: dict, sort):
        querystr = {}
        name = str(query.get('name')).strip()
        dept = str(query.get('dept')).strip()
        if name is not None and len(name) > 0:
            querystr['jsxm'] = re.compile(name);
        if dept is not None and len(dept) > 0:
            querystr['kkxy'] = dept

        cl = ConfigLogic()
        xn = str(cl.getCurrentXN()).strip()
        xq = str(cl.getCurrentXQ()).strip()
        querystr['xn'] = xn
        querystr['xq'] = int(xq)
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
        self.cache.refresh_department()
        return result, num, msg

    def xxkjxrw_oracle2mongo(self):
        from db.OracleConn import DBSession
        session = DBSession()
        cl = ConfigLogic()
        xn = cl.getCurrentXN()
        xq = cl.getCurrentXQ()
        res = session.query(Xxkjxrwb).order_by(Xxkjxrwb.xkkh).filter(Xxkjxrwb.xn == xn, Xxkjxrwb.xq == xq).all()
        dl = DepartmentLogic()
        depts, num, msg = dl.get_all_fromdb()
        result = []
        if res is not None and len(res) > 0:
            # self.delete_all()
            for jxrwb in res:
                teachtask = TeachTask()
                teachtask = copy_obj_attr(jxrwb, teachtask)
                teachtask.bjmc = '混班'
                teachtask.bjrs = jxrwb.rs
                teachtask.kkxy = self.replacexymc(depts, jxrwb.kkxy)
                findit = False
                for tt in result:
                    if tt.xkkh == teachtask.xkkh:
                        findit = True
                if not findit:
                    result.append(teachtask)
                    self.baseRepository.insert_one(teachtask)
                    print(teachtask.__dict__)
            print(len(result))
            return res

    def oracle2mongo(self):
        from db.OracleConn import DBSession
        session = DBSession()
        cl = ConfigLogic()
        xn = cl.getCurrentXN()
        xq = cl.getCurrentXQ()
        print("当前学年:", xn)
        print("学期:", xq)
        res = session.query(Jxrwb).order_by(Jxrwb.xkkh).filter(Jxrwb.xn == xn, Jxrwb.xq == xq).all()
        dl = DepartmentLogic()
        depts, num, msg = dl.get_all_fromdb()
        print(len(res))
        print(depts)
        result = []
        if res is not None and len(res) > 0:
            self.delete_all(query={'isimport': None})
            self.delete_all(query={'isimport': 0})
            for jxrwb in res:
                teachtask = TeachTask()
                teachtask = copy_obj_attr(jxrwb, teachtask)
                teachtask.bjmc, teachtask.bjrs = self.getbjmcandbjrs(res, jxrwb.xkkh)
                teachtask.kkxy = self.replacexymc(depts, jxrwb.kkxy)
                findit = False
                for tt in result:
                    if tt.xkkh == teachtask.xkkh:
                        findit = True
                if not findit:
                    result.append(teachtask)
                    self.baseRepository.insert_one(teachtask)
            return res

    def getbjmcandbjrs(self, jxrwblist: list, xkkh: str):
        bjmc = ''
        bjrs = 0
        for x in jxrwblist:
            if x.xkkh == xkkh:
                if x.bjrs is not None:
                    bjrs = bjrs + int(x.bjrs)
                if len(bjmc) > 0:
                    bjmc = bjmc + "," + x.bjmc
                else:
                    bjmc = x.bjmc
        return bjmc, bjrs

    def replacexymc(self, xymcs: list, xymc):

        for x in xymcs:
            if str(x.get('name')) == str(xymc):
                return x.get('othername')
        return xymc
