# -*- coding: utf-8 -*-

# @Time    : 2018/11/5 14:06
# @Author  : jian
# @File    : model_knn.py

# 使用knn模型
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV


data = pd.read_csv("data/2015001.csv")
# 构建特征 目标值

X = data.iloc[0: -1, 1:7]
Y = data.iloc[1:, 7:]

# print(X.shape, Y.shape)

#测试集 训练集划分
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.25)

# 建模
model = KNeighborsClassifier()
# 交叉验证 选取最好 n
n_neighbors = [2, 3, 4, 5]
param = {"n_neighbors": n_neighbors}
gc = GridSearchCV(model, param_grid=param)
gc.fit(x_train, y_train)

# 预测准确率
print(gc.score(x_test, y_test))
# 交叉验证中最好的结果
print(gc.best_score_)
# 最好的模型
# print(gc.best_estimator_)
# 每个k的 验证结果
print(gc.cv_results_)