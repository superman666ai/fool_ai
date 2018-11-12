# -*- coding: utf-8 -*-

# @Time    : 2018/11/12 19:27
# @Author  : jian
# @File    : demo.py

from sklearn import svm

x=[[2,0],[1,1],[2,3]]
y=[0,0,1]
clf= svm.SVC(kernel='linear')
clf.fit(x,y)

print(clf)
print(clf.support_vectors_) # 找到支持向量
print(clf.support_) # 支持向量在数据里的index
print(clf.n_support_) # 针对分类 找出了几个支持向量

# predictLabel = clf.predict([-1,2])
# print(predictLabel)
