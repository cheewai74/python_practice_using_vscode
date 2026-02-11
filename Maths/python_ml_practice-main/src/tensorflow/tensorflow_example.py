import tensorflow.compat.v1 as tf

tf.compat.v1.disable_v2_behavior()
x = tf.compat.v1.placeholder(tf.string)

with tf.compat.v1.Session() as sess:
    output = sess.run(x, feed_dict={x: 'Hello World'})
    print(output)