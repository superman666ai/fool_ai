#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2018/5/16 17:10
# @Author  : XieTianshun
# @Site    : 
# @File    : test_celery.py
# @Software: PyCharm

""" file describe """

# sys lib
import sys
from bson import ObjectId

# tp lib
import pymongo

# proj lib
from config import Config
from utils.macf import Macf


def main():
    """

    :return:
    """
    if len(sys.argv) == 1:
        print '参数传送错误'

    # 从参数中 获取 tid
    tid = sys.argv[1]

    # 根据 task_id 加载 策略信息
    conn = pymongo.MongoClient(Config.MONGO_HOST_CORE, Config.MONGO_PORT_CORE)
    db = conn.get_database(Config.MONGO_DB_CORE)
    tb = db.get_collection(Config.MONGO_TB_CHOOSE_STOCK)

    otid = ObjectId(tid)
    search = {'_id': otid}
    motify = {
        Macf.TaskStatus: Macf.StatusDone,
        'qk': [Macf.StatusTest]
    }

    tb.update_one(search, {'$set': motify})


def run_script(tid):
    """

    :param tid:
    :return:
    """

    # 根据 task_id 加载 策略信息
    conn = pymongo.MongoClient(Config.MONGO_HOST_CORE, Config.MONGO_PORT_CORE)
    db = conn.get_database(Config.MONGO_DB_CORE)
    tb = db.get_collection(Config.MONGO_TB_CHOOSE_STOCK)

    otid = ObjectId(tid)
    search = {'_id': otid}
    motify = {
        Macf.TaskStatus: Macf.StatusDone,
        'qk': [Macf.StatusTest]
    }

    tb.update_one(search, {'$set': motify})


if __name__ == '__main__':
    main()

