#!/usr/bin/python
# -*- coding:utf-8 -*-
from __future__ import unicode_literals
import pymongo
from config import Config


# 数据库连接
class SqlConn(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def mongo_conn(self):
        try:
            db_conn_mongo = pymongo.MongoClient(host=self.host, port=self.port)
        except Exception as e:
            print "MongoDB连接失败,e" % e
        else:
            return db_conn_mongo


# 连接db_core
db_core_conn = SqlConn(Config.MONGO_HOST_ASTOCK, Config.MONGO_PORT_ASTOCK)
mongo_core_conn = db_core_conn.mongo_conn()
DB_ASTOCK = mongo_core_conn.get_database(Config.MONGO_DB_ASTOCK)

# 连接db_jian
db_core_conn = SqlConn(Config.MONGO_HOST_ASTOCK, Config.MONGO_PORT_ASTOCK)
mongo_core_conn = db_core_conn.mongo_conn()
DB_CHOOSE = mongo_core_conn.get_database(Config.MONGO_DB_CHOOSE)
