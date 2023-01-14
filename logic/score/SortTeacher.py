import datetime
import re

from logic.Base import BaseLogic


class SortTeacherLogic(BaseLogic):
    def __init__(self):
        from logic.common.Cache import CacheLogic
        self.cache = CacheLogic()
        self.collectionName = "sortteacher"
        from repository.BaseRepository import BaseRepository
        self.baseRepository = BaseRepository(collectionname=self.collectionName)

    def get_one_by_userid_and_actyear(self, userid: str, actyear: str):
        query = {'userid': userid, 'actyear': actyear}
        result, num, msg = self.search_no_page(query=query)
        if result is not None:
            if len(result) > 0:
                return result[0]
        return None

    def checksortlist(self, sortlists: list, userinfo: dict):
        from logic.score.Score import ScoreLogic
        from logic.common.Config import ConfigLogic
        from logic.jwxt.Teacher import TeacherLogic
        tl = TeacherLogic()
        cl = ConfigLogic()
        sl = ScoreLogic()
        supervisonid: str = userinfo.get('id')
        actyear = cl.getCurrentActYear()
        haserror = False
        err_msg = ''
        max_a = round(float(cl.getMAX_A()), 2)
        a_num = 0
        b_plus_num = 0
        b_num = 0
        b_reduce_num = 0
        c_num = 0
        total_num = len(sortlists)
        teachers = list()
        for sortlist in sortlists:
            zgh = str(sortlist.get('zgh')).strip()
            print(zgh)
            #print(len(zgh))
            query = {'jszgh': zgh, 'actyear': actyear, 'score_user_info.id': supervisonid}
            # 检查教师是否在数据库中存在， 检查督导是否评价过该教师
            result, num, msg = sl.search_no_page(query=query)
            teacher, num, msg = tl.get_by_zgh(zgh=zgh)
            print(len(result))
            if len(result) == 0:
                haserror = True
                if teacher is not None:
                    err_msg += '您未对教师' + zgh + teacher.get('name') + '进行过听课评价，无法对其进行排序 '
                else:
                    err_msg += '职工号:' + zgh + '不存在'
            # 检查是否符合系统比例设定
            teacher['sortorder'] = sortlist['sort']
            sortorder = str(sortlist['sort']).strip().upper()
            if sortorder == 'A':
                a_num += 1
                teacher['result'] = 5
            elif sortorder == 'B+':
                b_plus_num += 1
                teacher['result'] = 4
            elif sortorder == 'B':
                b_num += 1
                teacher['result'] = 3
            elif sortorder == 'B-':
                b_reduce_num += 1
                teacher['result'] = 2
            elif sortorder == 'C':
                c_num += 1
                teacher['result'] = 1
            else:
                haserror = True
                err_msg += '职工号为:' + sortlist.get('zgh') + '的排序符号 ' + sortlist.get('sort') + ' 不正确！'
            teacher['id'] = teacher['_id']
            teacher.pop('_id')
            teacher.pop('mm')
            teachers.append(teacher)
        if a_num < 1 or b_plus_num < 1 or b_num < 1 or b_reduce_num < 1 or c_num < 1:
            haserror = True
            err_msg += '每个等级都至少分配一个人'
        current_max_a = round(float(a_num / total_num), 2)
        if round(float(a_num / total_num), 2) * 100 > max_a * 100:
            haserror = True
            err_msg += '排序A的比例大于设定值，当前A的比例：' + str(current_max_a * 100) + '%,设定值为' + str(max_a * 100) + '%。'
        if haserror:
            return False, err_msg, None
        return True, '', teachers

    def insert_sort_teacher(self, sortlists: list, userinfo: dict, zongjie: str):

        if len(sortlists) == 0:
            return False, 0, '排序名单不能为空！'
        result, msg, teachers = self.checksortlist(sortlists, userinfo)

        if result:
            from logic.common.Config import ConfigLogic
            cl = ConfigLogic()
            actyear = cl.getCurrentActYear()
            userinfo['commit_date'] = str(datetime.date.today())
            userinfo['teachers'] = teachers
            userinfo['actyear'] = actyear
            userid = userinfo['id']
            userinfo['userid'] = userid
            userinfo.pop('id')
            userinfo['zongjie'] = zongjie
            self.baseRepository.delete_all({'userid': userid, 'actyear': actyear})
            self.baseRepository.insert_one(userinfo)
            return True, 0, '提交成功'
        else:
            return False, 0, msg

    def get_all_sort_teacher(self, actyear: str, username: str, deptname: str, sort: str):
        from logic.user.supervision import SupervisionLogic
        svl = SupervisionLogic()
        sps = list()
        query = dict()

        if len(username) > 0:
            query['name'] = re.compile(username)
        if len(deptname) > 0:
            query['bm'] = re.compile(deptname)

        supversions, num, msg = svl.search_no_page(query=query, sort=sort)
        for supversion in supversions:
            id = supversion.get('_id')
            sortteacher = self.get_one_by_userid_and_actyear(userid=str(id), actyear=actyear)
            print(sortteacher)
            if sortteacher is not None:
                sortteacher['isfinish'] = True
                sps.insert(0, sortteacher)
            else:
                supversion.pop('mm')
                supversion['id'] = str(supversion['_id'])
                supversion.pop('_id')
                supversion.pop('token')
                supversion['isfinish'] = False
                sps.append(supversion)
        print(sps)
        return sps, len(sps), '正常'
