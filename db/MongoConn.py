#!/usr/bin/env python
# -*- coding:utf-8 -*-
from pymongo import MongoClient
from pymongo.errors import AutoReconnect
from retrying import retry

from config.startupconfig import init_config


def retry_if_auto_reconnect_error(exception):
    """Return True if we should retry (in this case when it's an AutoReconnect), False otherwise"""
    return isinstance(exception, AutoReconnect)


class MongoDB(object):

    def __init__(self):
        count = 0
        while True:
            self.conn = MongoClient(host=init_config.mongodb.ip, port=init_config.mongodb.port, connect=True,
                                    minPoolSize=0, maxPoolSize=200, connectTimeoutMS=400000, retryWrites=True,
                                    maxIdleTimeMS=10 * 60 * 1000)
            self.db = self.conn[init_config.mongodb.db]
            try:
                self.connecter = self.db.authenticate(init_config.mongodb.username, init_config.mongodb.password)
                self.conn.admin.command("ping")
            except Exception as e:
                count = count + 1
                self.connecter = False
                conn_result = str(e)
                print("连接失败,连接了", count, "次")
                if count >= 3:
                    break
            else:
                break


    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


@retry
def mongoconn():
    return MongoDB().db


mongodb = mongoconn()
