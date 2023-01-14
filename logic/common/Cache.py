# *_*coding:utf-8 *_*
from bson.json_util import dumps

from common.convert import class2json
from config.const.redisPrefix import *
from db.RedisConn import redisConn
from logic.course_evaluate.CourseEvaluate import CourseEvaluateLogic
from logic.course_evaluate.FirstIndex import FirstIndexLogic
from logic.course_evaluate.SecondIndex import SecondIndexLogic
from logic.jwxt.Department import DepartmentLogic


def read_data_to_cache(result: list, redis_prefix: str):
    r = dumps(class2json(result), ensure_ascii=False)
    # #print('刷新缓存--key:' + redis_prefix, " value:" + r)
    redisConn.set(redis_prefix, r)


class CacheLogic(object):
    def refresh_first_index(self):
        fil = FirstIndexLogic()
        result, num, data = fil.get_all_fromdb()
        read_data_to_cache(result, firstIndexPrefix)

    def refresh_second_index(self):
        sil = SecondIndexLogic()
        result, num, data = sil.get_all_fromdb()
        read_data_to_cache(result, secondIndexPrefix)

    def refresh_course_scheme(self):
        cel = CourseEvaluateLogic()
        result, num, data = cel.get_all_fromdb()
        read_data_to_cache(result, courseEvaluatePrefix)
        #print(len(result))
        if num>0:
            for cs in result:
                #print(str(cs.get("_id")))
                self.refresh_course_scheme_and_fis_sis(str(cs.get("_id")))

    def refresh_department(self):
        dl = DepartmentLogic()
        result, num, msg = dl.get_all_fromdb()
        read_data_to_cache(result, departmentPrefix)
        result, num, msg = dl.get_all_teach_dept_from_db()
        read_data_to_cache(result, teachDeptPrefix)

    def init(self):
        self.refresh_first_index()
        self.refresh_course_scheme()
        self.refresh_second_index()
        self.refresh_department()

    def refresh_course_scheme_and_fis_sis(self, schemeid):
        cel = CourseEvaluateLogic()
        scheme_info, num, msg = cel.get_ce_fis_sis(schemeid)
        if scheme_info is None:
            raise Exception(schemeid, "未找到")
        keyname = courseEvaluatePrefix + '_' + schemeid
        redisConn.set(keyname,dumps(class2json(scheme_info), ensure_ascii=False))
        redisConn.expire(keyname, 1000 * 60 * 60 * 24)
