#coding=utf-8

from celery import Celery
from main_shell import main_celery
import os

# proj lib
from config import Config


app = Celery('choose_stock', broker=Config.CELERY_REDIS)

# app.conf.update(
#       CELERYD_CONCURRENCY=3,
#       CELERYD_PREFETCH_MULTIPLIER=1,
# )

@app.task
def choose_stock(tid):
	"""

	:param tid:
	:return:
	"""
	print 'task {} go !'.format(tid)

	# real run
	status = os.popen('{} main_shell.py {} > ../logs/task.{}.log'.format(Config.PYTHON, tid, tid))

	# test run
	# status = os.popen('{} test_celery.py {} > ../logs/task.{}.log'.format(Config.PYTHON, tid, tid))


if __name__ == '__main__':
	app.start()

