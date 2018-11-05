# -*- coding: utf-8 -*-

# @Time    : 2018/11/5 11:13
# @Author  : jian
# @File    : test_data.py
import pandas as pd

data = pd.read_csv("/data/data.csv", encoding="utf-8")

print(data.head())

