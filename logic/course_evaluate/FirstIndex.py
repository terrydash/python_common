# *_*coding:utf-8 *_*
from model.logic.FirstIndex import FirstIndex
from model.logic.SecondIndex import SecondIndex
from repository.BaseRepository import BaseRepository
from model.logic.CourseEvaluate import CourseEvaluate
from db.RedisConn import redisConn
from config.const.redisPrefix import firstIndexPrefix
import re
from common.convert import class2json, redisstr2list


# 课程评价标准逻辑
class FirstIndexLogic:
    def __init__(self):
        from logic.common.Cache import CacheLogic
        self.cache = CacheLogic()
        self.collectionName = str(FirstIndex().COLLECTION_NAME)
        self.baseRepository = BaseRepository(collectionname=self.collectionName)

    def search_page(self, page, pagesize, name, schemeid, sort):
        query = {}
        if name is not None and len(name) > 0:
            query['name'] = re.compile(name);
        if schemeid is not None and len(schemeid) > 0:
            query['courseEvaluate._id'] = str(schemeid)
        #print(query)
        result, num, msg = self.baseRepository.search_page(page, pagesize, query, sort)
        return result, num, msg

    def search_no_page(self, name='', schemeid='', sort=None):
        query = {}
        if name is not None and len(name) > 0:
            query['name'] = re.compile(name);
        if schemeid is not None and len(schemeid) > 0:
            query['courseEvaluate._id'] = str(schemeid)
        #print(query)
        result, num, msg = self.baseRepository.search_no_page(query, sort)
        return result, num, msg

    def get_all_page(self, page, pagesize, sort):
        result, num, msg = self.baseRepository.get_all_page(page, pagesize, sort)
        return result, num, msg

    def get_all_fromdb(self):
        result, num, msg = self.baseRepository.get_all_no_page()
        return result, num, msg

    def get_by_id(self, _id):
        result, num, msg = self.baseRepository.get_by_id(_id)
        return result, num, msg

    def delete_by_id(self, _id):
        result, num_, msg_ = self.baseRepository.get_by_id(_id)
        if result is not None and 'courseEvaluate' in result.keys() and '_id' in result.get('courseEvaluate').keys():
            #print('执行刷新数量！')
            schemeid = result.get('courseEvaluate').get('_id')
            from logic.course_evaluate.CourseEvaluate import CourseEvaluateLogic
            result_, num, msg = self.baseRepository.delete_one_by_id(_id)
            CourseEvaluateLogic().refresh_first_index_num(schemeid)
        self.cache.refresh_first_index()
        return result_, num, msg

    def insert(self, name, remarks, description, schemeid, issingle, proportion,secondIndexType):
        fi = FirstIndex()
        fi.description = description
        fi.remarks = remarks
        fi.secondIndexNum = 0
        fi.name = name
        fi.secondIndexIsSingle = bool(issingle)
        fi.proportion = int(proportion)
        fi.secondIndexType=secondIndexType
        ce, num, msg = BaseRepository(entity=CourseEvaluate).get_by_id(schemeid)
        if ce is not None:
            fi.courseEvaluate = ce
        result, num, msg = self.baseRepository.insert_one(fi)
        self.cache.refresh_first_index()
        from logic.course_evaluate.CourseEvaluate import CourseEvaluateLogic
        CourseEvaluateLogic().refresh_first_index_num(schemeid)
        return result, num, msg

    def update(self, id, name, remarks, description, schemeid, issingle, proportion,secondtype):
        ce, num, msg = BaseRepository(entity=CourseEvaluate).get_by_id(schemeid)
        entity = FirstIndex()
        entity.name = name
        entity.description = description
        entity.remarks = remarks
        if ce is not None:
            entity.courseEvaluate = ce
        # CE.firstIndexNum = 0
        # CE.courseNum = 0
        entity.secondIndexIsSingle = bool(issingle)
        entity.proportion = int(proportion)
        entity.secondIndexType=int(secondtype)
        #print(entity.secondIndexIsSingle)
        result, num, msg = self.baseRepository.update_by_id(id, class2json(entity))
        self.cache.refresh_first_index()
        return result, num, msg

    def refresh_second_index_num(self, id):
        num = 0
        if id is not None:
            from model.logic.SecondIndex import SecondIndex
            result, num, msg = BaseRepository(SecondIndex).search_no_page(query={"firstIndexID": id}, sort=None)
        #print(id)
        #print(num)
        entity = {'secondIndexNum': num}
        result, num, msg =  BaseRepository(FirstIndex).update_by_id(id, entity)
        self.cache.refresh_first_index()
        return result, num, msg
