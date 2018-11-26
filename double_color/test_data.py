# -*- coding: utf-8 -*-

# @Time    : 2018/11/5 13:09
# @Author  : jian
# @File    : test_data.py
import pandas as pd

data = pd.read_csv("data/2015001.csv")
data1 = pd.read_csv("data/2016001.csv")
data2 = pd.read_csv("data/2017001.csv")
data3 = pd.read_csv("data/2018001.csv")
result = data.append(data1, ignore_index=True)
result = result.append(data2, ignore_index=True)
result = result.append(data3, ignore_index=True)
result.to_csv("./data/data.csv",index=False )
