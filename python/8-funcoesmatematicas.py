# abs() -> modulo (comprimento do numero)
km_inicial = 125
km_final = 33
diferenca = km_final - km_inicial # vai da valor negativo
diferenca_positivo = abs(diferenca)
print("A diferença de distancia é " + str(diferenca_positivo))

# divmod() -> retorna o quociente e o resto em uma tupla passamos dois argumentos
# basicamente executa (a // b, a % b)
a = 10
b = 3
print(divmod(a, b))
# é a mesma coisa que o print abaixo
print((a // b, a % b))

# pow() -> faz exponenciação
print(pow(5, 2))   # equivale a 5 ** 2

# round() -> faz arredondamento -> recebe dois parametros, o numero e o numero
# de casas decimais para arredondar
i = 17.349894525092
print(round(i, 4))
print(round(i, 2))
print("" + str(round(i, 1)))

# sum() -> somatorio da mtm
alguns_float = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
print(sum(alguns_float))   # soma todos os elementos da lista
# da pra fazer com dicionario, nesse caso ele soma as chaves
print(sum({-10: 30, -20: 'y', -30: 'z'}))

# exercicios de fixação
print(abs(100-500))
print(divmod(53, 7))
print(pow(10, 10))
print(round(5.47484, 1))
print(sum([1, 5, 99, 45, 33]))