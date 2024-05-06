from random import randint
from time import sleep
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0,2)
print('SUAS JOGADAS\n'
      '[0] pedra\n'
      '[1] papel\n'
      '[2] tesora')
jogador = int(input('Escolha sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-=' * 15)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 15)
if computador == 0: #pedra
    if jogador ==  0:
        print('o resultado é empate')

    elif jogador ==  1:
        print('o jogador venceu')

    elif jogador ==  2:
        print('o jogador perdeu')

    else:
        print('opção invalida')

elif computador == 1:               #papel
    if jogador ==  0:
        print('o jogador perdeu')
    elif jogador ==  1:
        print('empate')
    elif jogador == 2:
        print('o jogador venceu')
    else:
        print('opção invalida')
elif computador == 2:               #tesoura
    if jogador == 0:
        ('o jogador venceu')
    elif jogador == 1:
        ('o jogador perdeu')
    elif jogador == 2:
        print('empate')
    else:
        print('opção invalida')