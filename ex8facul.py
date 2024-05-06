import random
lista = []
for i in range(20):
    aleatorio = random.randint(0,9)
    lista.insert(i, aleatorio)
jogador1 = input('digite seu nome jogador1: ')
jogador2 = input('digite seu nome jogador2: ')

tenta = int(input('chute um número {}: '.format(jogador1)))
tenta2 = int(input('digite um número {}: '. format(jogador2)))
contagem = lista.count(tenta)
contagem2 = lista.count(tenta2)
print(lista)
print('{} acertou o número {} vezes '.format(jogador1, contagem))
print('{} acertou o número {} vezes '.format(jogador2, contagem2))
if contagem > contagem2:
    print('parabens {} vc acertou mais'.format(jogador1))
elif contagem < contagem2:
    print('parabens {} vc acertou mais'.format(jogador2))
elif contagem == contagem2:
    print('EMPATE!!!')