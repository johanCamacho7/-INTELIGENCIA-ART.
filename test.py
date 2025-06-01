import tensorflow as tf
from keras.src.datasets import mnist

print("TensorFlow version:", tf.__version__)
print("Keras version:", tf.keras.__version__)

(x_train, y_train), (x_test, y_test) = mnist.load_data()

print("Imagen shape:", x_train[0].shape)
print("Etiqueta:", y_train[0])
