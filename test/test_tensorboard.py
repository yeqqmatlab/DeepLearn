import tensorflow as tf

a = tf.constant([1, 2], name="a")
b = tf.constant([2, 2], name="b")

res = tf.add(a, b, name="add")

writer = tf.summary.FileWriter("/Users/yqq/data/tf_log", tf.get_default_graph())
writer.close()

