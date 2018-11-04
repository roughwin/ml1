import tensorflow as tf

g = tf.Graph()
with g.as_default():
  import tensorflow as tf
  sess = tf.Session()
  W_m = tf.Variable(tf.zeros([10,5]))
  x_v = tf.placeholder(tf.float32, [None, 10])
  rersult = tf.matmul(x_v, W_m)
print(g.as_graph_def())
# t1 = tf.constant([[[1,2],[2,3]],[[3,4],[5,6]]])
# 
# print(t1)