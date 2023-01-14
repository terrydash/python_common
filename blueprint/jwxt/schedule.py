from flask import Blueprint

from logic.jwxt.Schedule import ScheduleLogic
from model.common.jsonModel import response_normal, response_error

mainbp = Blueprint('schedule', __name__)


@mainbp.route('/get/<xkkh>', methods=["GET"])
def GetSchedule(xkkh):
    if len(xkkh) == 0 or xkkh is None:
        return response_error(msg='xkkh不能为空！').to_json()
    sl = ScheduleLogic()
    # print(xkkh)
    result, num, msg = sl.get_schedule_by_xkkh(xkkh)
    r = response_normal(data=result, count=num, msg=msg)
    return r.to_json()
