#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2018/3/6 14:08
# @Author  : XieTianshun
# @Site    : 
# @File    : boll_bands.py
# @Software: PyCharm

""" 布林线上穿 策略 """

# sys lib

# tp lib
import pymongo
import pandas as pd
import numpy as np

# proj lib


def load_data(qk):
    """

    :return:
    """
    conn = pymongo.MongoClient(host='192.168.0.60', port=27000)
    db = conn.get_database('db_usstock_day')
    tb = db.get_collection('tb_stock_day_ft')

    # cur = tb.find({'qk': 'US.AAPL', 'date': {'$gte': 20180101}})
    cur = tb.find({'qk': qk})

    data = pd.DataFrame(list(cur))

    data.sort_values('date', inplace=True)

    return data


def cal_boll_band(data, window=20, numsd=2):
    """

    :param date:
    :return:
    """

    data['mid'] = data['close'].rolling(window).mean()
    data['tmp2'] = data['close'].rolling(window).std()
    data['top'] = data['mid'] + numsd * data['tmp2']
    data['bottom'] = data['mid'] - numsd * data['tmp2']

    return data


if __name__ == '__main__':


    df = load_data('US.JPT')

    bb_df = cal_boll_band(df, 20)


