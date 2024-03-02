# pode ser entre "" e ''
cor1 = "azul"
cor2 = 'vermelho'

# podemos usar "" ou '' uma dentro da outra
print('Olá "Mundo"!')
print("Olá 'Mundo'!")

# concatenação de string (+)
print(cor1 + " com " + cor2 + " da o roxo")

# propagação de strin (*)
fruta1 = "maça,  "
print(fruta1 * 5)

# podemos usar 3 aspas (duplas ou simples) para quebrar linhas automaticamente
xxx = """aaa
bbb
ccc"""
print(xxx)
yyy = '''
ccc
bbb
aaa'''
print(yyy)

# caracteres de escape
# \\ = \
# \" = "
# \' = '
# \n = quebra linha
print("\\ \"ola\", \n \'mundo\'!")

# se usar o prefixo r em uma string nenhum caracter de escape é usado
print(r"\\ \"ola\", \n \'mundo\'!")

