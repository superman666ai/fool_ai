#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2018/3/30 10:02
# @Author  : XieTianshun
# @Site    : 
# @File    : trigger_strategy.py
# @Software: PyCharm

""" 触发任务 """

# sys lib

# tp lib
import subprocess

# proj lib
from src.task_config import TaskConfig


tid = "5abd99bc843ce1bdf9ac402b"

cmd = TaskConfig.TRIGGER_CMD.format(
    python=TaskConfig.PYTHON,
    py='../main_shell.py',
    arg=tid,
)

print cmd

subprocess.call(cmd)
# subprocess.call(cmd, shell=True)

