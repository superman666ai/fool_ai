# -*- coding: utf-8 -*-

# @Time    : 2018/9/20 9:30
# @Author  : jin
# @File    : task.py

from bson.objectid import ObjectId
import datetime
from utils.wt_utils_sqlconn import DB_ASTOCK, DB_CHOOSE, DB_ASTOCK_DAY
from config import Config
import pandas as pd
import numpy as np
from datetime import datetime
import tushare as ts
import json


class BaseTask(object):
    def __init__(self):
        self.resp_data = None
        self.init_form_data()

    def init_form_data(self):
        """
        初始化dataframe表格 包含stock 基本信息
        :return:
        """
        tb_stock_info = DB_ASTOCK.get_collection(Config.TB_STOCK_INFO)

        data = tb_stock_info.find({"type": "stock"},
                                  {"_id": 0, "type": 0, "listdate": 0, "stype": 0, "mtype": 0,
                                   "update_time": 0, "name": 0})
        self.resp_data = pd.DataFrame(data=list(data))

    def data_to_csv(self):
        """
        导出csv文件
        :return:
        """
        try:
            self.resp_data.to_csv("form_data.csv", encoding="utf-8")
            print u"导出csv成功"
        except Exception as e:
            print u"导出csv失败{}".format(e)


class OtherMethods(BaseTask):
    def __init__(self):
        BaseTask.__init__(self)

    def save_db_stock_info(self):
        """
       保存沪深上市公司基本面数据
        :return:
        """
        data = ts.get_stock_basics()
        data["code"] = data.index
        self.resp_data = pd.merge(left=self.resp_data, right=data, on=["code"])

        tb_new_stock_info = DB_CHOOSE.get_collection(Config.TB_NEW_STOCK_INFO)
        tb_new_stock_info.remove()
        tb_new_stock_info.insert(json.loads(self.resp_data.T.to_json()).values())
        return

    def rise_down(self, days=5):
        """
        近某日涨跌幅 涨跌比例=某日收盘价-当日收盘价/当日收盘价*100%
        :return:
        """
        try:
            new_list = []
            label_name = str(days) + "_rise_down"
            tb_stock_day = DB_ASTOCK_DAY.get_collection(Config.TB_STOCK_DAY)

            date = int(datetime.now().strftime("%Y%m%d"))
            for i in list(self.resp_data["qk"]):
                db_data = tb_stock_day.find({"qk": i, "date": {"$lte": date}},
                                            {"_id": 0}).sort([("date", -1)]).limit(days)
                data = pd.DataFrame(data=list(db_data))
                close = data[0:1]["close"].values
                before_close = data[-1:]["close"].values

                rate = round((close - before_close) / before_close * 100, 2)
                new_list.append(rate)

            # 添加新列
            self.resp_data[label_name] = new_list

        except Exception as e:
            print e

    def swing_dash(self, days=100):
        """
        近某日振幅
        :return:
        """
        try:
            new_list = []
            label_name = str(days) + "_swing"
            tb_stock_day = DB_ASTOCK_DAY.get_collection(Config.TB_STOCK_DAY)

            date = int(datetime.now().strftime("%Y%m%d"))
            for i in list(self.resp_data["qk"]):
                db_data = tb_stock_day.find({"qk": i, "date": {"$lte": date}},
                                            {"_id": 0}).sort([("date", -1)]).limit(days)
                data = pd.DataFrame(data=list(db_data))

                high = data["high"].max()
                low = data["low"].min()
                rate = round((high - low) / low * 100, 2)
                new_list.append(rate)

            # 添加新列
            self.resp_data[label_name] = new_list

        except Exception as e:
            print e

    def avg_price(self, days=365):
        """
        近某天平均价
        :return:
        """
        try:
            new_list = []
            label_name = str(days) + "_price_avg"
            tb_stock_day = DB_ASTOCK_DAY.get_collection(Config.TB_STOCK_DAY)

            date = int(datetime.now().strftime("%Y%m%d"))
            for i in list(self.resp_data["qk"]):
                db_data = tb_stock_day.find({"qk": i, "date": {"$lte": date}},
                                            {"_id": 0}).sort([("date", -1)]).limit(days)
                data = pd.DataFrame(data=list(db_data))
                avg = round(data["avg"].mean(), 2)
                new_list.append(avg)

            # 添加新列
            self.resp_data[label_name] = new_list
            print self.resp_data

        except Exception as e:
            print e

    def get_his_data(self):
        """
        volume：成交量
        p_change：涨跌幅
        ma5：5日均价
        ma10：10日均价
        ma20:20日均价
        v_ma5:5日均量
        v_ma10:10日均量
        v_ma20:20日均量
        turnover:换手率
        :return:
        """
        try:
            tb_stock_day = DB_ASTOCK_DAY.get_collection(Config.TB_STOCK_DAY)
            date = datetime.now().strftime("%Y-%m-%d")
            date = "2018-09-28"
            data_list = []
            for i in list(self.resp_data["code"]):
                # 获取单支股票的历史行情
                data = ts.get_hist_data(i)
                data = data[data.index == date]
                data["code"] = i
                self.resp_data = self.resp_data.merge(data, on="code")
                print self.resp_data
                break

            #
            # print self.resp_data
            # 添加新列
            # self.resp_data[label_name] = new_list
            # print self.resp_data

        except Exception as e:
            print e

    def save_db_day_info(self):
        """
        保存日线数据
        :return:
        """
        try:
            tb_day_info = DB_CHOOSE.get_collection(Config.TB_DAY_INFO)
            tb_day_info.remove()
            for i in list(self.resp_data["code"]):
                # 获取单支股票的历史行情
                data = ts.get_hist_data(i)
                data["code"] = i
                data["date"] = data.index
                # print json.loads(data.T.to_json()).values()
                tb_day_info.insert(json.loads(data.T.to_json()).values())


                #
                # print self.resp_data
                # 添加新列
                # self.resp_data[label_name] = new_list
                # print self.resp_data

        except Exception as e:
            print e




if __name__ == "__main__":
    df =  ts.get_index()
    print df
    # a = OtherMethods()
    # 储存stock 信息
    # a.save_db_stock_info()
    # a.rise_down(5)
    # a.rise_down(10)
    # a.rise_down(15)
    # a.swing_dash()
    # a.avg_price()
    # a.data_to_csv()
    # a.save_db_day_info()
    # a.save_db_stock_info()
