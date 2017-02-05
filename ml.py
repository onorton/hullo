from __future__ import print_function

import tensorflow as tf
from dnc.controller import BaseController
from dnc.dnc import DNC
import numpy as np
import random
import sys
import json

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

def binary_cross_entropy(predictions, targets):
    return tf.reduce_mean(
        -1 * targets * tf.log(predictions) - (1 - targets) * tf.log(1 - predictions)
    )

with open('outfile.json', 'r') as f:
    conversations = json.load(f)
my_aliases = {'Blaine William Rogers', 'Blaine Rogers'}

dnc = DNC(FeedForwardController, 10, 10, 1000)
optimizer = tf.train.RMSPropOptimizer(0.001, momentum=0.5)

outputs, _ = dnc.get_outputs()
squeezed = tf.clip_by_value(tf.sigmoid(outputs), 1e-6, 1. - 1e-6)

loss = binary_cross_entropy(squeezed, dnc.target_output)

gradients = optimizer.compute_gradients(loss)
apply_gradients = optimizer.apply_gradients(gradients)

def convert(n):
    bits = [int(digit) for digit in bin(n)[2:]]
    while len(bits) < 8:
        bits = [0] + bits
    return bits + [0, 0]

def deconvert(bits):
    return int(''.join('0' if b < .5 else '1' for b in bits), base=2)

def round_off(bits):
    return map(lambda f: round(f, 2), bits)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for conversation in conversations[0]:
        for length in range(1, min(10, len(conversation['messages']) - 1)):
            messages = conversation['messages'][:length]
            in_ = []
            for message in messages:
                try:
                    in_.extend(map(lambda c: convert(ord(c)), message['content']))
                    in_.append([0, 0, 0, 0, 0, 0, 0, 0, 1, 0])
                except:
                    continue
            in_.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
            out = map(lambda c: convert(ord(c)), conversation['messages'][length]['content'])
            out += [[0] * 10] * 5
            lenin = len(in_)
            in_ += [[0] * 10] * len(out)
            out = [[0] * 10] * lenin + out
            assert len(in_) == len(out)

            in_ = np.array([in_])
            out = np.array([out])

            o, l, _ = sess.run([squeezed, loss, apply_gradients], feed_dict={
                dnc.input_data: in_,
                dnc.target_output: out,
                dnc.sequence_length: in_.shape[1],
            })

        print('loss', l, 'message', ''.join(map(lambda l: chr(deconvert(l[:-2])), o[0])), end='\n\n')

    dnc.save(sess, 'checkpoints', 'checkpoint')
