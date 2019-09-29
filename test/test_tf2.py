# -*- coding:utf-8 -*-

import tensorflow as tf
import numpy as np

x_data = np.float32(np.random.rand(100))
y_data = x_data*x_data*2 + 5

Weights = tf.Variable(tf.random_uniform([1], 0, 3))
b = tf.Variable(tf.zeros([1]))

print '-------*------'
print Weights, b
print '-------*------'

y = Weights*x_data*x_data + b

loss = tf.reduce_mean(tf.square(y-y_data))
opt = tf.train.GradientDescentOptimizer(0.5)
train = opt.minimize(loss)

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

for step in range(2001):
    sess.run(train)
    if step % 1000 == 0:
        print step, sess.run(Weights), sess.run(b)


