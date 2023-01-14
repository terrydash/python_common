import logging

from flask import Blueprint, request

from model.common.jsonModel import response_normal

mainbp = Blueprint('sortteacher', __name__)
logger = logging.getLogger(__name__)


@mainbp.route('/get', methods=["GET"])
def GetSortTeacher():
    values = request.values
    actyear = ''
    print(values.get('actyear'))
    if 'actyear' in values:
        actyear = values.get('actyear')
        if len(actyear) == 0:
            from logic.common.Config import ConfigLogic
            cl = ConfigLogic()
            actyear = cl.getCurrentActYear()
    else:
        from logic.common.Config import ConfigLogic
        cl = ConfigLogic()
        actyear = cl.getCurrentActYear()
    print(actyear)
    username = values.get('username', '')
    deptname = values.get('deptname', '')
    sort = values.get('sort', '+id')
    from logic.score.SortTeacher import SortTeacherLogic
    stl = SortTeacherLogic()
    result, num, msg = stl.get_all_sort_teacher(actyear=actyear, username=username, deptname=deptname, sort=sort)

    return response_normal(data=result, count=num, msg=msg).to_json()
