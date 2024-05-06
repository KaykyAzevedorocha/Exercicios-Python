from random import randint
v=0
print('=-='* 10)
print('VAMOS JOGAR UM JOGO')
print('=-='* 10)
while True:
    jogador = int(input('digite um valor: '))
    comput = randint(0,10)
    tot = jogador + comput
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('ESCOLHA [p/i]')).strip().upper()[0]
    print(f'O computador escolheu {comput} e vc {jogador}, o total foi {tot} ')
    print('Deu Par' if tot % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if tot % 2 == 0:
            print(f'Você venceu')
            v += 1
        else:
            print(f'Você perdeu')
            break
    elif tipo == 'I':
        if tot % 2 == 1:
            print(f'Você Venceu')
            v += 1
        else:
            print(f'Você perdeu')
            break
    print('Vamos novamente')
print(f'Game Over vc venceu {v} vezes.')