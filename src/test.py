'''
This is a test for the dockerfile deployment
'''
import platform
import tensorflow as tf

from foo.bar import greet


if __name__ == '__main__':
    # Check python version
    print(platform.python_version())
    print(greet())

    # TensorFlow Test
    ## Creates a graph.
    a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
    b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
    c = tf.matmul(a, b)

    ## Creates a session with log_device_placement set to True.
    sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))

    ## Runs the op.
    print(sess.run(c))
