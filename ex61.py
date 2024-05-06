print('gerador de PA')
print('=-=' * 10)

pt = int(input('digite o primeiro termo: '))
razao = int(input('digite a razão: '))
cont = 0
termo = pt
while cont <= 10:
    print('{} -> '.format(termo), end= '')
    termo += razao
    cont += 1
print('FIM\)