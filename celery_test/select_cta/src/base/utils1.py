#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2018/3/30 11:46
# @Author  : XieTianshun
# @Site    : 
# @File    : utils1.py
# @Software: PyCharm

""" file describe """

# sys lib
import datetime
import time
from bson import ObjectId

# tp lib
import pymongo

# proj lib
from utils.macf import Macf
from config import Config


def load_task_info(tid):
    """
    加载 task info
    :return:
    """

    conn = pymongo.MongoClient(Config.MONGO_HOST_CORE, Config.MONGO_PORT_CORE)
    db = conn.get_database(Config.MONGO_DB_CORE)
    tb = db.get_collection(Config.MONGO_TB_CHOOSE_STOCK)

    otid = ObjectId(tid)
    search = {'_id': otid}
    motify = {Macf.TaskStatus: Macf.StatusRun}

    item = tb.find_one({'_id': otid})
    tb.update_one(search, {'$set': motify})

    return item


