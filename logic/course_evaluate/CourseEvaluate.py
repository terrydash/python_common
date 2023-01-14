from model.logic.CourseEvaluate import CourseEvaluate
from repository.BaseRepository import BaseRepository
import re
from db.RedisConn import redisConn
from config.const.redisPrefix import courseEvaluatePrefix
from common.convert import redisstr2list
from logic.course_evaluate.FirstIndex import FirstIndexLogic


# 课程评价标准逻辑
class CourseEvaluateLogic:

    def __init__(self):
        from logic.common.Cache import CacheLogic
        self.cache = CacheLogic()
        self.collectionName = str(CourseEvaluate().COLLECTION_NAME)
        self.baseRepository = BaseRepository(collectionname=self.collectionName)

    def search_page(self, page, pagesize, query, sort):
        result, num, msg = self.baseRepository.search_page(page, pagesize, dict(name=re.compile(query)), sort)
        return result, num, msg

    def get_ce_fis_sis(self, schemeid):
        result, num, msg = self.get_by_id(schemeid)
        scheme_info = {}
        if len(result) > 0:
            scheme_info = result
            fil = FirstIndexLogic()
            from logic.course_evaluate.SecondIndex import SecondIndexLogic
            sil = SecondIndexLogic()
            fis, num, msg = fil.search_no_page(schemeid=schemeid, sort=None)
            filist = []            
            for fi in fis:
                fi_id = fi.get('_id')
                query = {'firstIndexID': str(fi_id)}
                sis, num, msg = sil.search_no_page(query=query, sort=None)
                silist = []
                for si in sis:
                    if 'courseEvaluate' in si.keys():
                        si.pop('courseEvaluate')
                    if 'firstIndex' in si.keys():
                        si.pop('firstIndex')
                    silist.append(si)
                fi['second_index'] = silist
                if 'courseEvaluate' in fi.keys():
                    fi.pop('courseEvaluate')
                filist.append(fi)
            scheme_info['first_index'] = filist
            return scheme_info, 1, "正常"
        else:
            return None, 0, "schemeid错误"

    def get_all_page(self, page, pagesize, sort):
        result, num, msg = self.baseRepository.get_all_page(page, pagesize, sort)
        return result, num, msg

    def get_all_fromdb(self):
        result, num, msg = self.baseRepository.get_all_no_page()
        return result, num, msg

    def get_all_no_page(self):
        if redisConn.exists(courseEvaluatePrefix):
            r = redisConn.get(courseEvaluatePrefix)
            result = redisstr2list(r)
            num = len(result)
            msg = '正常'
        else:
            result, num, msg = self.baseRepository.get_all_no_page()
            from logic.common.Cache import CacheLogic
            self.cache.refresh_course_scheme()
        return result, num, msg

    def get_all_and_firstindex(self):
        result, num, msg = self.get_all_no_page()
        ceandfirstindex = []
        ce = {}
        for x in result:
            firesult, num_, msg = FirstIndexLogic().search_no_page(None, x.get('_id'), '+_id')
            fis = []
            for y in firesult:
                fis.append({'value': str(y.get('_id')), 'label': y.get('name')})
            ce = {'value': str(x.get('_id')), 'label': x.get('name'), 'children': fis}
            ceandfirstindex.append(ce)
        return ceandfirstindex, len(ceandfirstindex), '正常'

    def get_by_id(self, _id):
        result, num, msg = self.baseRepository.get_by_id(_id)
        return result, num, msg

    def delete_by_id(self, _id):
        result, num, msg = self.baseRepository.delete_one_by_id(_id)
        self.cache.refresh_course_scheme()
        return result, num, msg

    def insert(self, name, remarks, description):
        CE = CourseEvaluate()
        CE.description = description
        CE.remarks = remarks
        CE.secondIndexNum = 0
        CE.name = name
        CE.firstIndexNum = 0
        CE.courseNum = 0
        result, num, msg = self.baseRepository.insert_one(CE)
        self.cache.refresh_course_scheme()
        return result, num, msg

    def update(self, id, name, remarks, description):
        entity = {'name': name, 'remarks': remarks, 'description': description}
        # CE.firstIndexNum = 0
        # CE.courseNum = 0
        result, num, msg = self.baseRepository.update_by_id(id, entity)
        self.cache.refresh_course_scheme()
        return result, num, msg

    def refresh_first_index_num(self, id):
        num = 0
        if id is not None:
            from model.logic.FirstIndex import FirstIndex
            result, num, msg = BaseRepository(FirstIndex).search_no_page(query={"courseEvaluate._id": id}, sort=None)
        #print(id)
        #print(num)
        entity = {'firstIndexNum': num}
        result, num, msg = self.baseRepository.update_by_id(id, entity)
        self.cache.refresh_course_scheme()
        return result, num, msg

    def refresh_second_index_num(self, id):
        num = 0
        if id is not None:
            from model.logic.SecondIndex import SecondIndex
            result, num, msg = BaseRepository(SecondIndex).search_no_page(query={"courseEvaluate._id": id}, sort=None)
        #print(id)
        #print(num)
        entity = {'secondIndexNum': num}
        result, num, msg = self.baseRepository.update_by_id(id, entity)
        self.cache.refresh_course_scheme()
        return result, num, msg
