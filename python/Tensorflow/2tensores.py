import tensorflow as tf
import numpy as np

# cria um tensor de 4 dimensoes cheio de zeros
rank_4_tensor = tf.zeros([3, 2, 4, 5])

print("Type of every element: ", rank_4_tensor.dtype)
print("Number of axes: ", rank_4_tensor.ndim)
print("Shape of tensor: ", rank_4_tensor.shape)
print("Elements along axis 0 of tensor: ", rank_4_tensor.shape[0])
print("Elements along the last axis of tensor: ", rank_4_tensor.shape[-1])
print("Total number of elements (3*2*4*5): ", tf.size(rank_4_tensor).numpy())

# indexação de tensores 
rank_1_tensor = tf.constant([0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
print(rank_1_tensor.numpy())

print("First: ", rank_1_tensor[0].numpy())
print("Second: ", rank_1_tensor[1].numpy())
print("Last: ", rank_1_tensor[-1].numpy())

print("Everything: ", rank_1_tensor[:].numpy())
print("Before 4: ", rank_1_tensor[:4].numpy())
print("From 4 to the end: ", rank_1_tensor[4:].numpy())
print("From 2, before 7: ", rank_1_tensor[2:7].numpy())
print("Every other item: ", rank_1_tensor[::2].numpy())
print("Reversed: ", rank_1_tensor[::-1].numpy())

# para tensored com mais dimensões

rank_2_tensor = tf.constant([1, 2, 3, 4, 5, 6])
print(rank_2_tensor.numpy())

print(rank_2_tensor[1, 1].numpy()) # S: 4

rank_3_tensor = tf.constant([[[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]], [[10, 11, 12, 13, 14], [15, 16, 17, 18, 19]], [[20, 21, 22, 23, 24], [25, 26, 27, 28, 29]]])
print(rank_3_tensor[:, :, 4])

# shape do tensor
x = tf.constant([[1], [2], [3]])
print(x.shape)

# reshape
reshaped = tf.reshape(x, [1, 3])
print(reshaped.shape)

# cast (conversão de tipo)
the_f64_tensor = tf.constant([2.2, 3.3, 4.4], dtype=tf.float64)
the_f16_tensor = tf.cast(the_f64_tensor, dtype=tf.uint16) # perde o foco do decimal
# S: [2, 3, 4]

# broadcasting -> feito de forma implicita

x = tf.constant([1, 2, 3])

y = tf.constant(2)
z = tf.constant([2, 2, 2])
# todos os prints fazem a mesma operação
print(tf.multiply(x, 2))
print(x * y)
print(x * z)

# broadcast explicito -> força a criar o tensor
print(tf.broadcast_to(tf.constant([1, 2, 3]), [3, 3]))