# -*- coding: utf-8 -*-

# @Time    : 2018/9/12 9:15
# @Author  : jin
# @File    : basemethod.py
from bson.objectid import ObjectId
import datetime
from utils.wt_utils_sqlconn import DB_ASTOCK, DB_CHOOSE
from config import Config
import pandas as pd
import numpy as np


class BaseMethod(object):
    def __init__(self):
        self.resp_data = None
        self.result = []
        self.init_resp_form()

    def init_resp_form(self):
        """
        初始化dataframe表格 包含code name exchcode 信息
        :return:
        """
        tb_stock_info = DB_ASTOCK.get_collection(Config.TB_STOCK_INFO)
        code = []
        name = []
        exchcode = []
        for i in tb_stock_info.find({"type": "stock"}):
            if i is not None:
                code.append(str(i.get("code")))
                name.append(i.get("name"))
                exchcode.append(str(i.get("exchcode")))

        data = {}
        data["code"] = code
        data["name"] = name
        data["exchcode"] = exchcode
        self.result = code
        self.resp_data = pd.DataFrame(data=data)

    def db_insert_result(self, id=None):
        """
        将数据插入db，更改状态为0
        0 为结束
        1 为正在进行
        :return:
        """
        qk = self.resp_data[self.resp_data['code'].isin(self.result)]
        tittle = list(qk.columns.values)
        body = np.array(qk).tolist()
        tb_stock_day = DB_CHOOSE.get_collection(Config.TB_CHOOSE_TASK)
        tb_stock_day.update_one({"_id": ObjectId(id)}, {"$set": {
            "status": 0,
            "tittle": tittle,
            "qk": body}})



class QueryIndividualShare(BaseMethod):

    def per_price_limit(self, code=None, date=None):
        """
         查询股票的某日涨跌幅
        :param code:
        :param date:
        :return:
        """
        date_now = int(datetime.datetime.now().strftime("%Y%m%d"))
        if date == None:
            date = date_now
        elif date == "fivedays":
            date = (datetime.datetime.now() - datetime.timedelta(days=5)).strftime("%Y%m%d")
        elif date == "tendays":
            date = (datetime.datetime.now() - datetime.timedelta(days=10)).strftime("%Y%m%d")
        else:
            return None

        tb_stock_day = DB_ASTOCK.get_collection(Config.TB_STOCK_DAY)
        # 获取当日收盘价格
        close = None
        n = 0
        while close is None:
            data = tb_stock_day.find_one({"date": date_now, "code": code})
            if data != None:
                close = float(data.get("close"))
            date_now -= 1
            n += 1
            if n == 10:
                print u"当日收盘价格错误，股票{}近10日没有数据".format(code)
                return None

        # 获取某日收盘价格
        someday_close = None
        n = 0
        while someday_close is None:
            data = tb_stock_day.find_one({"date": date, "code": code})
            if data != None:
                someday_close = float(data.get("close"))
            date -= 1
            n += 1
            if n == 10:
                print u"某日收盘价格错误，股票{}近10日没有数据".format(code)
                return None

        price_limit_rate = round((close - someday_close) / someday_close * 100, 2)
        return price_limit_rate

    def per_stock_amount(self, code=None, date=None):
        """
         查询股票的某日涨跌幅
        :param code:
        :param date:
        :return:
        """
        date_now = datetime.datetime.now().strftime("%Y%m%d")
        if date == None:
            date = date_now

        tb_stock_day = DB_ASTOCK.get_collection(Config.TB_STOCK_DAY)
        # 获取成交额
        data = tb_stock_day.find_one({"date": date, "code": code})
        if data != None:
            amount = float(data.get("amount"))
            return amount
        # print u"股票{}，{}没有成交额".format(code, date_now)
        return

    def per_across_dish(self, code=None, date=30, lte=15):
        try:

            # code = "000631"
            qk = "szse." + code
            tb_stock_day = DB_ASTOCK.get_collection(Config.TB_STOCK_DAY)

            for i in tb_stock_day.aggregate([{"$match": {"qk": qk}},
                                             {"$sort": {"date": -1}},
                                             {"$limit": date},
                                             {"$group":
                                                  {"_id": "$qk", "high": {"$max": "$high"}, "low": {"$min": "$low"}}}]):

                high = i.get("high")
                low = i.get("low")
                dish_rate = (high - low) / low * 100
                if dish_rate <= lte:
                    print dish_rate
                    return 1
            return 0

        except Exception as e:
            print e
