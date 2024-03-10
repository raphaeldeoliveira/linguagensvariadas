# somando listas
criaturas_maritmas = ['tubarão', 'peixe', 'lula']
oceanos = ['pacifico', 'atlantico', 'artico']
print(criaturas_maritmas + oceanos)
# output: ['tubarão', 'peixe', 'lula', 'pacifico', 'atlantico', 'artico']

# adicionando um item a lista
print(criaturas_maritmas + ['mexilhão'])

# multiplicando uma lista ~ repete
print(criaturas_maritmas * 2)

# da pra usar o += ou *= pra modificar a lista com aquela operação

# deletando um elemento da lista
del criaturas_maritmas[1]
print(criaturas_maritmas)

# podemos deletar mais elementos com intervalo [:]
criaturas_maritmas *= 3
print(criaturas_maritmas)
del criaturas_maritmas[1:3]
print(criaturas_maritmas)

# listas de listas
nomes_marinhos = [['tubarão', 'peixe', 'camarão'], ['barbatana', 'nemo', 'cascudo']]
# acessmos seus indices como uma matriz
print(nomes_marinhos[0][1])   # peixe
print(nomes_marinhos[1][2])   # cascudo

# exercicios de fixação
linguagens = ['java', 'python', 'cobol', 'typescript', 'flutter']
print(linguagens)
print(linguagens[2])
print(linguagens[-1])
linguagens[0] = 'C#'
print(linguagens)
linguagens += ['prolog']
print(linguagens)

# metodos de listas

# append() -> adiciona um item ao final da lista
peixes = ['tilapia', 'bacalhau', 'sardinha']
peixes.append('tainha')
print(peixes)

# insert() -> adiciona um item a uma posição especifica
peixes.insert(0, 'salmao')
print(peixes)

# extend() -> adiciona uma lista ao final de outra lista
peixes.extend(['baleia', 'camarão'])
print(peixes)

# remove() -> remove o item de uma lista. O argumento é o proprio item
peixes.remove('bacalhau')
print(peixes)

# pop() -> retorna o elemento e o remove em seguida
print(peixes.pop(0))    # remove o primeiro elemento
print(peixes)
print(peixes.pop())    # remove o ultimo elemento
print(peixes)

# index() -> retorna o elemento que esta naquele indice
print(peixes.index('tainha'))