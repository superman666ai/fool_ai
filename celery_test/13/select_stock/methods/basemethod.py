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
        self.init_resp_form()

    def init_resp_form(self):
        """
        初始化dataframe表格 包含code name exchcode 信息
        :return:
        """
        tb_stock_info = DB_ASTOCK.get_collection(Config.TB_STOCK_INFO)
        qk = []
        name = []

        for i in tb_stock_info.find({"type": "stock"}):
            if i is not None:
                qk.append(str(i.get("qk")))
                name.append(i.get("name"))

        data = {}
        data["qk"] = qk
        data["name"] = name
        self.result = qk
        self.all_stocks = qk
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

    def data_to_csv(self):
        self.resp_data.to_csv("form_data.csv", encoding="utf-8", index=False)


class QueryIndividualShare(BaseMethod):

    def per_rise_down(self, code, date=None):
        """
         查询股票的某日涨跌幅
        :param code:
        :param date:
        :return:
        """
        if date == None:
            date = 2
        try:
            tb_stock_day = DB_ASTOCK.get_collection(Config.TB_STOCK_DAY)
            # code = "000631"
            qk = "szse." + code
            stock_num = tb_stock_day.find({"qk": qk}).count()
            # 取不到两个交易日的数据就报错
            if stock_num < 2:
                return None
            data = tb_stock_day.aggregate([{"$match": {"qk": qk}},
                                             {"$sort": {"date": -1}},
                                             {"$limit": date},
                                             {"$group":
                                                  {"_id": "$qk",
                                                   "close": {"$push": "$close"},
                                                   "pclose": {"$push": "$pclose"}}}])
            for i in data:
                close = i.get("close")[0]
                before_close = i.get("close")[-1]
                rate = round(( close- before_close) / before_close * 100, 2)
            return rate

        except Exception as e:
            print "error---", e

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
