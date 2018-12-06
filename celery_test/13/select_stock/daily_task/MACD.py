# -*- coding: utf-8 -*-

# @Time    : 2018/10/8 14:37
# @Author  : jin
# @File    : MACD.py

import tushare as ts


# df=ts.get_k_data('600600')
# print df

pro = ts.pro_api(token="095bcdf3baef2f08104831abfe943e71c307d0f3f2deaa134a74df4b")

data = pro.new_share(start_date='20180901', end_date='20181018')
print data