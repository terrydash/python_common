import tensorflow as tf


def start():
    matrix1 = tf.constant([[3., 3.]])

    matrix2 = tf.constant([[2.], [2.]])

    product = tf.matmul(matrix1, matrix2)
    sess = tf.Session()
    result = sess.run(product)

    sess.close()


if __name__ == '__main__':
    start()
