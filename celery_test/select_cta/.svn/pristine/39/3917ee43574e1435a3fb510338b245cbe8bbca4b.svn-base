#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2018/4/13 10:32
# @Author  : XieTianshun
# @Site    : 
# @File    : choose_base.py
# @Software: PyCharm

""" 选股基类 """

# sys lib
import pandas as pd
import pymongo
from bson import ObjectId
from libwt.base.wt_error_message import WtErrorMessage

from config import Config
from utils.macf import Macf


class ChooseBase(WtErrorMessage):
    """ """

    def __init__(self):
        WtErrorMessage.__init__(self)

        self.status = Macf.StatusRun
        self.tid = ''
        self.param = None
        self.sort_key = 'date'
        self.ok_qk = []

        # 创建 mongo 连接
        self.mgtb = pymongo.MongoClient(
            Config.MONGO_HOST_CORE,
            Config.MONGO_PORT_CORE
        ).get_database(
            Config.MONGO_DB_CORE
        ).get_collection(Config.MONGO_TB_CHOOSE_STOCK)


    def set_status(self, status):
        """
        设置
        :param status:
        :return:
        """
        self.status = status


    def set_param(self, param):
        """
        加载 参数 信息
        :param param:
        :return:
        """

        self.param = param
        self.param.set_index(Macf.Code, inplace=True)


    def set_tid(self, tid):
        """
        设置 任务 id
        :param tid:
        :return:
        """
        self.tid = ObjectId(tid)


    def set_load_data(self, objld):
        """
        设置 加载 load 对象
        :param ld:
        :return:
        """

        self.ld = objld()


    def set_sort_key(self, key):
        """

        :param key:
        :return:
        """
        self.sort_key = key


    def refresh_status(self):
        """
        刷新 task 状态
        :return:
        """
        try:

            search = {'_id': self.tid}

            motify = {Macf.TaskStatus: self.status}

            # 那 mongo 句柄 刷新 status
            rst = self.mgtb.update_one(search, {'$set': motify})

            print rst.raw_result

        except Exception, e:
            self.set_err_message(e)
            return False


    def load_tid_info(self):
        """
        加载 tid 信息
        :return:
        """

        item = self.mgtb.find_one({'_id': self.tid})

        param_body = item.get('param_body')
        param_title = item.get('param_title')

        df = pd.DataFrame(param_body, columns=param_title)

        # df.set_index('code', inplace=True)

        self.set_param(df)


    def parse_param(self):
        """
        处理 参数
        :return:
        """


    def refresh_result(self):
        """
        将 结果 update 数据库
        :return:
        """

        try:

            search = {'_id': self.tid}

            motify = {Macf.Qk: self.ok_qk}

            # 那 mongo 句柄 刷新 status
            rst = self.mgtb.update_one(search, {'$set': motify})

            print rst.raw_result

            self.set_status(Macf.StatusDone)

        except Exception, e:
            self.set_err_message(e)
            return False


    def filtrate_stock(self):
        """
        筛选股票
        :param qk:
        :return:
        """



    def run(self):
        """
        入口
        :return:
        """
        try:
            # 根据 tid 刷新 task 状态
            self.refresh_status()

            # 根据 tid 加载 task 信息
            self.load_tid_info()

            # 处理 参数
            self.parse_param()

            # 根据 task 参数 生成 所需 数据的 tb 句柄（分离）
            self.ld.set_param(self.param)
            self.ld.parse_param()
            self.qttb = self.ld.get_datb_by_param()

            # 获取 复权信息的 句柄
            self.fqtb = self.ld.get_fqtb_by_param()

            self.ld.get_iftb_by_param()

            # 将 tb 句柄 交给 load_data 类去 获取 data
            # 将 根据 param 获取 的数据集 feed 给 算法 （分离）
            self.filtrate_stock()

            # 接受 算法的 结果
            # 如果 成功 将 结果集 update 到 task 中
            self.refresh_result()

        except Exception, e:

            print e

            self.set_status(Macf.StatusErr)

        finally:

            # 最后 根据 设置 status 去 update status
            self.refresh_status()

