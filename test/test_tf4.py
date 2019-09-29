import tensorflow as tf

mat1 = tf.constant([[3, 3]])
mat2 = tf.constant([[2],
                    [3]])

res = tf.matmul(mat1, mat2)

# sess = tf.Session()
# res1 = sess.run(res)
# print res1
# sess.close()

with tf.Session() as sess:
    res2 = sess.run(res)
    print res2