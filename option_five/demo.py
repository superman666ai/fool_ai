# -*- coding: utf-8 -*-

# @Time    : 2018/11/9 10:18
# @Author  : jian
# @File    : demo.py
import pandas as pd
from itertools import combinations

data = pd.read_csv("data/20181107.csv")
# 所有数据
all = list(data.drop(["id"], axis=1).values)

# 构造新的dataframe
new_data = []
for i in all:
    new_data.append(sorted(list(i)))


data_csv = pd.DataFrame(data=new_data, index=data["id"], columns=["a", "b", "c", "d", "e"])

# 拼接所有数字 组成ids
data_csv["ids"] = data_csv["a"].map(str) + data_csv["b"].map(str) + data_csv["c"].map(str) + data_csv["d"].map(str) + \
                  data_csv["e"].map(str)

group_data = data_csv.groupby(["ids"], as_index=False)['ids'].agg({'cnt': 'count'})

data_end = group_data.sort_values(by=["cnt"], ascending=False)


# 所有结果
all_data = list(combinations([x for x in range(1, 12)], 5))

# 全奇数
odd_data = list(combinations([x for x in range(1, 13, 2)], 5))

# 全偶数
even_data = [(2, 4, 6, 8, 10)]

# 顺子
stra_data = [(1, 2, 3, 4, 5), (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), (4, 5, 6, 7, 8), (5, 6, 7, 8, 9), (6, 7, 8, 9, 10),
             (7, 8, 9, 10, 11), (8, 9, 10, 11, 12)]

# 四连
four_data = []
for i in all_data:
    # 判断是否相连
    if i[0] + 1 == i[1] and i[1] + 1 == i[2] and i[2] + 1 == i[3]:
        four_data.append(i)
    elif i[1] + 1 == i[2] and i[2] + 1 == i[3] and i[3] + 1 == i[4]:
        four_data.append(i)

# 三连
three_data = []
for i in all_data:
    # 判断是否相连
    if i[0] + 1 == i[1] and i[1] + 1 == i[2]:
        three_data.append(i)
    elif i[1] + 1 == i[2] and i[2] + 1 == i[3]:
        three_data.append(i)
    elif i[2] + 1 == i[3] and i[3] + 1 == i[4]:
        three_data.append(i)

# 剩余
dell_data = odd_data + even_data + stra_data + four_data + three_data

remain_data = []
for i in all_data:
    if i not in dell_data:
        remain_data.append(i)
print(len(remain_data))


# print(len(all_data))
