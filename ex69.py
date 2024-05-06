while True:
    escolha= int(input('qual tabuada deseja: '))
    if escolha < 0:
       break
    print('-' * 20)
    for c in range (1, 11):
        print(f'{escolha} X {c} = {escolha*c}')
    print('-' * 20)

print('digite um valor positivo++')