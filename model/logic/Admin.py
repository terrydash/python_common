# -*-coding:utf-8-*-
from model.base.MongoDBEntity import MongoDBEntity


class Admin(MongoDBEntity):
    username = ''
    truename = ''
    mm = ''
    bm = ''
    powers = []
    token = ''
