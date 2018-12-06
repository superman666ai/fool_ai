# -*- coding: utf-8 -*-

# @Time    : 2018/9/12 10:37
# @Author  : jin
# @File    : testcla.py

class A(object):
    def __init__(self):
        print "init A"

    def pr(self):
        print  "i'am C"


class B(A):
    def pr(self):
        print  "i'am B"

class C(A):
    def pr(self):
        print  "i'am C"

class D(A):
    def pr(self):
        print  "i'am D"

class F(A):
    def pr(self):
        print  "i'am F"



class Z(C, D, F):
    pass


a = Z()
a.pr()
