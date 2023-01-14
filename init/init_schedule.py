import time

import schedule

from init.init_logging import get_logger

logger = get_logger(__name__)


def start():
    from logic.jwxt.Schedule import ScheduleLogic
    sl = ScheduleLogic()
    schedule.every().day.do(sl.oracle2mongo)
    from logic.jwxt.Teacher import TeacherLogic
    tl = TeacherLogic()
    schedule.every().day.do(tl.oracle2mongo)
    from logic.jwxt.TeachTask import TeachTaskLogic
    ttl = TeachTaskLogic()
    schedule.every(7).days.do(ttl.oracle2mongo)
    logger.debug('定时任务已经启动')
    #print('定时任务已经启动')
    while True:
        schedule.run_pending()
        time.sleep(10)
