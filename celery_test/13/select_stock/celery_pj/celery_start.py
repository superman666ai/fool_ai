# -*- coding: utf-8 -*-

# @Time    : 2018/9/6 15:11
# @Author  : jin
# @File    : celery.py

from __future__ import absolute_import, unicode_literals
from celery import Celery
from config import Config

app = Celery('play',
             broker=Config.REDIS_BROKER,
             backend=Config.REDIS_BACKEND,
             include=['celery_pj.tasks'])

if __name__ == '__main__':
    app.start()
