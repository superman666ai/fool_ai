#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2018/3/30 11:34
# @Author  : XieTianshun
# @Site    : 
# @File    : boll_bands_1.py
# @Software: PyCharm

""" boll 策略 1

    今天碰上轨 - 肯定是

    今天没碰上轨 -
        1、找最后一次上穿的 index
        2、在从该 index 往后 找 有没有 low < 中轨的

    1- 先找 最后的 上涨趋势(最新贴上轨的K线 index)

    2- 在上涨趋势中 不碰其他轨的股票

    成交额(amount) > 1000w

"""

# sys lib

# tp lib
from base.choose_base import ChooseBase
from base.load_data_base import LoadDataBase
from technical_indicator.boll_bands import cal_boll_band
from utils.macf import Macf


class BollBandOne(ChooseBase):
    """

    """

    def __init__(self):
        ChooseBase.__init__(self)


    def parse_param(self):
        """
        处理 参数
        :return:
        """

        self.window = int(self.param.loc['period'].get('default'))
        self.numsd = float(self.param.loc['numsd'].get('default'))
        self.amount = float(self.param.loc['amount'].get('default')) * 10000

        fq = self.param.loc[Macf.Frequency].get(Macf.Value)

        if fq in Macf.QS_STOCK_DAILY:
            self.set_sort_key('date')
        else:
            self.set_sort_key('time')


    def is_valid(self, df):
        """
        碰上轨属于上涨趋势，
        后续碰就不属于上涨趋势

        :param df:
        :return:
        """

        # 取出 最后 1 个数据
        ldata = df.iloc[-1].to_dict()

        # 过滤 成交额 小的 股票
        amount = ldata.get('at5', None)
        if amount is not None:
            if amount < self.amount:
                return False

        high = ldata.get('high')
        top = ldata.get('top')

        if high >= top:
            # 上穿 肯定是
            return True
        else:
            # 找最后一次 穿 中轨的

            # 碰中轨
            pzg = (df['low'] < df['mid']) & (df['high'] > df['mid'])
            # 中轨之下
            zgx = df['high'] <= df['mid']

            xx = df[pzg | zgx]

            if 0 == xx.shape[0]:
                return False

            # 取最后1个非上涨
            ldt = xx.iloc[-1].get(self.sort_key)

            df_tmp = df[df[self.sort_key] >= ldt]

            df_rst = df_tmp[df_tmp['high'] >= df_tmp['top']]

            if 0 < df_rst.shape[0]:
                return True
            else:
                return False


    def cal_ma_amount(self, df):
        """

        :param df:
        :return:
        """

        if 'amount' not in df.columns:
            return df

        # 求均值
        df['at5'] = df['amount'].rolling(5).mean()

        return df


    def filtrate_stock(self):
        """
        筛选股票
        :param qk:
        :return:
        """

        qk_list = self.ld.get_stock_info()

        # 提取 用户 参数
        for qk in qk_list.index:

            df = self.ld.get_fq_data_by_qk(qk)

            if 0 == df.shape[0]:
                print '数据为 NULL！'
                continue

            # 获取包含 布林线的 结果集
            bb_df = cal_boll_band(df, self.window, self.numsd)

            df_xl = self.cal_ma_amount(bb_df)

            rst = self.is_valid(df_xl)

            if rst is True:
                print qk, rst
                self.ok_qk.append(qk)


def run_script(tid):
    """

    :return:
    """
    go = BollBandOne()
    go.set_tid(tid)
    go.set_load_data(LoadDataBase)
    go.run()

