import re

from config.const.redisPrefix import courseEvaluatePrefix
from db.RedisConn import redisConn
from init.init_logging import get_logger
from logic.Base import BaseLogic
from model.logic.Score import Score

logger = get_logger(__name__)


class ScoreLogic(BaseLogic):
    def __init__(self):
        from logic.common.Cache import CacheLogic
        self.cache = CacheLogic()
        self.collectionName = str(Score().COLLECTION_NAME)
        from repository.BaseRepository import BaseRepository
        self.baseRepository = BaseRepository(collectionname=self.collectionName)

    def get_by_id_check_role(self, _id, userinfo):
        result, num, msg = self.baseRepository.get_by_id(_id)
        print(result)

        if int(userinfo.get('roleid')) != 1 and int(userinfo.get('roleid')) != 4 and result is not None:
            result['is_teacher_judge_supervison'] = 0
            result['teacher_judge_supervison_result'] = ""
        return result, num, msg

    def delete_by_id(self, _id: str, userinfo: dict):
        result, num_, msg_ = self.baseRepository.get_by_id(_id)
        if result is not None:
            # result_, num, msg = self.baseRepository.delete_one_by_id(_id)
            score_user_info: dict = result.get('score_user_info')
            if score_user_info.get('id') != userinfo.get('id'):
                return None, 0, '只能删除自己评价的方案'
            result['status'] = 'deleted'
            result, num, msg = self.baseRepository.update_by_id(_id, result)
        else:
            return None, 0, 'id不正确'
        return result, num, msg

    def get_export(self, page: int, pagesize: int, sort: str, teacher_name: str, dept: str,
                   actyear: str, schemeid: str):
        query = {}
        if actyear is not None and len(actyear) > 0:
            query['actyear'] = actyear
        if teacher_name is not None and len(teacher_name) > 0:
            query['jsxm'] = re.compile(teacher_name)
        if schemeid is not None and len(schemeid) > 0:
            query['schemeid'] = str(schemeid)
        if dept is not None and len(dept) > 0:
            query['kkxy'] = dept
        ziduan = {'result': 0, 'content': 0, 'comment': 0}
        return self.baseRepository.search_page(page=page, pagesize=pagesize, query=query, sort=sort, ziduan=ziduan)

    def get_with_userinfo(self, userinfo: dict, page: int, pagesize: int, sort: str, teacher_name: str, dept: str,
                          actyear: str, supervision_name: str):
        query = {'score_user_info.id': userinfo.get('id'), 'actyear': actyear, 'status': 'normal'}

        if int(userinfo.get('roleid')) == 2:
            if teacher_name is not None and len(teacher_name) > 0:
                query['jsxm'] = re.compile(teacher_name)
            if dept is not None and len(dept) > 0:
                query['kkxy'] = dept
        elif int(userinfo.get('roleid')) == 1:
            if teacher_name is not None and len(teacher_name) > 0:
                query['jsxm'] = re.compile(teacher_name)
            if dept is not None and len(dept) > 0:
                query['kkxy'] = dept
        elif int(userinfo.get('roleid')) == 3:
            if teacher_name is not None and len(teacher_name) > 0:
                query['jsxm'] = re.compile(teacher_name)
            query['kkxy'] = userinfo.get('bm')
            query.pop('score_user_info.id')
            # print(userinfo.get('bm'))
        elif int(userinfo.get('roleid')) == 4:
            if teacher_name is not None and len(teacher_name) > 0:
                query['jsxm'] = re.compile(teacher_name)
            if supervision_name is not None and len(supervision_name) > 0:
                query['score_user_info.name'] = str(supervision_name)
            if dept is not None and len(dept) > 0:
                query['kkxy'] = dept
            if 'score_user_info.id' in query.keys():
                query.pop('score_user_info.id')
            query.pop('status')
        elif int(userinfo.get('roleid')) == 5:
            if teacher_name is not None and len(teacher_name) > 0:
                query['jsxm'] = re.compile(teacher_name)
            if supervision_name is not None and len(supervision_name) > 0:
                query['score_user_info.name'] = str(supervision_name)
            if dept is not None and len(dept) > 0:
                query['kkxy'] = dept
            query.pop('status')
        else:
            return None, 0, '权限不正确'
        logger.debug(query)
        logger.debug(userinfo)
        ziduan = {'result': 0, 'content': 0, 'comment': 0}
        return self.baseRepository.search_page(page=page, pagesize=pagesize, query=query, sort=sort, ziduan=ziduan)

    def get_with_userinfo_for_teacher_history(self, userinfo: dict, page: int, pagesize: int, sort: str, actyear: str):
        query = {'actyear': actyear, 'status': 'normal'}
        from logic.jwxt.Teacher import TeacherLogic
        tl = TeacherLogic()
        teacher, num, result = tl.get_by_id(userinfo.get('id'))
        # print(teacher)
        jszgh: str = str(teacher.get('zgh'))
        query['jszgh'] = jszgh
        logger.debug(query)
        logger.debug(userinfo)
        return self.baseRepository.search_page(page=page, pagesize=pagesize, query=query, sort=sort)

    def insert_v2(self, score: dict):
        from logic.common.Login import GetUserInfoFromToken
        result, userinfo = GetUserInfoFromToken()
        if not result:
            return None, 0, 'Token过期或者错误！'
        if score['result'] is not None and len(score['result']) > 0:
            sum = 0
            for element in score['result']:
                fi: dict = element['fi']
                si: dict = element['si']
                if not isinstance(si, list):
                    sum = sum + int(fi.get('proportion')) * int(si.get('value')) / 100
                else:
                    for sis in si:
                        sum = sum + int(fi.get('proportion')) * int(sis.get('value')) / 100
            score['totalscore'] = int(sum)
        jszgh = score.get('jszgh')
        if len(str(jszgh)) > 6:
            score['jszgh'] = str(jszgh)[0:6]
        zz = r"<img[^>]*>"
        if len(str(score["content"])) > 5000:
            score["content"] = re.sub(zz, "", str(score["content"]))
        if len(str(score["comment"])) > 5000:
            score["comment"] = re.sub(zz, "", str(score["comment"]))
        score['score_user_info'] = userinfo
        score['is_dept_reply'] = False
        score['dept_manager_reply'] = ""
        score['is_teacher_reply'] = False
        score['teacher_reply'] = ""
        score['is_teacher_judge_supervison'] = False
        score['teacher_judge_supervison_result'] = ""
        score['teacher_judge_supervison_score'] = 0
        import datetime
        score['commit_date'] = str(datetime.date.today())
        score['status'] = 'normal'
        self.baseRepository.insert_one(score)
        return score, 1, '提交成功!'

    def insert(self, score: dict):
        from logic.common.Login import GetUserInfoFromToken
        result, userinfo = GetUserInfoFromToken()
        if not result:
            return None, 0, 'Token过期或者错误！'
        if score['result'] is not None and len(score['result']) > 0:
            sum = 0
            for element in score['result']:
                fi: dict = element['fi']
                si: dict = element['si']
                sum = sum + int(fi.get('proportion')) * int(si.get('value')) / 100
            score['totalscore'] = int(sum)
        jszgh = score.get('jszgh')
        if len(str(jszgh)) > 6:
            score['jszgh'] = str(jszgh)[0:6]
        score['score_user_info'] = userinfo
        score['is_dept_reply'] = False
        score['dept_manager_reply'] = ""
        score['is_teacher_reply'] = False
        score['teacher_reply'] = ""
        score['is_teacher_judge_supervison'] = False
        score['teacher_judge_supervison_result'] = ""
        score['teacher_judge_supervison_score'] = 0
        import datetime
        score['commit_date'] = str(datetime.date.today())
        score['status'] = 'normal'
        self.baseRepository.insert_one(score)
        return score, 1, '提交成功!'

    def check_model(self, score: dict):
        key_name_list = ["jszgh", "jsxm", "kkxy", "tksj", "jc", "js", "bjrs", "sjrs", "cdrs", "kkrs", "content",
                         "result", "totalscore", "comment", "xkkh", "xn", "xq", "actyear", "schemeid", "bjmc", "kcmc"]
        from common.dicthelper import dictHelper
        dh = dictHelper(score)
        checkresult, bad_name_list = dh.check_keys(key_name_list)
        result = False
        num = 0
        err_msg = '参数问题'
        if checkresult:
            from logic.course_evaluate.FirstIndex import FirstIndexLogic
            from logic.course_evaluate.CourseEvaluate import CourseEvaluateLogic
            from logic.jwxt.TeachTask import TeachTaskLogic
            ttl = TeachTaskLogic()
            cel = CourseEvaluateLogic()
            fil = FirstIndexLogic()
            schemeid = score['schemeid']
            schemes, num, msg = cel.get_by_id(schemeid)
            fis, num, msg = fil.search_no_page(schemeid=schemeid)
            xkkh = score['xkkh']
            teacktasks = ttl.search_no_page({'xkkh': xkkh})
            if len(schemes) > 0 and len(fis) > 0 and len(teacktasks) > 0:
                if len(fis) == len(score['result']):
                    result = True
                    err_msg = '检查成功'
                else:
                    err_msg = '选项数量不正确，请填写完整！'
            else:
                err_msg = 'schemeid或者xkkh不正确'
        return result, num, err_msg

    def get_course_info_and_scheme(self, xkkh, schemeid):
        scheme_info = {}
        keyname = courseEvaluatePrefix + '_' + schemeid
        schedule_info = {}
        if redisConn.exists(keyname):
            from common.convert import redisstr2list
            scheme_info = redisstr2list(redisConn.get(keyname))
        else:
            from logic.course_evaluate.CourseEvaluate import CourseEvaluateLogic
            cel = CourseEvaluateLogic()
            scheme_info, num, msg = cel.get_ce_fis_sis(schemeid)
        print(scheme_info)
        from logic.jwxt.Schedule import ScheduleLogic
        sl = ScheduleLogic()
        print(xkkh)
        result, num, msg = sl.get_schedule_by_xkkh(xkkh)
        print(result)
        if len(result) > 0:
            weeks = self.get_weeks_from_kcb(result)
            # print(weeks)
            week_schedule = self.get_week_kcb(weeks, result)
            schedule_info = {'all': result, 'weeks': week_schedule}
        return {'scheme_info': scheme_info, 'schedule': schedule_info}

    def get_weeks_from_kcb(self, kcbs: list):
        weeks = []

        for kcb in kcbs:
            qssj = int(kcb.get('qssj'))
            jssj = int(kcb.get('jssj'))
            dsz = kcb.get('dsz')

            for week in range(qssj, jssj + 1):
                if dsz == '单':
                    if (week % 2) != 0 and week not in weeks:
                        weeks.append(week)
                elif dsz == '双':
                    if (week % 2) == 0 and week not in weeks:
                        weeks.append(week)
                else:
                    if week not in weeks:
                        weeks.append(week)
        return weeks

    def get_week_kcb(self, weeks: list, kcbs: list):
        kcbschedule = []
        for week in weeks:
            schedules = []
            for kcb in kcbs:
                qssj = int(kcb.get('qssj'))
                jssj = int(kcb.get('jssj'))
                if week >= qssj and week <= jssj:
                    schedules.append(kcb)
            kcbschedule.append({'week': week, 'schedules': schedules})

        return kcbschedule
