from random import randint
print('Olá sou seu computador')
print('Acabei de pensar em um número entre 0 e 10')
print('será que você consegue adivinhar qual foi?')
din = randint(0,10)
acertou = False
palpite = 0
while not acertou:
    num  = int(input('digite seu chute: '))
    palpite += 1
    if num == din:
        acertou = True
    else:
        if num < din:
            print('mais alto ... tente mais uma vez')
        else:
            print('mais baixo ... tente mais uma vez')
print('Acertou com {} tentativas'.format(palpite))








