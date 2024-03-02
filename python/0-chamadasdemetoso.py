# função - como chamar uma fução
def somar(x, y):
    return x + y

# inputs
x = int(input("Digite o valor de x"))
y = int(input("Digite o valor de y"))

# concatenação de strings
print("A soma de x com y é: " + str(somar(x, y)))

# ----------------------------------------------------

# chamada pro opção - simulação de chat

from datetime import datetime

def chatgpt(option):
    if (int(option) == 1):
        return str(datetime.now().time())[0:8]
    elif (int(option) == 2):
        return "Pele"
    elif (int(option) == 3):
        return "Rio de Janeiro"
    else:
        return "opção inválida"

print("--" * 9)
print("Bib bop kkkkkk. Como posso te ajudar?")
print("-- 1- que horas são? --")
print("-- 2- quem é o rei do futebol? --")
print("-- 3- Onde é a cidade maravilhosa? --")
option = str(input("Resposta: "))

print(chatgpt(option))