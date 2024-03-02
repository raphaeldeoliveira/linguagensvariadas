# metodos de conversão para maiusculo e minusculo
minusculo = "minusculo"
maiusculo = "MAIUSCULO"
print(minusculo.upper())
print(maiusculo.lower())

# metodos de verificação (retornam um booleano)
print(maiusculo + " é minusculo? " + str(maiusculo.islower()))
print(maiusculo + " é maiusculo? " + str(maiusculo.isupper()))
print(maiusculo + " é alphanumerico? " + str(maiusculo.isalnum()))
print(maiusculo + " é alfabetico? " + str(maiusculo.isalpha()))
print(maiusculo + " é numerico? " + str(maiusculo.isnumeric()))
print(maiusculo + " é espaço em branco? " + str(maiusculo.isspace()))
print(maiusculo + " é um titulo? " + str(maiusculo.istitle()))

# metodo para tamanho da string
print(len(maiusculo))

# UNIR duas strings (interpolar)
print("-".join(maiusculo))

# SEPARAR (divide e retorna um array com as strings (o valor passado como parametro é "excluido", se nao for passado nada considera como espaço em branco))
print(str(maiusculo.split("U")))
print("o dia inteiro te odeio te busco e te caço".split())

# SUBSTITUIR
print("Olá mundo".replace("mundo", "pessoas"))