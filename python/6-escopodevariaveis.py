# podemos atribuir um mesmo valor a varias variaveis
x = y = z = 10

# os valores podem ser atribuidos como uma fila (de forma respectiva)
x, y, z = "tubarão", 2.05, 16

# criamos uma var global (fora da função)
glb_var = "global"
#chamando a var global
print(glb_var)

# criando uma var local (dentro da função)
def var_function():
    lcl_var = "local"
    print(lcl_var)
# chamando a var local
var_function()

# quando temos duas variaveis com o mesmo nome uma vai sombrear a outra dependendo
# da chamada
num1 = 5
def minha_function():
    num1 = 10   # temos a variavel com o mesmo nome da global. Nesse caso ela vai sombrear a global e printar a local
    print(num1)
minha_function()
print(num1)   # ja aqui ela vai printar a global

# é possivel criar uma variavel global dentro de uma function
def nova_msg():
    global msg    # não é uma pratica recomendada
    msg = "olá mundo"
nova_msg()
# abaixo estamos acessando a variavel que seria local e virou global
print(msg)

# podemos incluir variaveis a uma string com o metodo .format()
print("Pedro tem {} laranjas".format(5))
print("João tem {} bananas e {} maças".format(4, 5))
print("Maria tem {1} bananas e {0} maças".format(4, 5))
print("Bruno tem {aaa} bananas e {bbb} maças".format(aaa = "quatro", bbb = "três"))
# {1:3d} quer dizer que na posição 1 serao 3 decimais (se n tiver ele coloca um
# espaço em branco), assim com .3f que vai deixar 3 casas decimais
modelo = "Pedro tem {0:s} laranjas e {1:3d} maças e {2:.3f} outras frutas"
print(modelo.format("cinco", 10, 3.55477))

# exercicios de fixação
var_int = 50
nota_aluno = 8.5
x = 150
x = x * 2
def imprimir():
    print(x)
print("{0:.2f}".format(357.756))
# no processo de formatação de decimais o format arredonda