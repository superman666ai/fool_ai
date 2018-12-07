#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2018/6/12 14:05
# @Author  : XieTianshun
# @Site    : 
# @File    : config_offline.py
# @Software: PyCharm

""" file describe """

# sys lib

# tp lib

# proj lib
from config_comm import ConfigBase


class Config(ConfigBase):

    CELERY_REDIS = 'redis://192.168.0.60:6001/5'

    MONGO_HOST_CORE = '192.168.0.60'
    MONGO_PORT_CORE = 26000

    # Us-stock
    US_HOST = '192.168.0.60'
    US_PORT = 27000

    # India-stock
    In_HOST = '192.168.0.82'
    In_PORT = 27017

    # Au-stock
    AU_HOST = '192.168.0.82'
    AU_PORT = 27017

    # A-stock
    A_HOST = '192.168.0.60'
    A_PORT = 26000

    # HK-stock
    HK_HOST = '192.168.2.141'
    HK_PORT = 27017

