# -*- coding: utf-8 -*-

# @Time    : 2018/11/8 9:30
# @Author  : jian
# @File    : demo.py
import pandas as pd

from sklearn import neighbors
from sklearn import datasets

knn = neighbors.KNeighborsClassifier()

iris = datasets.load_iris()

knn.fit(iris.data, iris.target)

predictedLabel = knn.predict([[0.1, 0.2, 0.3, 0.4]])
print (predictedLabel)
