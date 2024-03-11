# laõ de repetição for

for i in range(0, 5):
    print(i)

# range([start], [stop], [step])
# start = onde começa
# stop = onde termina
# step = passo    
for i in range(0, 15, 3):
    print(i)

# range decrescente
for i in range(50, 0, -10):
    print(i)

# range com lista
animais = ["macaco", "babuino", "lontra"]
for animal in animais:
    print(animal)

# combinando listas com range
animais = ['gato', 'cachorro', 'papagaio', 'canguru']
for item in range(len(animais)):
    animais.append('animal')
print(animais)

# no exemplo a baixo ele ja pega nome como uma lista
nome = 'animal'
for letra in nome:
    print(letra)

# recuperando o valores de um dicionario
cliente = {'nome': 'José', 'idade': '31', 'cidade': 'Brasilia', 'UF': 'DF'}
for chave in cliente:
    print(chave + ': ' + cliente[chave])

# laço aninhado
minha_lista = []
for x in [20, 40, 60]:
   for y in [2, 4, 6]:
      minha_lista.append(x * y)
print(minha_lista)

# lista de listas
lista_de_listas = [['cavalo', 'vaca', 'gato'], [0, 1, 2], [9.9, 8.8, 7.7]]
for lista in lista_de_listas:
   print(lista)

# break - quebra o laço
for i in range(10):
    print(i)
    if i == 5:
        break
print('Saiu do laço')

# continue - pula aquela parte mas continua o laço
numero = 0
for numero in range(10):
   numero += 1
   if numero == 5:
      continue
   print(numero)
print('Fora do laço')
# nesse caso vai pular o 5 (ele pula mas continua executando)

# exercicio de fixação
# crie um laço for que imprima os valores de 0 a 9
for i in range(10):
    print(i)

# crie um laço for que imprima os valores de 9 a 0 reduzindo 2 unidades por vez
#for i in range(9, 0, -2):
for i in range(9, -1, -2):
    print(i)

# crie um laço for que imprime a lista ['joao', 'maria', 'pedro', 'paulo'] em ordem inversacrie um laço for que imprime a lista ['joao', 'maria', 'pedro', 'paulo'] em ordem inversa
lista = ['joao', 'maria', 'pedro', 'paulo']
lista.reverse()
for item in lista:
    print(item)

# imprima a tuabuada do 0 a 5 com for aninhado
for x in range(6):
    for y in range(6):
        print(str(x) + ' * ' + str(y) + ' = ' + str(x * y))

# crie um laço for que itera de 1 a 10 porem só imprime se os numeros pares usando a instrução continue
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)