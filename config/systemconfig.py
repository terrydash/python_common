from config.const.redisPrefix import sysconfigPrefix
from db.RedisConn import redisConn
from model.logic.Config import Config
from repository.BaseRepository import BaseRepository

sys_config_list = [
    {'name': '当前学年', 'dbname': 'actyear'},
    {'name': '每页个数', 'dbname': 'pagesize'},
    {'name': '学年', 'dbname': 'xn'},
    {'name': '学期', 'dbname': 'xq'},
    {'name': '课程表是否从教务系统读取', 'dbname': 'kcb_from_oracle'},
    {'name': '督导排序教师是否开放', 'dbname': 'can_supervision_sort_teacher'},
    {'name': '督导排序教师时A的最大比例', 'dbname': 'sortteacher_max_a'},
    {'name': '系统更新日志', 'dbname': 'commitlog'},
    {'name': '学年信息', 'dbname': 'actyears'},
    {'name': '许可序列号', 'dbname': 'activecode'},

]
sys_config = {}


def init():
    br = BaseRepository(entity=Config)
    for config in sys_config_list:
        if 'dbname' in config.keys():
            dbkey = config.get('dbname')
            result, _num, _msg = br.search_no_page({'name': dbkey}, None)
            if result is not None and len(result) > 0:
                config['value'] = result[0].get('value')
                config['id'] = result[0].get('_id')
                sys_config[config.get('dbname')] = config
                redisConn.set(sysconfigPrefix + dbkey, config['value'])
                # print(sys_config)


xn = ''
xq = ''
actyear = ''
kcb_from_oracle = ''
can_supervision_sort_teacher = ''
sortteacher_max_a = ''
commitlog = ''
actyears = ''
activecode = ''


def get_config(keyname: str):
    if redisConn.exists(sysconfigPrefix + keyname):
        return redisConn.get(sysconfigPrefix + keyname)
    init()
    if keyname in sys_config:
        configdict: dict = sys_config.get(keyname)
        if 'value' in configdict:
            return configdict.get('value')
    return None


def get_allconfig():
    init()
    return sys_config
