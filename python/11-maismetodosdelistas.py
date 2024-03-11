# copy() -> metodo para copiar uma lista
peixes = ['salmão', 'sardinha', 'tainha']
peixes2 = peixes.copy()
print(peixes2)

# reverse() -> reverte a ordem dos itens de uma lista
peixes.reverse()
print(peixes)

# count() -> retorna o numero de vezes que o elemento aparece na lista
print(peixes.count('salmão'))

# sort() -> faz ordenação da lista em ordem alfabetica (segundo a tabela ASCII)
peixes.append('bacalhão')
peixes.append('espada')
print(peixes)
peixes.sort()
print(peixes)

# clear() -> remove todos os elementos da lista
peixes.clear()
print(peixes)

# exercicios de fixação
nome_paises = ['Brazil', 'Nova Zelandia', 'Australia', 'França']
nome_paises.insert(0, 'Suécia')
nome_paises.pop()
nome_paises2 = nome_paises.copy()
nome_paises.reverse()

# CONTROLE DE FLUXO

# condicional if - elif - else
nota = 40
if nota >= 65:
   print("Passou")
elif nota >= 50:
   print("Recuperação")
else:
   print("Reprovou")


# instruções aninhadas
nota1 = 80
nota2 = 50
if nota1 > 60:
   if nota2 > 60:
      print('Passou nas duas fases')
   else:
      print('Só passou na primeira fase')
else:
   print('Não passou na primeira fase')

# while
senha = ''
while senha != 'admin':
   print('Digite a senha:')
   senha = input()
print('Senha correta!')

# exercicio de fixação

animais = []
while len(animais) < 5:
   print('Digite digite o nome do ' + str(int(len(animais)) + 1) + ' animal')
   animal = input()
   if (len(animal) < 3):
      print('Animal invalido. os animais devem ter ome maior que 3 letras')
   else:
      animais.append(animal)
print(animais)