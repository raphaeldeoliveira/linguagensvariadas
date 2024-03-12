import numpy as np
# metodos de redução do ndarray

# ndarray
a = np.array([1, 2, 3, 4, 5, 6])

# ndarray.sum()
print(a.sum())

# ndarray.mean()
print(a.mean())

# ndarray.std()
print(a.std())

# ndarray.min()
print(a.min())

# ndarray.max()
print(a.max())

# ndarray.argmin()
print(a.argmin())

# ndarray.argmax()
print(a.argmax())

# metodos matematicos

# multiplicação de matrizes
# exemplo matriz com 1 linha
matrizA = np.array([1, 2, 3, 4, 5, 6])
matrizB = np.array([1, 2, 3, 4, 5, 6])
print(matrizA.dot(matrizB))
# o resultado da 91 porque na multiplicação de matrizes se multiplica linha por coluna para cada elemento
# porem como só temos uma linha ela vai multiplicar os elementos coluna a coluana

# exemplo matriz 3 x3
matrizA = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrizB = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrizC = matrizA.dot(matrizB)
print(matrizC)
# aqui a multiplicação é feita elemento por elemento, proporcionalmente relacionando linha com coluna

# transpose() -> retorna a transposta (inverte linha com coluna)
print(matrizA.transpose())

# round() -> arredonda para o inteiro mais proximo
matrizAFloat = np.array([1.1, 2.6, 3.3, 4.5, 4.59])
matrizArredondado = matrizAFloat.round()
print(matrizArredondado)

# metodos de modificação

# reshape() -> altera a forma dos dados -> muda as dimensões
uni_dimensao = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
array4x3 = uni_dimensao.reshape(4, 3)
array2x6 = array4x3.reshape(2, 6)

print(uni_dimensao)
print(array4x3)
print(array2x6)

# flatten() -> transforma o array em unidimentsional
print(array4x3.flatten())

# resize() -> como o reshape porem corta ou preenche elementos se necessario
# preenchendo elementos
array = np.array([1, 2, 3, 4, 5])
array.resize(2, 3)
print(array)
# cortando elementos
array2 = np.array([1, 2, 3, 4, 5])
array2.resize(2, 5)
print(array2)

# sort()
array = np.array([3, 1, 4, 1, 5, 9, 2, 6])
array.sort()
print(array)

# clip()
exemplo = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(exemplo.clip(5, 7))

# metodos de pesquisa e indexação

# argmax() -> retorna o indice do elemento com maior valor
array = np.array([5, 1, 2, 9, 0])
print(array.argmax())

# argmin() -> retorna o indice do elemento com menor valor
print(array.argmin())

# argsort() -> retorna os indices que ordenariam em ordem crescenet
print(array.argsort())

# nonzero() -> retorna os indices dos elementos que nao sao 0
print(array.nonzero())

# operações de conjunto

# unique()
rol = np.array([1, 1, 1, 2, 3, 4, 4, 5, 5, 6, 6, 7, 8, 8, 0])
print(np.unique(rol))

# union1d() -> retorna a união de dois vetores
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([2, 3, 5, 6])
print(np.union1d(arr1, arr2))

# podemos importar constantes como pi e infinito
print(np.inf)
print(np.pi)

# função de logaritmo
# log natural ~~ a base é o numero de Euler
print(np.log(10))
# log na base 2
print(np.log2(4))
# log na base 10
print(np.log10(1000))

# funções de trigonometria
print(np.sin(np.deg2rad(90)))
print(np.cos(np.deg2rad(180)))
print(np.tan(0))

aleatorios = np.random.rand(5)
print("Números aleatórios:", aleatorios)

sequencia = np.arange(10)
escolhas = np.random.choice(sequencia, 3)
print("Escolhas aleatórias:", escolhas)

sequencia = np.arange(10)
np.random.shuffle(sequencia)
print("Sequência embaralhada:", sequencia)