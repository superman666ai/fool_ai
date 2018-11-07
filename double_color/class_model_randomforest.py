# -*- coding: utf-8 -*-

# @Time    : 2018/11/5 17:07
# @Author  : jian
# @File    : class_model_randomforest.py

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 导入数据
data = pd.read_csv("data/data.csv", encoding="utf8")
X = data.iloc[0: -1, 2:8]
Y = data.iloc[1:, 8:9]

# Y值降维
# pca = PCA(n_components=1)
# Y = pca.fit_transform(Y)
# print(Y)

# 数据归一化
# stand_scaler = StandardScaler()
# X = stand_scaler.fit_transform(X)
# print(X)
# Y = stand_scaler.transform(Y)
# 测试集 训练集划分
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=1)

# 建模
model = RandomForestClassifier()

# 预测
model.fit(x_train, y_train)
y_predict = model.predict(x_test)
# y_predict = stand_scaler.inverse_transform(y_predict)
score = model.score(x_test, y_test)

# print('预测值{}'.format(y_predict))
# print('真实值{}'.format(y_test))
print("model分数{}".format(score))
