#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2018/4/13 15:40
# @Author  : XieTianshun
# @Site    : 
# @File    : mongo_singleton.py
# @Software: PyCharm

""" file describe """

# sys lib
import datetime

# tp lib
import pandas as pd
import pymongo

# proj lib
from config import Config
from macf import Macf

class MongoSingleton:

    QUOTE_STOCK_MODE = 'tb_stock_{}'
    QUOTE_MINS_DB_MODE = 'db_{}stock_{}'

    QS_STOCK_DB_MPA = {
        'A': 'db_astock_day',
        'AU': 'db_austock',
        'IN': 'db_instock',
        'US': 'db_usstock_day',
        'HK': 'db_hkstock_day',
    }

    # 复权表 映射
    QS_STOCK_FQ_MPA = {
        'A': 'tb_ex_factor',
        # 'AU': 'db_austock',
        # 'IN': 'db_instock',
        'US': 'tb_ext_factor',
        'HK': 'tb_ext_factor',
    }

    # 用 映射 关系 来 结果 不同市场不同 表 和 db 的问题
    QS_STOCK_CONN_MAP = pd.DataFrame([
        {'mk': 'A', 'host': Config.A_HOST, 'port': Config.A_PORT, 'dydb': 'db_astock_day', 'day': 'tb_stock_day', 'info': 'tb_stock_info'},
        {'mk': 'AU', 'host': Config.AU_HOST, 'port': Config.AU_PORT, 'dydb': 'db_austock', 'day': 'tb_stock_day', 'info': 'tb_stock_info'},
        {'mk': 'IN', 'host': Config.In_HOST, 'port': Config.In_PORT, 'dydb': 'db_instock', 'day': 'tb_stock_day', 'info': 'tb_stock_info'},
        {'mk': 'US', 'host': Config.US_HOST, 'port': Config.US_PORT, 'dydb': 'db_usstock_day', 'day': 'tb_stock_day_ft', 'info': 'tb_stock_info_ex'},
        {'mk': 'HK', 'host': Config.HK_HOST, 'port': Config.HK_PORT, 'dydb': 'db_hkstock_day', 'day': 'tb_stock_day_ft', 'info': 'tb_stock_info_ex'},
    ])


    QS_STOCK_CONN_MAP.set_index('mk', inplace=True)


    @classmethod
    def get_mgtb(cls, mk, fq):
        """

        :param mk:
        :param fq:
        :return:
        """

        ip, port = cls.QS_STOCK_CONN_MAP.loc[mk, ['host', 'port']]

        conn = pymongo.MongoClient(ip, int(port))

        # 根据 频率 分流 选择 数据库
        if fq in Macf.QS_STOCK_DAILY:


            db, tb = cls.QS_STOCK_CONN_MAP.loc[mk, ['dydb', Macf.QS_STOCK_FREQUENCY_DAY]]

            return conn.get_database(db).get_collection(tb)

        else:
            ty = datetime.datetime.now().year
            db = cls.QUOTE_MINS_DB_MODE.format(mk, fq).lower()
            tb = cls.QUOTE_STOCK_MODE.format(ty)

            return conn.get_database(db).get_collection(tb)


    @classmethod
    def get_fqtb(cls, mk):
        """

        :param mk:
        :return:
        """

        if not cls.QS_STOCK_FQ_MPA.has_key(mk):
            return False

        ip, port = cls.QS_STOCK_CONN_MAP.loc[mk, ['host', 'port']]

        conn = pymongo.MongoClient(ip, int(port))

        db = cls.QS_STOCK_DB_MPA.get(mk)
        tb = cls.QS_STOCK_FQ_MPA.get(mk)

        return conn.get_database(db).get_collection(tb)


    @classmethod
    def get_iftb(cls, mk):
        """
        获取 stock info 表 信息
        :param mk:
        :return:
        """

        if not cls.QS_STOCK_FQ_MPA.has_key(mk):
            return False

        ip, port = cls.QS_STOCK_CONN_MAP.loc[mk, ['host', 'port']]

        conn = pymongo.MongoClient(ip, int(port))

        db, tb = cls.QS_STOCK_CONN_MAP.loc[mk, ['dydb', 'info']]

        # db = cls.QS_STOCK_DB_MPA.get(mk)
        # tb = cls.QS_STOCK_FQ_MPA.get(mk)

        return conn.get_database(db).get_collection(tb)
