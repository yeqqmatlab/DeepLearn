# -*- coding:utf-8 -*-

import tensorflow as tf

# def two mat
W1 = tf.Variable(tf.random_normal((2, 3), stddev=1, seed=1))
W2 = tf.Variable(tf.random_normal((3, 1), stddev=1, seed=1))

# X is 1*2 mat
X = tf.constant([[0.7, 0.9]])

# 向前传播算法获得神经网络的输出
A = tf.matmul(X, W1)
y = tf.matmul(A, W2)

# create session
sess = tf.Session()

# sess.run(W1.initializer)
# sess.run(W2.initializer)

init_op = tf.global_variables_initializer()
sess.run(init_op)

print sess.run(y)

sess.close()



