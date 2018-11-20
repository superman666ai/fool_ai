# -*- coding: utf-8 -*-

# @Time    : 2018/11/7 19:45
# @Author  : jian

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
        date_end_str = "2018-11-09"
        date_end = datetime.datetime.strptime(date_end_str, "%Y-%m-%d")
        date_start = (date_end + datetime.timedelta(days=-60)).strftime("%Y-%m-%d")
        date_end = date_end.strftime("%Y-%m-%d")

        # open high close low volume price_change p_change ma5 ma10 ma20 v_ma5 v_ma10 v_ma20 turnover
        X = ts.get_hist_data(code, start=date_start, end=date_end)
        X = X.sort_index(0)  # 将数据按照日期排序下。
        print(X)
        Y = X["close"] # 构造Y
        # 删除close
        del X["close"]
        predict_X = X.iloc[1:]

        # #使用最后一个数据做测试。
        predict_test = X.iloc[-2:]

        # 删除最后一条数据 偏移股票数据，今天的数据，目标是明天的价格
        X = X.iloc[:-1, :]

        Y = Y.iloc[1:]

        model = linear_model.LinearRegression()
        model.fit(X, Y)
        # print(Y)
        # print(X.shape, predict_test.shape)
        predict = model.predict(predict_test)
        # print(stock_y_test)
        #
        # # print("############## coef_ & intercept_ #############")
        # # print(model.coef_) #系数
        # # print(model.intercept_) #截断
        # print("score:", model.score(X, Y)) #评分
        #
        if predict[0] < predict[1]:
            rate = round(((predict[1] - predict[0]) / predict[0]) * 100, 5)
            rise.append(code + str(rate))
            if rate > 5:
                pre.append(code + "rise" + str(rate))
            print("{}----涨----{}%".format(code, rate))
        else:
            rate = round(((predict[0] - predict[1]) / predict[0]) * 100, 5)
            print("{}----跌----{}%".format(code, rate))
            down.append(code + str(rate))

        num += 1
        print("---", num)


        # 画图
        # print(Y)
        # print(predict)
        # t = np.arange(len(Y))
        # plt.figure()
        # plt.plot(t, list(Y), 'r-', linewidth=2, label='Test_b')
        # plt.plot(t, predict, 'g-', linewidth=2, label='Predict_b')
        # plt.grid()
        # plt.show()

    except Exception as e:

        print(e)
        # continue
time_sign = datetime.datetime.now()

with open('lin/lin_rise', 'a+') as f:
    f.write(str(time_sign) + '\n' + str(rise) + '\n')

with open('lin/lin_down', 'a+') as t:
    t.write(str(time_sign) + '\n' + str(down) + '\n')

with open('lin/lin_pre', 'a+') as t:
    t.write(str(time_sign) + '\n' + str(pre) + '\n')
