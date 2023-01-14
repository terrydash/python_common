import datetime
import logging
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 获取上级目录的绝对路径
log_dir = BASE_DIR + '/logs/' + str(datetime.datetime.now().strftime('%Y-%m-%d')) + '.log'


def init_log():
    pass


def get_logger(classname: str = __name__):
    fh = logging.FileHandler(log_dir, encoding='utf-8')  # 创建一个文件流并设置编码utf8
    console = logging.StreamHandler()
    logger = logging.getLogger(classname)  # 获得一个logger对象，默认是root
    logger.setLevel(logging.DEBUG)  # 设置最低等级debug
    fm = logging.Formatter(fmt="%(asctime)s %(filename)s[line:%(lineno)d] %(message)s'",
                           datefmt='%Y-%m-%d %H:%M:%S')  # 设置日志格式
    fh.setFormatter(fm)
    console.setFormatter(fm)
    logger.addHandler(fh)  # 把文件流添加进来，流向写入到文件
    logger.addHandler(console)
    # 把文件流添加写入格式
    return logger
