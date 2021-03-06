#!/usr/bin/python
# -*- coding:utf-8 -*-


from __future__ import unicode_literals
import redis
import os


class Config(object):
    """
        配置文件类
    """
    CONFIG_NAME = "conf_online"

    """---------------核心数据库------------------"""
    # 核心数据库  MONGO
    MONGO_HOST_ASTOCK =             "192.168.0.80"
    MONGO_PORT_ASTOCK =             27017
    MONGO_DB_ASTOCK =               "db_astock_day"
    TB_STOCK_DAY =                  "tb_stock_day"
    TB_STOCK_INFO =                 "tb_stock_info"
    TB_CHOOSE_TASK =                "tb_choose_task"

    """---------------redis-----------------------"""

    REDIS_BROKER =                   'redis://127.0.0.1:6379/6'
    REDIS_BACKEND =                  'redis://localhost'

