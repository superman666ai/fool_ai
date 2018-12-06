#!/usr/bin/python
# -*- coding:utf-8 -*-
from __future__ import unicode_literals

class Config(object):
    """
        配置文件类
    """
    CONFIG_NAME = "conf_offline"

    """---------------mongo数据库------------------"""
    # 1
    MONGO_HOST_ASTOCK =             "192.168.0.80"
    MONGO_PORT_ASTOCK =             27017
    MONGO_DB_ASTOCK =               "db_astock_day"
    # 测试db
    MONGO_DB_CHOOSE =                 "db_jian"
    TB_STOCK_DAY =                  "tb_stock_day"
    TB_STOCK_INFO =                 "tb_stock_info"
    TB_CHOOSE_TASK =                "tb_choose_task"
    TB_DAY_INFO =                    "tb_day_info"
    TB_NEW_STOCK_INFO =                  "tb_stock_info"

    # db_astock_day
    DB_ASTOCK_DAY =                  "db_astock_day"



    """---------------redis-----------------------"""

    REDIS_BROKER =                   'redis://127.0.0.1:6379/6'
    REDIS_BACKEND =                  'redis://localhost'

