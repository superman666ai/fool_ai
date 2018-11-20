# -*- coding: utf-8 -*-

# @Time    : 2018/11/20 11:35
# @Author  : jian
# @File    : september.py

import datetime
import pandas as pd
import numpy as np
import tushare as ts
from sklearn import linear_model
import matplotlib.pyplot as plt

token = "095bcdf3baef2f08104831abfe943e71c307d0f3f2deaa134a74df4b"
pro = ts.pro_api(token=token)
data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
code_list = list(data["symbol"])
# code_list = ["002147"]
rise = []
down = []
pre = []
num = 0
for code in code_list:
    try:
        date_end_str = datetime.datetime.now().strftime("%Y-%m-%d")
        date_end = datetime.datetime.strptime(date_end_str, "%Y-%m-%d")
        date_start = (date_end + datetime.timedelta(days=-10)).strftime("%Y-%m-%d")
        date_end = date_end.strftime("%Y-%m-%d")

        y_date_end_str = datetime.datetime.now().strftime("%Y-%m-%d")
        y_date_end_str = "2018-09-12"
        y_date_end = datetime.datetime.strptime(y_date_end_str, "%Y-%m-%d")
        y_date_start = (y_date_end + datetime.timedelta(days=-10)).strftime("%Y-%m-%d")
        y_date_end = y_date_end.strftime("%Y-%m-%d")

        X = ts.get_hist_data(code, start=date_start, end=date_end)
        X = X["close"].mean()

        Y = ts.get_hist_data(code, start=y_date_start, end=y_date_end)
        Y = Y["close"].mean()

        if X > Y:
            rate = round(X - Y, 2)
            rise.append(code + str(rate))
            print("{}----相对上涨----{}".format(code, rate))
        else:
            rate = round(Y - X, 2)
            rise.append(code + str(rate))
            if rate > 3:
                pre.append(code + "down" + str(rate))
            print("{}----相对下跌----{}".format(code, rate))

    except Exception as e:
        print(e)
        # continue
time_sign = datetime.datetime.now()

with open('sep/sep_rise', 'a+') as f:
    f.write(str(time_sign) + '\n' + str(rise) + '\n')

with open('sep/sep_down', 'a+') as t:
    t.write(str(time_sign)+ '\n' + str(down) + '\n')

with open('sep/sep_pre', 'a+') as t:
    t.write(str(time_sign)+ '\n' + str(pre) + '\n')
