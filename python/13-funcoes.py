# primeira função em python
def hello():
    print("Olá mundo!")
hello()

# função com argumentos
def adicionar_numeros(x, y, z):
   a = x + y
   b = x + z
   c = y + z
   print(a, b, c)
adicionar_numeros(1, 2, 3)

# argumentos nomeados
def profile(usuario, seguidores):
   print("Usuario: " + usuario)
   print("José" + str(seguidores))
profile(seguidores=200, usuario="Paulo")

# retornando um valor
def quadrado(y):
   y = y ** 2
   return y
resultado = quadrado(3)
print(resultado)

# função main
def ola():
   print("Olá mundo")
def main():
   print("Essa é a função principal")
   ola()
main()

# função que é executada somente se o programa é principal
if __name__ == '__main__':
    # codigo somente executado quando o programa é principal
   print("Esse programa é o principal")

# exercicios de fixação
def saudacao(nome):
   print("Olá " + nome)
saudacao("João")

def ehPar(numero):
   if numero % 2 == 0:
      return True
   else:
      return False
ehPar(3)
ehPar(6)

def main():
   def IMC(altura, peso):
      print("seu imc: 1.546")
   print("digite seu peso: ")
   peso = input()
   print("digite sua altura: ")
   altura = input()
   IMC(altura, peso)
if __name__ == '__main__':
   main()

# strip() -> remove os espaços em branco no inicio e no final da string
fruta = '   banana   '
print("minha fruta favorita é " + fruta.strip())