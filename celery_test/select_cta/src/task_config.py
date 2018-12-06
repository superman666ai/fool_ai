#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2018/3/27 11:52
# @Author  : XieTianshun
# @Site    : 
# @File    : task_config.py
# @Software: PyCharm

""" 任务 config """

# sys lib

# tp lib
from strategy_script import boll_bands_1
from strategy_script import test_celery

# proj lib


class TaskConfig:
    """ """

    TRIGGER_CMD = '{python} {py} {arg}'

    # python 执行 路径
    # PYTHON = '/opt/anaconda2/envs/py2/bin/python'
    PYTHON = 'python'

    FUNC_MAP = {
        'boll_bands_1': boll_bands_1.run_script,
        'test_celery': test_celery.run_script
    }

