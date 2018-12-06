#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2018/4/13 11:10
# @Author  : XieTianshun
# @Site    : 
# @File    : macf.py
# @Software: PyCharm

""" file describe """

# sys lib

# tp lib

# proj lib


class Macf:
    """ """

    Code = 'code'
    Value = 'default'

    Market = 'market'
    Frequency = 'freq'

    StatusRun = 'run'
    StatusDone = 'done'
    StatusErr = 'error'
    StatusTest = 'test'

    TaskStatus = 'status'

    Qk= 'qk'

    # 分钟
    QS_STOCK_FREQUENCY_1 = 'm1'
    QS_STOCK_FREQUENCY_3 = 'm3'
    QS_STOCK_FREQUENCY_5 = 'm3'
    QS_STOCK_FREQUENCY_15 = 'm15'
    QS_STOCK_FREQUENCY_30 = 'm30'
    QS_STOCK_FREQUENCY_60 = 'm60'

    QS_STOCK_FREQUENCY_DAY = 'day'
    QS_STOCK_FREQUENCY_WEEK = 'week'
    QS_STOCK_FREQUENCY_MONTH = 'month'
    QS_STOCK_FREQUENCY_SEASON = 'quarter'
    QS_STOCK_FREQUENCY_YEAR = 'year'

    QS_STOCK_DAILY = [
        QS_STOCK_FREQUENCY_DAY,
        QS_STOCK_FREQUENCY_WEEK,
        QS_STOCK_FREQUENCY_MONTH,
        QS_STOCK_FREQUENCY_SEASON,
        QS_STOCK_FREQUENCY_YEAR
    ]

    QS_STOCK_MINS = [

        QS_STOCK_FREQUENCY_1,
        QS_STOCK_FREQUENCY_3,
        QS_STOCK_FREQUENCY_5,
        QS_STOCK_FREQUENCY_15,
        QS_STOCK_FREQUENCY_30,
        QS_STOCK_FREQUENCY_60,
    ]


    @classmethod
    def get_mgtb(cls, mk, fq):
        """

        :param mk:
        :param freq:
        :return:
        """

        # 根据 频率 分流 选择 数据库
        if fq in cls.QS_STOCK_DAILY:

            Macf.get_daily_db_tb(mk, fq)

        else:

            print 'ok'




    @classmethod
    def get_daily_db_tb(cls, mk, freq):
        """

        :param mk:
        :param freq:
        :return:
        """


    @classmethod
    def get_mins_db_tb(cls, mk, freq):
        """

        :param mk:
        :param freq:
        :return:
        """





