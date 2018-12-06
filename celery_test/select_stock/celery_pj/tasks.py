# -*- coding: utf-8 -*-

# @Time    : 2018/9/6 15:15
# @Author  : jin
# @File    : tasks.py
from __future__ import absolute_import, unicode_literals
from bson.objectid import ObjectId
from celery_pj.celery_start import app
from methods.mixmethod import MixMethod
from utils.wt_utils_sqlconn import DB_CHOOSE
from config import Config
from operator import methodcaller
import time


@app.task
def trans_info(id):
    """
    根据id 查询选股参数
    :param id:
    :return:
    """
    try:
        # 查询任务参数
        tb_choose_task = DB_CHOOSE.get_collection(Config.TB_CHOOSE_TASK)
        data = tb_choose_task.find_one({"_id": ObjectId(id)})
        if data != None:
            print u"开始任务{}".format(id)
            param = data.get("param")
            # 实例化类
            obj = MixMethod()
            # 调用类的业务
            for i in param:
                para = i[1: ]
                list = methodcaller(i[0], *para)(obj)
            # 将数据存库
            obj.db_insert_result(id=id)
            print u"任务结束{}".format(id)
    except Exception as e:
        print u"任务出错{}".format(e)
    return
