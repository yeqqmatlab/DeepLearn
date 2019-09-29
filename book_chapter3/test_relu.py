# -*- coding:utf-8 -*-

import tensorflow as tf

X = tf.constant([[1,-2]])

A = tf.constant([1,-1])
B = tf.constant([3,6])

b = tf.constant(-6)
y = tf.nn.relu(A)
# 修剪函数
c = tf.clip_by_value(X,-1,1)


ab = tf.reduce_mean(B*X)


sess = tf.Session()

init_op = tf.global_variables_initializer()
sess.run(init_op)

print sess.run(y)

print sess.run(c)

print sess.run(ab)









