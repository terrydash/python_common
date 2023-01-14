import logging

from flask import Blueprint, request

from common.decorator import need_power
from logic.score.DeptScore import DeptScoreLogic
from logic.score.Score import ScoreLogic
from model.common.Common import RoleType
from model.common.jsonModel import response_normal, response_error, response_notlogin

mainbp = Blueprint('score', __name__)
logger = logging.getLogger(__name__)


@mainbp.route('/get/<id>', methods=["GET"])
def GetOne(id):
    if len(id) == 0 or id is None:
        return response_error(msg='id不能为空！').to_json()
    from logic.common.Login import GetUserInfoFromToken
    result, userinfo = GetUserInfoFromToken()
    tl = ScoreLogic()
    result, num, msg = tl.get_by_id_check_role(_id=id, userinfo=userinfo)
    r = response_normal(data=result, count=num, msg=msg)
    return r.to_json()


@mainbp.route('/delete', methods=["POST"])
def DeleteCS():
    from logic.common.Login import GetUserInfoFromToken
    result, userinfo = GetUserInfoFromToken()
    requestjson = request.json
    if result:
        _id = requestjson.get('id')
        if len(_id) == 0 or _id is None:
            return response_error(msg='id不能为空！').to_json()
        fi = ScoreLogic()
        logger.info(response_normal(requestjson).to_json())
        result, num, msg = fi.delete_by_id(_id, userinfo)
        if result is None:
            return response_error(msg=msg).to_json()
        r = response_normal(data=result, count=num, msg=msg)
        return r.to_json()
    return response_notlogin().to_json()


@mainbp.route('/getinfo')
def getinfo():
    xkkh = ''
    schemeid = ''
    if 'xkkh' in request.values:
        xkkh = str(request.values.get('xkkh'))
    if 'schemeid' in request.values:
        schemeid = str(request.values.get('schemeid'))
    if len(xkkh) == 0 or len(schemeid) == 0:
        return response_error(msg='参数错误!').to_json()
    from logic.score.Score import ScoreLogic
    sl = ScoreLogic()
    result = sl.get_course_info_and_scheme(xkkh=xkkh, schemeid=schemeid)
    return response_normal(data=result).to_json()


@mainbp.route('/teacherreply', methods=["POST"])
def teacherreply():
    requestjson: dict = request.json
    logger.info(response_normal(requestjson).to_json())
    print(requestjson)
    if 'id' in requestjson.keys() and 'content' in requestjson.keys():
        id = str(requestjson.get('id')).strip()
        content = str(requestjson.get('content')).strip()
        if len(content) == 0:
            return response_error(msg='回复内容不能为空！').to_json()
        from logic.score.TeacherScore import TeacherScoreLogic
        tsl = TeacherScoreLogic()
        result, num, msg = tsl.teacher_reply(id, content)
        if result is not None:
            return response_normal(data=result).to_json()
        else:
            return response_error(msg=msg).to_json()
    else:
        return response_error(msg='参数不正确!').to_json()
    return response_error(data=requestjson).to_json()


@mainbp.route('/deptreply', methods=["POST"])
def deptreply():
    requestjson: dict = request.json
    logger.info(response_normal(requestjson).to_json())
    print(requestjson)
    if 'id' in requestjson.keys() and 'content' in requestjson.keys():
        id = str(requestjson.get('id')).strip()
        content = str(requestjson.get('content')).strip()
        if len(content) == 0:
            return response_error(msg='回复内容不能为空！').to_json()
        tsl = DeptScoreLogic()
        result, num, msg = tsl.dept_reply(id, content)
        if result is not None:
            return response_normal(data=result).to_json()
        else:
            return response_error(msg=msg).to_json()
    else:
        return response_error(msg='参数不正确!').to_json()
    return response_error(data=requestjson).to_json()


@mainbp.route('/judgesupervision', methods=["POST"])
def udgesupervision():
    requestjson: dict = request.json
    logger.info(response_normal(requestjson).to_json())
    print(requestjson)
    if 'id' in requestjson.keys() and 'result' in requestjson.keys():
        id = str(requestjson.get('id')).strip()
        judge_result = str(requestjson.get('result')).strip()
        if len(judge_result) == 0:
            return response_error(msg='评价选项不能为空！').to_json()
        from logic.score.TeacherScore import TeacherScoreLogic
        tsl = TeacherScoreLogic()
        result, num, msg = tsl.judge_supervision(id, judge_result)
        if result is not None:
            return response_normal(data=result).to_json()
        else:
            return response_error(msg=msg).to_json()
    else:
        return response_error(msg='参数不正确!').to_json()
    return response_error(data=requestjson).to_json()


@mainbp.route('/insert', methods=["POST"])
def insert():
    requestjson = request.json
    logger.info(response_normal(requestjson).to_json())
    if 'score' in requestjson:
        model = dict(requestjson.get('score'))
        sl = ScoreLogic()
        result, num, msg = sl.check_model(model)
        if result:
            result, num, msg = sl.insert_v2(model)
            if result:
                return response_normal(count=num, msg=msg).to_json()
            return response_error(msg=msg).to_json()
        else:
            return response_error(msg=msg).to_json()
    else:
        return response_error(msg='参数不正确!').to_json()
    return response_error(data=requestjson).to_json()


