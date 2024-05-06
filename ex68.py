from random import randint
v = 0
while True:
    escolhanum = int(input('digite o número que deseja: '))
    comput = randint(0,10)
    s = escolhanum + comput
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('digite sua escolha Par ou Impar: ')).strip()[0].upper()
    print(f'voce jogou {escolhanum} e o computador jogou {comput} o total foi {s}')
    if escolha == 'P':
        if s % 2 == 0:
            print('Voce venceu')
            v = v + 1
        else:
            print('Voce perdeu')
            break
    elif escolha == 'I':
        if s % 3 == 0:
            print('voce venceu')
            v = v + 1
        else:
            print('voce perdeu')
            break
    print('Vamos jogar novamente')
print(f' GAME OVER, voce venceu {v} ')

