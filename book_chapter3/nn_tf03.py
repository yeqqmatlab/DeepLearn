# -*- coding:utf-8 -*-

import tensorflow as tf
from numpy.random import RandomState

# def batch
batch_size = 8

# def the args of nn
w1 = tf.Variable(tf.random_normal([2, 3], stddev=1))
w2 = tf.Variable(tf.random_normal([3, 1], stddev=1))

x = tf.placeholder(tf.float32, shape=(None, 2), name='x-input')
y_ = tf.placeholder(tf.float32, shape=(None, 1), name='y-input')

# def nn --->
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

# def 损失函数和反向传播算法
y = tf.sigmoid(y)
# 损失函数
cross_entropy = -tf.reduce_mean(
        y_*tf.log(tf.clip_by_value(y, 1e-10, 1))
        + (1-y)*tf.log(tf.clip_by_value(1-y, 1e-10, 1))
    )

# learning_rate
learning_rate = 0.001

train_step = tf.train.AdamOptimizer(learning_rate).minimize(cross_entropy)

# get dataset
rdm = RandomState(1)
dataset_size = 128

X = rdm.rand(dataset_size, 2)

Y = [[int(x1 + x2 < 1)] for (x1, x2) in X]

# create session
with tf.Session() as sess:
    init_op = tf.global_variables_initializer()
    # init w1 w1
    sess.run(init_op)

    print sess.run(w1)
    print sess.run(w2)

    # def steps
    STEPS = 5000
    for i in range(STEPS):
        # batch_size
        start = (i*batch_size % dataset_size)
        end = min(start+batch_size, dataset_size)
        # print i,"<-------------",start, end, "------------->"

        # train nn from data and update args w1 w1
        sess.run(train_step,
                 feed_dict={x: X[start:end], y_: Y[start:end]})
        if i % 16 == 0:
            # print i,"<-------------",start, end, "------------->"
            # print X[start:end],"-----", Y[start:end]
            print "-----w1--->",sess.run(w1)
            print "-----w2--->",sess.run(w2)


        if i % 1000 == 0:
            #  每隔一段时间计算在所有数据上的交叉熵并输出
            total_cross_entropy = sess.run(
                cross_entropy, feed_dict={x: X, y_: Y} )

            print ("After %d training steps, cross entropy is %g" % (i, total_cross_entropy))


    print sess.run(w1)
    print sess.run(w2)





























