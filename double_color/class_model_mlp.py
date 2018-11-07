# -*- coding: utf-8 -*-

# @Time    : 2018/11/5 19:03
# @Author  : jian
# @File    : class_model_mlp.py

# 多层感知机 对数据缩放比较敏感 建议归一化数据
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler


data = pd.read_csv("data/2015001.csv")
# 构建特征 目标值

X = data.iloc[0: -1, 1:7]
Y = data.iloc[1:, 7:]

# print(X.shape, Y.shape)
# 归一化数据
scaler = StandardScaler()
X = scaler.fit_transform(X)
#测试集 训练集划分
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

# 建模
model = MLPClassifier(solver='lbfgs', hidden_layer_sizes=(6, 2), random_state=1)

# 预测
model.fit(x_train, y_train)
y_predict = model.predict(x_test)
score = model.score(x_test, y_test)

# print('预测值{}'.format(y_predict))
# print('真实值{}'.format(y_test))
print("model分数{}".format(score))
# print(model.decision_function([[1,2,3,4,5,6]]).shape)

t = np.arange(len(y_test))
plt.figure()
plt.plot(t, y_test, 'r-', linewidth=2, label='Test_b')
plt.plot(t, y_predict, 'g-', linewidth=2, label='Predict_b')
plt.xticks(tuple(x for x in range(len(y_test))))
plt.grid()
plt.show()