# -*- encoding:utf-8 -*-
"""
decision_tree
贪心算法 自上而下   下面三个属性度量不同
id3   information gain
c4.5  gain ratio
cart  gini
"""
import pandas as pd
import json
from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import tree
from sklearn import preprocessing
from sklearn.externals.six import StringIO
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import LabelBinarizer
# 读取数据（pandas 读取）
data = pd.read_csv("data/data.csv", encoding="utf-8")

# csv 读取
# allElectronicsData = open(r'data/data.csv', 'rt')
# reader = csv.reader(allElectronicsData)
# for i in reader:
#     print(i)

print(data.head())
X = data.iloc[:, 1:-1]
Y = data.iloc[:, -1:]

# print(X)
# featureList = []
# labelList = []
#

#
# # Vetorize features
vec = DictVectorizer()
X = vec.fit_transform(json.loads(X.T.to_json()).values()) .toarray()


# # vectorize class labels
lb = LabelBinarizer()
Y = lb.fit_transform(Y)
# print(Y)
# print("dummyY: " + str(dummyY))
#
# # Using decision tree for classification
clf = tree.DecisionTreeClassifier()
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(X, Y)
# print("clf: " + str(clf))
#
#
# # Visualize model
# 保存树结构
# with open("tree.dot", 'w') as f:
    # f = tree.export_graphviz(clf, feature_names=vec.get_feature_names(), out_file=f)

#dot -T pdf tree.dot -o tree.pdf   转化为pdf


# 预测新的结果

oneRowX = X[0:1, :]

print (oneRowX)
newRowX = oneRowX
newRowX[0][0] = 1
newRowX[0][2] = 1
print(newRowX)
#
#
predictedY = clf.predict(newRowX)
print("predictedY: " + str(predictedY))


