import tensorflow as tf
from dnc.controller import BaseController
from dnc.dnc import DNC
import random

class FeedForwardController(BaseController):
    def network_vars(self):
        self.W = tf.Variable(
                tf.truncated_normal([self.nn_input_size, 128]),
                name='weights'
        )
        self.b = tf.Variable(tf.zeros([128]), name='bias')

    def network_op(self, X):
        output = tf.matmul(X, self.W) + self.b
        activations = tf.nn.relu(output)
        return activations

dnc = DNC(FeedForwardController, 8, 8, 10)
optimizer = tf.train.RMSPropOptimizer(0.01, momentum=0.01)

outputs, _ = dnc_instance.get_outputs()
loss = tf.reduce_mean(tf.square(outputs - dnc_instance.target_output))
gradients = optimizer.compute_gradients(loss)
apply_gradients = optimizer.apply_gradients(gradients)

def convert(n):
    bits = [int(digit) for digit in bin(n)[2:]]
    while len(bits) < 8:
        bits = [0] + bits
    return bits

def deconvert(bits):
    return int(''.join(str(b) for b in bits), base=2)

with tf.Session() as sess:
    for step in range(100):
        in_ = [random.randrange(24) for _ in range(random.randrange(10))]
        out_ = [sum(in_)] + [0 for _ in range(len(in_) - 1)]
        sess.run(apply_gradients, feed_dict={
            dnc.input_data: list(map(convert, in_)),
            dnc.target_output: list(map(convert, out_)),
            dnc.sequence_length: len(in_),
        })
        print('.', end='')
        if step == 99:
            print()
            print(in_, sess.run(outputs, {
                dnc.input_data: list(map(convert, in_)),
                dnc.sequence_length: len(in_),
            }))
