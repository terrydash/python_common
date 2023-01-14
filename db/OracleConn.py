# coding=utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool,NullPool

from config.startupconfig import init_config


def getconn():
    username = init_config.oracle.username  # 用户名
    passwd = init_config.oracle.password  # 用户密码
    host = init_config.oracle.ip  # 用户密码
    port = init_config.oracle.port  # 用户密码
    sid = init_config.oracle.sid  # 用户密码
    db = create_engine(
        'oracle://' + username + ':' + passwd + '@' + host + ':' + str(port) + '/' + sid + '',poolclass=QueuePool,pool_size=100,pool_timeout=1000*60)
    conn = db.connect()
    return conn, db


dbConn, db = getconn()
DBSession = sessionmaker(bind=db)
