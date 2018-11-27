# -*- coding: utf-8 -*-

# @Time    : 2018/11/5 11:13
# @Author  : jian

import pandas as pd

data = pd.read_csv("data/13001.csv")
data1 = pd.read_csv("data/14001.csv")
data2 = pd.read_csv("data/15001.csv")
data3 = pd.read_csv("data/16001.csv")
data4 = pd.read_csv("data/17001.csv")
data5 = pd.read_csv("data/18001.csv")

result = data.append(data1, ignore_index=True)
result = result.append(data2, ignore_index=True)
result = result.append(data3, ignore_index=True)
result = result.append(data4, ignore_index=True)
result = result.append(data5, ignore_index=True)
result.to_csv("./data/data.csv", index=False)
