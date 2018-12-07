# -*- coding: utf-8 -*-

# @Time    : 2018/8/31 11:46
# @Author  : jin
# @File    : methods.py
from bson.objectid import ObjectId
from utils.wt_utils_sqlconn import DB_ASTOCK, DB_CHOOSE
from config import Config
import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta
from basemethod import QueryIndividualShare


class PriceStrategy(QueryIndividualShare):
    """
    价格类选股策略
    """

    def fun_price_strategy_rise_down(self, date=None, gte=-5, lte=5):
        """
        涨跌幅 涨跌比例=某日收盘价-当日收盘价/当日收盘价*100%
        :param date: 前几日  eg: 10， 前十日的涨跌幅
        :param gte:
        :param lte:
        :return:
        """
        new_list = []
        result = []
        # 循环查询股票
        for j in self.all_stocks:
            data = self.per_rise_down(j, date=date)
            new_list.append(data)
            if data == None:
                pass
            elif gte <= data <= lte:
                result.append(j)

        # 构建新列名
        if date == None:
            label_name = "today_rise_down"
        else:
            label_name = str(date) + "_rise_down"

        # 结果取交集
        self.result = [i for i in self.result if i in result]
        # 添加新列
        self.resp_data[label_name] = new_list

    def fun_price_strategy_deal_amount(self, date=None, gte=None, lte=None):
        """
        某日成交额
        :param begin:
        :param end:
        :return:
        """
        new_list = []
        result = []
        for j in self.resp_data["code"]:
            data = self.per_stock_amount(code=j, date=date)
            new_list.append(data)
            if gte <= data <= lte:
                result.append(j)
        if date == None:
            label_name = "today_amount"
        else:
            label_name = str(date) + "amount"
        print "----++++{}".format(label_name)
        # 结果取交集
        self.result = [i for i in self.result if i in result]

        self.resp_data[label_name] = new_list

    def fun_price_strategy_across_dish(self, date=100, lte=15):
        """
         选出近日横盘的股票
        :param date:  近多少天 eg， 100  近100天
        :param lte:  振幅小于多少
        :return:
        """
        print "1111start------{}".format(datetime.now())
        new_list = []
        result = []
        # 循环查询股票
        for j in self.all_stocks:
            data = self.per_across_dish(code=j, date=date, lte=lte)
            new_list.append(data)
            if data == 1:
                result.append(j)

        # 构建新列名
        label_name = str(date) + "days_is_dish"
        # 结果取交集
        self.result = [i for i in self.result if i in result]
        # 添加新列
        self.resp_data[label_name] = new_list
        print "1111end------{}".format(datetime.now())

    def fun_price_strategr_rise_down2(self, date=None, gte=-5, lte=5):
        pass

    def fun_price_strategy_across_dish2(self, date=100, lte=15):
        """
         选出近日横盘的股票
        :param date:  近多少天 eg， 100  近100天
        :param lte:  振幅小于多少
        :return:
        """
        date = 130
        tb_stock_day = DB_ASTOCK.get_collection(Config.TB_STOCK_DAY)
        print "start------{}".format(datetime.now())
        new_list = []
        result = []
        # 查询100天内所有股票的数据
        end_date = int(datetime.now().strftime("%Y%m%d"))
        start_date = int((datetime.now() - timedelta(days=date)).strftime("%Y%m%d"))
        # # 构建新列名
        label_name = str(date) + "days_is_dish"

        # data = tb_stock_day.find({"date": {"$gte": start_date, "$lte": end_date}},
        #                          {"qk": 1, "high": 1, "low": 1, "_id": 0})
        data = tb_stock_day.aggregate([{"$match": {"date": {"$gte": start_date, "$lte": end_date}}},
                                         {"$group":
                                              {"_id": "$qk", "high": {"$max": "$high"}, "low": {"$min": "$low"}}}])

        data = pd.DataFrame(list(data))
        data.eval("{}=(high - low) / low * 100".format(label_name), inplace=True)
        # data.drop_duplicates(subset="qk", keep="first", inplace=True)
        print data

# a.across_dish_fun()
# a.price_limit(date=20180509)
# print a.resp_data
# a.insert_db()
# print a.resp_data.info()
