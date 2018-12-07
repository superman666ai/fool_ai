#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2018/4/13 13:25
# @Author  : XieTianshun
# @Site    : 
# @File    : load_data_base.py
# @Software: PyCharm

""" 加载数据 基类 """

# sys lib

# tp lib
import pandas as pd
import pymongo
from libwt.base.wt_error_message import WtErrorMessage
from utils.macf import Macf

# proj lib
from utils.mongo_singleton import MongoSingleton
from cal_fq import cal_jl_fq, cal_ft_fq


class LoadDataBase(WtErrorMessage):
    """ """

    def __init__(self):
        WtErrorMessage.__init__(self)

        self.param = None
        self.data = pd.DataFrame()
        self.sort_key = 'date'


    def set_param(self, param):
        """
        加载 参数 信息
        :param param:
        :return:
        """

        self.param = param


    def set_sort_key(self, key):
        """

        :param key:
        :return:
        """
        self.sort_key = key


    def check_param(self):
        """
        检查 参数
        :return:
        """


    def parse_param(self):
        """
        解析 参数
        :return:
        """
        df = self.param

        self.mk = df.loc[Macf.Market].get(Macf.Value)
        self.fq = df.loc[Macf.Frequency].get(Macf.Value)

        print 'load param ok !'


    def get_datb_by_param(self):
        """
        根据 参数 获取 mg 句柄

        '日线': 'day',
        '周线': 'week',
        '月线': 'month',
        '季线': 'quarter',
        '年线': 'year',
        '1分钟': 'm1',
        '5分钟': 'm5',
        '15分钟': 'm15',
        '30分钟': 'm30',
        '60分钟': 'm60',

        :return:
        """

        if self.fq in Macf.QS_STOCK_DAILY:
            self.set_sort_key('date')
        else:
            self.set_sort_key('time')

        self.qttb = MongoSingleton.get_mgtb(self.mk, self.fq)

        return self.qttb


    def get_fqtb_by_param(self):
        """
        获取 复权表 句柄
        :return:
        """

        self.fqtb = MongoSingleton.get_fqtb(self.mk)

        return self.fqtb


    def get_iftb_by_param(self):
        """

        :return:
        """

        self.iftb = MongoSingleton.get_iftb(self.mk)

        return self.fqtb


    def calculate_fq_data(self, qk, df):
        """
        计算 复权 数据
        :param df:
        :return:
        """

        if 'A' == self.mk:
            df_rst = cal_jl_fq(self.fqtb, self.sort_key, qk, df)
        elif self.mk in ['US', 'HK']:
            df_rst = cal_ft_fq(self.fqtb, self.sort_key, qk, df)
        else:
            df_rst = df

        return df_rst


    def transform_freq(self, df, f):
        """

        :param df:
        :return:
        """

        ohlc_dict = {
            'open': 'first',
            'high': 'max',
            'close': 'last',
            'low': 'min',
            'volume': 'sum',
            'amount': 'sum',

            # 日期后归档
            'date': 'last',
            # 'time': 'last',
            # 'year': 'last',

            'qk': 'first',
            'code': 'first'
        }

        df.index = pd.DatetimeIndex(df['date'].astype(str))

        xxx = df.resample(
            f,
            closed='left',
            label='left'
        ).agg(ohlc_dict).dropna(how='any')

        return xxx


    def trans_ktype(self):
        """

        :return:
        """

        return {
            Macf.QS_STOCK_FREQUENCY_WEEK: 'W',
            Macf.QS_STOCK_FREQUENCY_MONTH: 'BM',
            Macf.QS_STOCK_FREQUENCY_SEASON: 'BQ',
            Macf.QS_STOCK_FREQUENCY_YEAR: 'BA',
        }.get(self.fq)


    def get_fq_data_by_qk(self, qk):
        """
        根据 qk 获取 复权 数据
        :param qk:
        :return:
        """

        cur = self.qttb.find({Macf.Qk: qk}).sort(self.sort_key, pymongo.DESCENDING).limit(1000)

        df = pd.DataFrame(list(cur))
        if 0 == df.shape[0]:
            return df

        df.sort_values(self.sort_key, inplace=True)

        df = self.calculate_fq_data(qk, df)

        if self.fq in  [
            Macf.QS_STOCK_FREQUENCY_WEEK,
            Macf.QS_STOCK_FREQUENCY_MONTH,
            Macf.QS_STOCK_FREQUENCY_SEASON,
            Macf.QS_STOCK_FREQUENCY_YEAR,
        ]:

            ftp = self.trans_ktype()

            df = self.transform_freq(df, ftp)

        return df


    def get_stock_info(self):
        """

        :return:
        """

        cur = self.iftb.find({"type" : "stock"}, {'qk': 1, '_id': 0})

        df = pd.DataFrame(list(cur))

        df.set_index('qk', inplace=True)

        return df

