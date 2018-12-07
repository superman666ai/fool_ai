# -*- coding: utf-8 -*-

# @Time    : 2018/9/18 16:16
# @Author  : jin
# @File    : other_methods.py
import pandas as pd
import numpy as np
import tushare as ts
import tushare as ts
import matplotlib.pyplot as plt

# data = ts.get_sina_dd("600198", date="2018-09-18")
# print data
# data = ts.top_list("2018-09-17")


# data = ts.get_latest_news() #默认获取最近80条新闻数据，只提供新闻类型、链接和标题
# print data
# data = ts.get_latest_news(top=5,show_content=True) #显示最新5条新闻，并打印出新闻内容
#
# data = ts.get_stock_basics()
# print data


class OtherInfor(object):

    def cap_tops(self):
        """
        获取近5、10、30、60日个股上榜统计数据,包括上榜次数、累积购买额、累积卖出额、净额、买入席位数和卖出席位数。
        :return:
        """
        df = ts.get_k_data('600600')
        print df
        #
        # df['MA10_rolling'] = pd.rolling_mean(df['close'], 10)
        # close = [float(x) for x in df['close']]
        # # 调用talib计算10日移动平均线的值
        # df['MA10_talib'] = talib.MA(np.array(close), timeperiod=10)
        # df.tail(12)


        # data = ts.cap_tops()
        # print list(data["code"])
        # return data


def main():
    a = OtherInfor()
    a.cap_tops()


if __name__ == '__main__':
    main()
