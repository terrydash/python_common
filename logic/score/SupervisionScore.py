import re

from init.init_logging import get_logger

logger = get_logger(__name__)


class SupervisionScoreLogic:
    def __init__(self):
        from logic.common.Cache import CacheLogic
        self.cache = CacheLogic()
        from model.logic.Score import Score
        self.collectionName = str(Score().COLLECTION_NAME)
        from repository.BaseRepository import BaseRepository
        self.baseRepository = BaseRepository(collectionname=self.collectionName)

    def getSortList(self, userinfo: dict, sort: str, teacher_name: str, dept: str,
                    actyear: str):
        query = {'score_user_info.id': userinfo.get('id'), 'actyear': actyear, 'status': 'normal'}
        logger.debug(query)
        logger.debug(userinfo)
        if int(userinfo.get('roleid')) == 2:
            if teacher_name is not None and len(teacher_name) > 0:
                query['jsxm'] = re.compile(teacher_name)
            if dept is not None and len(dept) > 0:
                query['kkxy'] = dept
        else:
            return None, 0, '只有督导才能使用本功能'

        scoreresult, num, msg = self.baseRepository.search_no_page(query=query, sort=sort)

        teachers = []
        from logic.jwxt.Teacher import TeacherLogic
        tl = TeacherLogic()

        for score in scoreresult:
            findit = False
            for t in teachers:
                if str(t.get('zgh')) == str(score.get('jszgh')):
                    findit = True
            if findit == False:
                result, num, msg = tl.get_by_zgh(str(score.get('jszgh')).strip())
                if result is not None:
                    if 'mm' in result.keys():
                        result.pop('mm')
                    result['sortorder'] = ''
                    teachers.append(result)
        from config.const.configConst import SORT_MAX_A
        from config.systemconfig import get_config
        rules = {str(SORT_MAX_A): get_config(SORT_MAX_A)}
        from model.common.jsonModel import response_normal
        print(response_normal(data=teachers).to_json())
        sortlist = {'scorelist': scoreresult, 'teacherlist': teachers, 'rules': rules}
        return sortlist, len(teachers), '正常'
