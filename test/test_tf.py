import tensorflow as tf

a = tf.constant([1, 2],  name="a")

b = tf.constant([2, 3], name="b")


#
# result = a + b
#
# sess = tf.Session()
#
# print sess.run(result)

c1 = tf.constant([3])
c2 = tf.constant([[3]])

init_op = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init_op)

print c1
print c2

