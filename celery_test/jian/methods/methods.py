# -*- coding: utf-8 -*-

# @Time    : 2018/8/31 11:46
# @Author  : jin
# @File    : methods.py
from bson.objectid import ObjectId
from utils.wt_utils_sqlconn import DB_ASTOCK, DB_CHOOSE
from config import Config
import pandas as pd
import numpy as np
from basemethod import QueryIndividualShare


class SelectMethods(QueryIndividualShare):
    """
    各类选股策略
    """
    def price_limit(self, date=None, gte=None, lte=None):
        """
        某日涨跌幅 涨跌比例=某日收盘价-当日收盘价/当日收盘价*100%
        :return:
        """
        new_list = []
        result = []
        for j in self.resp_data["code"]:
            data = self.per_price_limit(j, date=date)
            new_list.append(data)
            if gte <= data <= lte:
                result.append(j)

        if date == None:
            label_name = "today_price_limit"
        else:
            label_name = str(date) + "_price_limit"

        # 结果取交集
        self.result = [i for i in self.result if i in result]
        # 添加新列
        self.resp_data[label_name] = new_list

    def stock_amount(self, date=None, gte=None, lte=None):
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

    def across_dish(self, date=None, lte=15):
        """
        选出近某日横盘的股票
        :param date: 近多少日  例如20
        :return:
        """
        new_list = []
        result = []
        for j in self.resp_data["code"]:
            data = self.per_across_dish(code=j, date=date, lte=lte)

            new_list.append(data)
            if data == 1:
                result.append(j)

        if date == None:
            label_name = "30days_acrross"
        else:
            label_name = str(date) + "days_acrross"

        # 结果取交集
        print "eeeeeeeee", result
        self.result = [i for i in self.result if i in result]
        self.resp_data[label_name] = new_list


a = SelectMethods()
a.across_dish(date=100, lte=15)
print a.resp_data
print a.result

print len(a.result)


# a.across_dish_fun()
# a.price_limit(date=20180509)
# print a.resp_data
# a.insert_db()
# print a.resp_data.info()
