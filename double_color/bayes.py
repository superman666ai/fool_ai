# -*- coding: utf-8 -*-

# @Time    : 2018/11/23 13:59
# @Author  : jian
# @File    : class_model_nn.py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB

data = pd.read_csv("data/data.csv")
# 构建特征 目标值

X = data.iloc[0: -1, 1:7]
Y = data.iloc[1:, 7:]

# print(X.shape, Y.shape)
# minmax = MinMaxScaler()
# X = minmax.fit_transform(X)
# #测试集 训练集划分
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.25)
# print(x_test)
# 建模
nn = MultinomialNB()

nn.fit(x_train, y_train)

y_predict = nn.predict(x_test)

pre = nn.predict([[1, 10, 25, 27, 30, 32]])
# pre = nn.predict([[3, 5, 11, 15, 20, 23]])
# pre = nn.predict([[1, 3, 6, 10, 11, 29]])
print(pre, "pre")
# dict = nn.predict(x_test)
# print(nn.out_activation_)

# 预测准确率
print(nn.score(x_test, y_test))

t = np.arange(len(y_test))
plt.figure()
plt.plot(t, y_test, 'r-', linewidth=2, label='Test_b')
plt.plot(t, y_predict, 'g-', linewidth=2, label='Predict_b')
plt.xticks(tuple(x for x in range(len(y_test))))
plt.grid()
plt.show()
