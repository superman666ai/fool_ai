# -*- coding: utf-8 -*-

# @Time    : 2018/8/31 11:46
# @Author  : jin
# @File    : methods.py

from basemethod import QueryIndividualShare
from methods import PriceStrategy
from other_methods import OtherInfor

class MixMethod(PriceStrategy, OtherInfor):
    pass


a = MixMethod()
# 测试横盘股票
# a.fun_price_strategy_across_dish(date=100, lte=15)
# print a.resp_data
# print a.result
# print len(a.result)

# 测试涨跌幅
a.fun_price_strategy_rise_down(date=10, lte=5, gte=-5)
print a.resp_data
a.data_to_csv()
# print a.result
# print len(a.result)

# 测试横盘股票2
# a.fun_price_strategy_across_dish2(date=100, lte=15)
# print a.resp_data
# print a.result
# print len(a.result)
