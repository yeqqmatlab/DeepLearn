import tensorflow as tf

a = tf.constant([1, 2], name="a")
b = tf.constant([2, 2], name="b")

res = tf.add(a, b, name="add")
print res.name

res1 = a + b
sess = tf.Session()

# 以下二个命令的功能相同
# print sess.run(res1)
# print res1.eval(session=sess)
# print res1.eval()
