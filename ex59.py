from time import sleep
n1 = int(input('digite o primeiro valor: '))
n2 = int(input('digite o segundo valor'))
opcao = 0
while opcao != 5:
    print('''   [ 1 ] SOMA
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opcao = int(input('escolha a opção: '))
    if opcao == 1:
        soma = n1 +n2
        print('o resultado da soma é: {}'.format(soma))
    elif opcao == 2:
        multi = n1 * n2
        print('O resultado da multiplicação é: {}'.format(multi))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('entre {} e {} o maior é {}'.format(n1,n2,maior))
    elif opcao == 4:
        n1 = int(input('digite o primeiro valor'))
        n2 = int(input('digite o segundo valor'))
    elif opcao == 5:
        print('finalizando...')
    else:
        print('Opção invalida')
    sleep(2)
    print('=-=' * 10)



