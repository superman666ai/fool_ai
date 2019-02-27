# -*- coding: utf-8 -*-

# @Time    : 2019-01-28 17:02
# @Author  : jian
# @File    : test.py
import pandas as pd

data = pd.read_csv("data/20181107.csv")
print(data.shape)
data2 = pd.read_csv("data/20181108.csv")
print(data.shape)
data = data.append(data2)
print(data.head())

new_data = []
all = list(data.drop(["id"], axis=1).values)
for i in all:
    new_data.append(tuple(sorted(list(i))))

# print(new_data)
result = {}
t = 0
for i in set(new_data):
    cou = new_data.count(i)
    if cou > 1:
        t += 1
    result[i] = cou
print(result)

print(t)
