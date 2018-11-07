# -*- encoding:utf-8 -*-
"""
decision_tree
贪心算法 自上而下   下面三个属性度量不同
id3   information gain
c4.5  gain ratio
cart  gini
"""
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import tree
from sklearn import preprocessing
from sklearn.externals.six import StringIO

# 读取数据（pandas 读取）
data = pd.read_csv("data/data.csv", encoding="utf-8")

# csv 读取
allElectronicsData = open(r'data/data.csv', 'rt')
reader = csv.reader(allElectronicsData)
# for i in reader:
#     print(i)

X = data

# featureList = []
# labelList = []
#
# for row in reader:
#     labelList.append(row[len(row)-1])
#     rowDict = {}
#     for i in range(1, len(row)-1):
#         rowDict[headers[i]] = row[i]
#     featureList.append(rowDict)
#
# print(featureList)
#
# # Vetorize features
# vec = DictVectorizer()
# dummyX = vec.fit_transform(featureList) .toarray()
#
# print("dummyX: " + str(dummyX))
# print(vec.get_feature_names())
#
# print("labelList: " + str(labelList))
#
# # vectorize class labels
# lb = preprocessing.LabelBinarizer()
# dummyY = lb.fit_transform(labelList)
# print("dummyY: " + str(dummyY))
#
# # Using decision tree for classification
# # clf = tree.DecisionTreeClassifier()
# clf = tree.DecisionTreeClassifier(criterion='entropy')
# clf = clf.fit(dummyX, dummyY)
# print("clf: " + str(clf))
#
#
# # Visualize model
# with open("allElectronicInformationGainOri.dot", 'w') as f:
#     f = tree.export_graphviz(clf, feature_names=vec.get_feature_names(), out_file=f)
#
# oneRowX = dummyX[0, :]
# print("oneRowX: " + str(oneRowX))
#
# newRowX = oneRowX
# newRowX[0] = 1
# newRowX[2] = 0
# print("newRowX: " + str(newRowX))
#
# predictedY = clf.predict(newRowX)
# print("predictedY: " + str(predictedY))


