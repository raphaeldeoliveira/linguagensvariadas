# conversão de int para float
n = 10
print(n)
print(type(n))
f = float(n)
print(f)
print(type(f))

# conversão de float pra int
f = 325.7
print(f)
n = int(f)
print(n)

# divisao de dois int resulta em um float
print(5/2)

# converter numero para string
n = 1.81
# dessa forma da erro: print("eu tenho " + n)
print("eu tenho " + str(n) + " metros")

# convertendo string para int
a = "10"
b = "35.6"
c = int(a) - float(b)
print(c)
# note que se fosse um + funcionaria, ja que concatenaria as strings

# convertendo list para tuple
l = ["abacaxi", "uva", "laranja"]
t = tuple(l)
print(t)

# convertendo tuple para list
t = ("abelha", "formiga", "mosca")
l = list(t)
print(l)

# converter string em tupla (tabem vale para list)
msg = "Olá Mundo!"
tuplemsg = tuple(msg)
print(tuplemsg)

# exercicios de fixação
i = 10
f = float(i)
print("O valor i é " + str(i) + " e o valor de f é " + str(f))
fa = float("32.7")
print(fa)
n = 5000
nstring = str(n)
lista = list(nstring)
print(lista)