# aula numpy Gran

import numpy as np

# diferença entre ndarray e list
# exemplo de população de listas python normais (list)
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
c = []
for i in range(len(a)):
  c.append(a[i] * b[i])
print(c)
# exemplo com numpy
a = np.array(a)
b = np.array(b)
c = np.array([])
c = a * b
print(c)

# exemplos que ainda nao sei como funcionam
import numpy as np
a = np.arange(15).reshape(3, 5)
print(a)

print(a.shape)

print(a.ndim)

print(a.dtype)

print(a.itemsize)

print(a.size)

print(type(a))

b = np.array([6, 7, 8])
print(b)

print(type(b))

# criação de array
import numpy as np
a = np.array([2.1, 3.5, 4.2])
print(a)
print(a.dtype)

# criação de lista de listas
b = np.array([(1.5, 2, 3), (4, 5, 6)])
print(b)
print(b.dtype)

# criação de array explicitando o tipo
c = np.array([[1, 2], [3, 4]], dtype=complex)
print(c)
print(c.dtype)

# podemos criar arrays com conteudo fixo (reservado)

# matriz 3x4 somente com zeros
#print(np.zeros((3, 4)))

# duas matrizes 3x4 somente com 1
#print(np.ones((2, 3, 4), dtype=np.int16))

print(np.empty((2, 3)))

# podemos criar sequencias com np.arange
print(np.arange(10, 30, 5))

print(np.arange(0, 2, 0.3))

# podemos criar espaços lineares com linespace() isso serve para fazer como no ultimo exemplo, porem sem dar erro de perder a precisão em ponto flutuante
print(np.linspace(0, 2, 9))      # vai imprimir 9 elementos de 0 a 2

from numpy import pi

x = np.linspace(0, 2 * pi, 100)
f = np.sin(x)
print(x)
print(f)

# testes
import numpy as np
a = np.arange(5, 20).reshape(3, 5)
print(a)