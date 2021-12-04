!pip install tensorflow
# example of loading the mnist dataset
import tensorflow.keras.datasets.mnist as mnist
from matplotlib import pyplot as plt
import numpy as np
# load dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# summarize loaded dataset
print('Train: X=%s, y=%s' % (x_train.shape, y_train.shape))
print('Test: X=%s, y=%s' % (x_test.shape, y_test.shape))