@mainbp.route('/insertv2', methods=["POST"])
def insertv2():
    requestjson = request.json
    logger.info(response_normal(requestjson).to_json())
    if 'score' in requestjson:
        model = dict(requestjson.get('score'))
        sl = ScoreLogic()
        result, num, msg = sl.check_model(model)
        if result:
            result, num, msg = sl.insert(model)
            if result:
                return response_normal(count=num, msg=msg).to_json()
            return response_error(msg=msg).to_json()
        else:
            return response_error(msg=msg).to_json()
    else:
        return response_error(msg='参数不正确!').to_json()
    return response_error(data=requestjson).to_json()


@mainbp.route('/getforteacher', methods=["GET"])
def getforteacher():
    page = 1
    pagesize = 10

    sort = '+id'

    actyear = ''
    if 'page' in request.values:
        page = int(request.values.get('page'))

    if 'pagesize' in request.values:
        pagesize = int(request.values.get('pagesize'))
    if 'sort' in request.values:
        sort = request.values.get('sort')
    if 'actyear' in request.values:
        actyear = request.values.get('actyear')
    from logic.common.Login import GetUserInfoFromToken
    result, userinfo = GetUserInfoFromToken()
    if result:
        sl = ScoreLogic()
        result, num, msg = sl.get_with_userinfo_for_teacher_history(userinfo=userinfo, page=page, pagesize=pagesize,
                                                                    actyear=actyear, sort=sort)
        return response_normal(result, num, msg).to_json()
    return response_notlogin().to_json()


@mainbp.route('/get', methods=["GET"])
def get():
    page = 1
    pagesize = 10
    teacher_name = ''
    sort = '+id'
    dept = ''
    actyear = ''
    supervision_name = ''
    if 'page' in request.values:
        page = int(request.values.get('page'))
    if 'teacher_name' in request.values:
        teacher_name = request.values.get('teacher_name')
    if 'pagesize' in request.values:
        pagesize = int(request.values.get('pagesize'))
    if 'sort' in request.values:
        sort = request.values.get('sort')
    if 'dept' in request.values:
        dept = request.values.get('dept')
    if 'actyear' in request.values:
        actyear = request.values.get('actyear')
    if 'supervision_name' in request.values:
        supervision_name = str(request.values.get('supervision_name'))
    from logic.common.Login import GetUserInfoFromToken
    result, userinfo = GetUserInfoFromToken()
    print(userinfo)
    if result:
        sl = ScoreLogic()
        result, num, msg = sl.get_with_userinfo(userinfo, page, pagesize, sort, teacher_name, dept, actyear,
                                                supervision_name)
        return response_normal(result, num, msg).to_json()
    return response_notlogin().to_json()


@mainbp.route('/getexport', methods=["GET"])
def getexport():
    page = 1
    pagesize = 10
    teacher_name = ''
    sort = '+id'
    dept = ''
    actyear = ''
    if 'page' in request.values:
        page = int(request.values.get('page'))
    if 'name' in request.values:
        teacher_name = request.values.get('name')
    if 'pagesize' in request.values:
        pagesize = int(request.values.get('pagesize'))
    if 'sort' in request.values:
        sort = request.values.get('sort')
    if 'dept' in request.values:
        dept = request.values.get('dept')
    if 'actyear' in request.values:
        actyear = request.values.get('actyear')
    if 'schemeid' in request.values:
        schemeid = str(request.values.get('schemeid'))
    from logic.common.Login import GetUserInfoFromToken
    result, _ = GetUserInfoFromToken()
    if result:
        sl = ScoreLogic()
        result, num, msg = sl.get_export(page, pagesize, sort, teacher_name, dept, actyear, schemeid)
        return response_normal(result, num, msg).to_json()
    return response_notlogin().to_json()


@mainbp.route('/getsortlist', methods=["GET"])
def getsortlist():
    teacher_name = ''
    sort = '+id'
    dept = ''
    actyear = ''

    if 'teacher_name' in request.values:
        teacher_name = request.values.get('teacher_name')

    if 'sort' in request.values:
        sort = request.values.get('sort')
    if 'dept' in request.values:
        dept = request.values.get('dept')
    if 'actyear' in request.values:
        actyear = request.values.get('actyear')
    from logic.common.Login import GetUserInfoFromToken
    result, userinfo = GetUserInfoFromToken()
    if result:
        from logic.score.SupervisionScore import SupervisionScoreLogic
        sl = SupervisionScoreLogic()
        result, num, msg = sl.getSortList(userinfo=userinfo, sort=sort, teacher_name=teacher_name, dept=dept,
                                          actyear=actyear)
        return response_normal(result, num, msg).to_json()
    return response_notlogin().to_json()


@need_power(roles=[RoleType.Admin.value, RoleType.SuperVision])
@mainbp.route('/insertsortlist', methods=["POST"])
def insertsortlist():
    from logic.common.Login import GetUserInfoFromToken
    result, userinfo = GetUserInfoFromToken()
    from logic.common.Config import ConfigLogic
    cl = ConfigLogic()
    r = str(cl.getSortTeacherIsOpen()).strip()

    if r == "0":
        return response_error(msg='督导排序功能未开放!').to_json()

    if result:
        requestjson = request.json
        if 'sortlist' in requestjson and 'zongjie' in requestjson:
            sortlist = list(requestjson.get('sortlist'))
            zongjie = str(requestjson.get('zongjie'))
            from logic.score.SortTeacher import SortTeacherLogic
            stl = SortTeacherLogic()
            result, num, msg = stl.insert_sort_teacher(sortlist, userinfo, zongjie)
            if result:
                return response_normal(msg='提交成功').to_json()
            else:
                return response_error(msg=msg).to_json()
        else:
            return response_error(msg='参数不正确!').to_json()
        return response_error(data=requestjson).to_json()
    else:
        return response_notlogin().to_json()
