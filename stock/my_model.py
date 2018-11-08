# -*- coding: utf-8 -*-

# @Time    : 2018/11/7 19:45
# @Author  : jian
# @File    : regre_model_linear.py
import datetime
import pandas as pd
import tushare as ts

from sklearn import linear_model

code = "601360"
date_end_str = datetime.datetime.now().strftime("%Y-%m-%d")
date_end = datetime.datetime.strptime(date_end_str, "%Y-%m-%d")
date_start = (date_end + datetime.timedelta(days=-300)).strftime("%Y-%m-%d")
date_end = date_end.strftime("%Y-%m-%d")


# open high close low volume price_change p_change ma5 ma10 ma20 v_ma5 v_ma10 v_ma20 turnover
X = ts.get_hist_data(code, start=date_start, end=date_end)
X = X.sort_index(0)  # 将数据按照日期排序下。
print(X)
Y = pd.Series(X["close"].values)
print(X.shape, Y.shape)
#
#
# stock_X_test = stock_X.iloc[len(stock_X)-1]
#
# # 使用今天的交易价格，13 个指标预测明天的价格。偏移股票数据，今天的数据，目标是明天的价格。
# stock_X = stock_X.drop(stock_X.index[len(stock_X)-1]) # 删除最后一条数据
# stock_y = stock_y.drop(stock_y.index[0]) # 删除第一条数据
# #删除掉close 也就是收盘价格。
# del stock_X["close"]
# del stock_X_test["close"]
#
# #使用最后一个数据做测试。
# stock_y_test = stock_y.iloc[len(stock_y)-1]
#
# # print(stock_X.tail(5))
# # print("###########################")
# # print(stock_y.tail(5)) #
# #print(stock_X.values[0])
#
# # print("###########################")
# # print(len(stock_X),",",len(stock_y))
#
# # print("###########################")
# # print(stock_X_test.values,stock_y_test)
# print("----",stock_X.values )
# model = linear_model.LinearRegression()
# model.fit(stock_X.values,stock_y)
# # print("############## test & target #############")
#
# print("预测", model.predict([stock_X_test]))
# print(stock_y_test)
#
# # print("############## coef_ & intercept_ #############")
# # print(model.coef_) #系数
# # print(model.intercept_) #截断
# print("score:", model.score(stock_X.values,stock_y)) #评分
