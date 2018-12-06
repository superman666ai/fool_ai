# -*- coding: utf-8 -*-

# @Time    : 2018/9/6 15:40
# @Author  : jin
# @File    : test.py

from celery_pj.tasks import trans_info

a = trans_info.delay("5b8fac3e6e9dee00587b3207")

