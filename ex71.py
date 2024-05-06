print('Loja do Kayky')
tot = totmil = menor = cont = 0
bara = ''
while True:

    produto = str(input('Digite o nome do produto: '))
    valor = float(input('digite o valor do produto: '))
    tot += valor
    cont += 1
    if valor > 1000:
        totmil += 1
    if cont == 1 or valor < menor:
        menor = valor
        bara = produto
    escolha = ' '
    while escolha not in 'NS':
        escolha = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
    if escolha == 'N':
        break
print('FIM DO PROGRAMA')
print(f'O total da compra foi: {tot}')
print(f'{totmil} produtos custaram mais de R$ 1000,00')
print(f'o produto com menor preço foi {bara} custa R${valor:.2f}')
