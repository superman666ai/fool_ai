# -*- coding: utf-8 -*-

# @Time    : 2018/11/5 13:09
# @Author  : jian
# @File    : test_data.py
import pandas as pd

data = pd.read_csv("data/data.csv")
print(data.describe())
