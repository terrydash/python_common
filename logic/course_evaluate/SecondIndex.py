# *_*coding:utf-8 *_*
from model.logic.SecondIndex import SecondIndex as SILogic
from repository.BaseRepository import BaseRepository
from model.logic.CourseEvaluate import CourseEvaluate
from model.logic.FirstIndex import FirstIndex
from model.logic.SecondIndex import SecondIndex
from db.RedisConn import redisConn
from config.const.redisPrefix import secondIndexPrefix
import re
from common.convert import class2json, redisstr2list


# 课程评价标准逻辑
class SecondIndexLogic:
    def __init__(self):
        from logic.common.Cache import CacheLogic
        self.cache = CacheLogic()
        self.collectionName = str(SecondIndex().COLLECTION_NAME)
        self.baseRepository = BaseRepository(collectionname=self.collectionName)

    def check_model(self, model: dict):
        result = True
        msg = ''
        si = SecondIndex()
        if 'name' in model.keys() and len(model.get('name')) > 0:
            si.name = model.get('name')
        else:
            msg += '名称不能为空!'
            result = False
        if 'schemeid' in model.keys() and len(model.get('schemeid')) > 0:
            si.courseEvaluateID = model.get('schemeid')
        else:
            msg += '所属课程方案不能为空!'
            result = False
        if 'firstindexid' in model.keys() and len(model.get('firstindexid')) > 0:
            si.firstIndexID = model.get('firstindexid')
        else:
            msg += '所属一级指标不能为空!'
            result = False
        if 'schemetype' in model.keys() and len(str(model.get('schemetype'))) > 0:
            si.scheme_type = model.get('schemetype')
        else:
            msg += '所属表现形势不能为空!'
            result = False
        if 'order' in model.keys() and len(str(model.get('order'))) > 0:
            si.order = model.get('order')
        else:
            msg += '排序序号不能为空!'
            result = False
        if 'description' in model.keys():
            si.description = model.get('description')
        if 'height' in model.keys():
            si.height = model.get('height')
        if 'width' in model.keys():
            si.width = model.get('width')
        if 'value' in model.keys():
            si.value = model.get('value')
        if 'remarks' in model.keys():
            si.remarks = model.get('remarks')
        if 'isdeptcanreply' in model.keys():
            si.is_department_can_reply = model.get('isdeptcanreply')
        if 'isdeptcansee' in model.keys():
            si.is_department_can_see = model.get('isdeptcansee')
        if 'isteachercanreply' in model.keys():
            si.is_teacher_can_reply = model.get('isteachercanreply')
        if 'isdeptcansee' in model.keys():
            si.is_teacher_can_see = model.get('isteachercansee')

        if not result:
            return result, None, msg
        else:
            return result, si, '正常'

    def search_page(self, page, pagesize, name, firstindexid, sort):
        query = {}
        if name is not None and len(name) > 0:
            query['name'] = re.compile(name);
        if firstindexid is not None and len(firstindexid) > 0:
            query['firstIndexID'] = str(firstindexid)
        #print(query)
        result, num, msg = self.baseRepository.search_page(page, pagesize, query, sort)
        return result, num, msg

    def search_no_page(self, name, schemeid, sort):
        query = {}
        if name is not None and len(name) > 0:
            query['name'] = re.compile(name);
        if schemeid is not None and len(schemeid) > 0:
            query['courseEvaluate._id'] = str(schemeid)
        #print(query)
        result, num, msg = self.baseRepository.search_no_page(query, sort)
        return result, num, msg

    def search_no_page(self, query, sort):
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
            from logic.course_evaluate.CourseEvaluate import CourseEvaluateLogic
            CourseEvaluateLogic().refresh_second_index_num(schemeid)
            self.cache.refresh_first_index()
        return result_, num, msg

    def insert(self, si: SecondIndex):
        ce, num, msg = BaseRepository(entity=CourseEvaluate).get_by_id(si.courseEvaluateID)
        if ce is not None:
            si.courseEvaluate = ce
        fi, num, msg = BaseRepository(entity=FirstIndex).get_by_id(si.firstIndexID)
        del fi['courseEvaluate']
        if fi is not None:
            si.firstIndex = fi
        result, num, msg = self.baseRepository.insert_one(si)
        self.cache.refresh_second_index()
        from logic.course_evaluate.FirstIndex import FirstIndexLogic
        FirstIndexLogic().refresh_second_index_num(si.firstIndexID)
        from logic.course_evaluate.CourseEvaluate import CourseEvaluateLogic
        CourseEvaluateLogic().refresh_second_index_num(si.courseEvaluateID)
        return result, num, msg

    def update(self, id,entity:SecondIndex):
        result, num, msg = self.baseRepository.update_by_id(id, class2json(entity))
        self.cache.refresh_second_index()
        from logic.course_evaluate.FirstIndex import FirstIndexLogic
        FirstIndexLogic().refresh_second_index_num(entity.firstIndexID)
        from logic.course_evaluate.CourseEvaluate import CourseEvaluateLogic
        CourseEvaluateLogic().refresh_second_index_num(entity.courseEvaluateID)
        return result, num, msg
