# -*- coding: utf-8 -*-

# @Time    : 2018/11/28 17:49
# @Author  : jian
# @File    : test.py

import tensorflow as tf
import numpy as np

# create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3

Weights = tf.Variable(tf.random_uniform([1], -1, 1))
biases = tf.Variable(tf.zeros([1]))

y = Weights * x_data +biases

loss = tf.reduce_mean(tf.square(y- y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# 初始化结构
init = tf.initialize_all_variables()

# 会话
sess = tf.Session()
sess.run(init)          # Very important

for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(Weights), sess.run(biases))