import os
import tensorflow as tf
import cProfile
import numpy as np

tf.executing_eagerly()

x = [[2.]]
m = tf.matmul(x, x)
print("hello, {}".format(m))

# criando um tensor
a = tf.constant([[1, 2], [3, 4]])
print(a)

# suporte a broadcast (broadcast = espalha uma operação)
b = tf.add(a, 1)
print(b)

# exemplo de sobrecarga de operador
print(a*b)

# o mesmo que o anterior com o numpy
c = np.multiply(a, b)
print(c)

# entraindo uma lista numpy do tensor
print(a.numpy())

# tensor padrão
rank_0_tensor = tf.constant(4) # tensor 
print(rank_0_tensor)

rank_1_tensor = tf.constant([2.0, 3.0, 4.0])
print(rank_1_tensor)

rank_2_tensor = tf.constant([[1, 2], [3, 4], [5, 6]], dtype=tf.float16)
print(rank_2_tensor)

rank_3_tensor = tf.constant([[[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]], [[10, 11, 12, 13, 14], [15, 16, 17, 18, 19]], [[20, 21, 22, 23, 24], [25, 26, 27, 28, 29]], ])
print(rank_3_tensor)

# transformando um tensor em um array numpy
print(np.array(rank_2_tensor))

# igual ao anteiror
print(rank_2_tensor.numpy())

# operações com tensores
f = tf.constant([[1, 2], [3, 4]])
g = tf.constant([[1, 1], [1, 1]])
print(tf.add(f, g), "\n")
print(tf.multiply(f, g), "\n")
print(tf.matmul(f, g), "\n")  # matmul faz a multiplicação de matrizes

# é possivel fazer as operações com sobrecarga de operadores
print(f + g, "\n")
print(f * g, "\n")
print(f @ g, "\n")

# demais operações com o tensor (retornam tensores, nao valores)
p = tf.constant([[4.0, 5.0], [10.0, 1.0]])
# encontrar o maior valor
print(tf.reduce_max(p))
# encontrar o indice do maior valor
print(tf.argmax(p))
# computar softmax
print(tf.nn.softmax(p))