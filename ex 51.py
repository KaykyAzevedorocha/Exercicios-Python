termo = int(input('digite o primeiro termo: '))
razao = int(input('digite a razão: '))
decimo = termo + (10-1) * razao
for c in range(termo,decimo + razao, razao):
    print('{}'.format(c), end=' ->')
print('ACABOU')
