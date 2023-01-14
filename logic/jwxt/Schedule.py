# -*- coding: utf-8 -*-

import re

from common.convert import class2json
from common.helper import copy_obj_attr
from init.init_logging import get_logger
from logic.Base import BaseLogic
from logic.common.Config import ConfigLogic
from model.logic.Schedule import Schedule
from model.oracle.models import *
from repository.BaseRepository import BaseRepository
logger = get_logger(__name__)
class ScheduleLogic(BaseLogic):
    def __init__(self):
        from logic.common.Cache import CacheLogic
        self.cache = CacheLogic()
        self.collectionName = str(Schedule().COLLECTION_NAME)
        self.baseRepository = BaseRepository(collectionname=self.collectionName)

    def search_page(self, page, pagesize, query: dict, sort):
        querystr = {}
        name = str(query.get('name')).strip()
        dept = str(query.get('dept')).strip()
        if name is not None and len(name) > 0:
            querystr['jsxm'] = re.compile(name);
        if dept is not None and len(dept) > 0:
            querystr['kkxy'] = dept
        # print(querystr)
        result, num, msg = self.baseRepository.search_page(page, pagesize, querystr, sort)
        return result, num, msg

    def get_schedule_by_xkkh(self, xkkh):
        from config.systemconfig import get_config
        kcb_from_oracle = get_config('kcb_from_oracle')
        logger.info({'kcb_from_oracle': kcb_from_oracle})
        result = []
        if kcb_from_oracle == 1:
            try:
                from db.OracleConn import DBSession
                session = DBSession()
                result: list = session.query(Tjkbapqkb).order_by(Tjkbapqkb.qssj).order_by(Tjkbapqkb.xqj).order_by(
                    Tjkbapqkb.sjdxh).filter(
                    Tjkbapqkb.xkkh == xkkh).all()
            except Exception as err:
                logger.error(err)
                query = {'xkkh': xkkh}
                result, num, msg = self.baseRepository.search_no_page(query=query)
        else:
            query = {'xkkh': xkkh}
            result, num, msg = self.baseRepository.search_no_page(query=query)
        disintresult = []
        logger.debug(result)
        for x in result:

            z = Schedule()
            y = x
            z = copy_obj_attr(y, z)
            if kcb_from_oracle == 1:
                if x.dsz == '单':
                    y.dsz = '双'
                    if y in result:
                        z.dsz = ''
                elif x.dsz == '双':
                    y = x
                    y.dsz = '单'
                    if y in result:
                        z.dsz = ''
            else:
                if x.get('dsz') == '单':
                    y['dsz'] = '双'
                    if y in result:
                        z.dsz = ''
                elif x['dsz'] == '双':
                    y = x
                    y['dsz'] = '单'
                    if y in result:
                        z.dsz = ''
            z = class2json(z)
            if z not in disintresult:
                disintresult.append(z)
        # disintresult = list(set(disintresult))
        # print(disintresult)
        return disintresult, len(disintresult), '正常'

    def get_schedule_by_actyear(self):
        from db.OracleConn import DBSession
        cl = ConfigLogic()
        actyear = str(cl.getCurrentActYear()).strip()
        session = DBSession()
        # print(actyear)
        result = session.query(Tjkbapqkb).order_by(Tjkbapqkb.xqj).filter(
            Tjkbapqkb.xkkh.like("(" + actyear + ")%")).all()
        return result, len(result), '正常'

    def update(self, id, entity):
        result, num, msg = self.baseRepository.update_by_id(id, class2json(entity))
        # self.cache.refresh_second_index()
        # from logic.course_evaluate.FirstIndex import FirstIndexLogic
        # FirstIndexLogic().refresh_second_index_num(entity.firstIndexID)
        self.cache.refresh_department()
        return result, num, msg

    def oracle2mongo(self):
        res, num, msg = self.get_schedule_by_actyear()
        logger.debug('开始执行课表ORALCE读取到MongoDB')
        # print(len(res))
        if res is not None and len(res) > 0:
            self.delete_all()
            entites = []
            for schedulefromoracle in res:
                schedule = Schedule()
                schedule = copy_obj_attr(schedulefromoracle, schedule)
                entity = class2json(schedule)
                # print(entity)
                entites.append(schedule)
            self.baseRepository.insert_many(entites)
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
        return '未知学院'
