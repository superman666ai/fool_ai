#!/usr/bin/env python
#  -*- coding: utf-8 -*-

# @Time    : 2018/3/30 9:52
# @Author  : XieTianshun
# @Site    : 
# @File    : main_shell.py
# @Software: PyCharm

""" 入口程序 """

# sys lib
import sys
sys.path.append('/opt/pylibwt')
import multiprocessing
from threading import Thread

# tp lib

# proj lib
from base.utils1 import load_task_info
from task_config import TaskConfig


def load_strategy(tid):
    """

    :param tid:
    :return:
    """

    item = load_task_info(tid)
    if type(None) == type(item):
        print '{} don`t find from mongodb !'.format(tid)

    fi = item.get('func_id')

    # 选择对应的 股票

    fp = TaskConfig.FUNC_MAP.get(fi)

    # 激活 进程 去 执行 对应函数
    run_by_processes(fp, tid)


def run_by_processes(func, argc):
    """
    使用进程来干活
    :param func:
    :param argc:
    :return:
    """

    func(argc)

    # th = Thread(
    #     target=func,
    #     args=argc
    # )

    # 启动线程
    # th.start()

    # p = multiprocessing.Process(target=func, args=argc)
    # p.start()
    # p.join()


def main():
    """

    :return:
    """
    if len(sys.argv) == 1:
        print '参数传送错误'

    # 从参数中 获取 tid
    tid = sys.argv[1]

    # 根据 task_id 加载 策略信息
    load_strategy(tid)


def main_celery(tid):
    """

    :param tid:
    :return:
    """

    # 根据 task_id 加载 策略信息
    load_strategy(tid)


if __name__ == '__main__':


    main()