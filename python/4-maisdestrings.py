# Uma string é tratada como uma lista no python

# podemos acessaar o indice para retornar um caractere
msg = "Olá Mundo!"
print(msg[4])   # vai retornar o "M"

# é possivel pegar com um indice de tras pra frente com indice negativo
# isso é util para pegar o ultimo index sem usar o len() entre []
msg = "Olá Mundo!"
print(msg[-2])    # vai retornar o "o"

# podemos pegar um intervalo da string
# o primeiro parametro (caracter de incio) é inclusivo e o segundo (caracter de fim) é exclusivo
msg = "Olá Mundo!"
print(msg[4:9])   # retorna "Mundo"
# podemos omitir o primeiro parametro ou o ultimo pra ele considerar o primeiro e o ultimo caracter respectivamente
print(msg[:3])   # retorna Olá
print(msg[4:])   # retorna Mundo!
# podemos adicionar um terceiro parametro que é o passo (pulo)
print(msg[0:7:2])   # retorna OáMn

# podemos usar o metodo len() pra saber a quantidade de caracteres que a string tem
print(len(msg))   # retorna 10

# podemos contar quantos caracteres especificos a string tem
print("O rato roeu a roupa do rei de roma".count("r"))   # retorna 5

# pra encontrar a posição que se encontra o primeiro caractere
print("Vamos estudar python".find("a"))
print("Vamos estudar Python".find("Python"))
# é possivel especificar um intervalo para essa busca
print("Vamos estudar Python".find("t", 2, -5))




# exercicios de fixação - aula 8 (bem como todos os conceitos desse .py)
msg = "A ligeira raposa marrom ataca o cão preguiçoso"
print(msg[12])
print(msg[8:])
print(msg[::-1])
print(msg.count("a"))