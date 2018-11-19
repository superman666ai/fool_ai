# -*- coding: utf-8 -*-

# @Time    : 2018/11/13 19:05
# @Author  : jian
# @File    : daily_basic.py
import datetime
import tushare as ts

token = "095bcdf3baef2f08104831abfe943e71c307d0f3f2deaa134a74df4b"
pro = ts.pro_api(token=token)
data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
code_list = list(data["ts_code"])
# print(code_list)
# code_list = ["002147.SZ"]
rise = []
down = []
num = 0
for code in code_list:
    try:
        date_end_str = datetime.datetime.now().strftime("%Y-%m-%d")
        # date_end_str = "2018-11-09"
        date_end = datetime.datetime.strptime(date_end_str, "%Y-%m-%d")
        date_start = (date_end + datetime.timedelta(days=-20)).strftime("%Y-%m-%d")
        date_end = date_end.strftime("%Y-%m-%d")

        # open high close low volume price_change p_change ma5 ma10 ma20 v_ma5 v_ma10 v_ma20 turnover
        X = pro.query('daily_basic', ts_code=code, start=date_start, end=date_end)
        data_pe = X[["pe", "pe_ttm"]]
        mean = data_pe["pe"].mean()
        mean2 = data_pe["pe_ttm"].mean()
        print(mean, mean2, code)
        if 13 < int(mean) < 20:
            print("{}----预计涨----{}%".format(code))
            rise.append(code)


        # if predict[0] < predict[1]:
        #     rate = round(((predict[1] - predict[0]) / predict[0]) * 100, 5)
        #     if rate > 5:
        #         rise.append(code)
        #     print("{}----涨----{}%".format(code, rate))
        # else:
        #     rate = round(((predict[0] - predict[1]) / predict[0]) * 100, 5)
        #     print("{}----跌----{}%".format(code, rate))
        #     down.append(code)
        #
        # num += 1
        # print("---", num)

        # 画图
        # print(Y)
        # print(predict)
        # t = np.arange(len(Y))
        # plt.figure()
        # plt.plot(t, list(Y), 'r-', linewidth=2, label='Test_b')
        # plt.plot(t, predict, 'g-', linewidth=2, label='Predict_b')
        # plt.grid()
        # plt.show()

    except Exception as e:
        print(e)
        # continue

# print(rise)
# print("----------")
# print(down)
