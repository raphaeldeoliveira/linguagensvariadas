import random
numero = random.randint(1, 25)
n_tentativa = 0
while n_tentativa < 5:
    print('Advinhe um numero entre 1 e 25:')
    chute = input()
    chute = int(chute)
    n_tentativa += 1
    if chute < numero:
        print('Seu palpite é muito baixo')
    if chute > numero:
        print('Seu palpite é muito alto')
    if chute == numero:
        break
if chute == numero:
    print('Você advinhou o numero em ' + str(n_tentativa) + ' tentativas!')
else:
    print('Você não advinhou o numero Era ' + str(numero))