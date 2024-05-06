resp = 'S'
s = 0
cont = 0
maior = 0
menor = 0
while resp in 'Ss':
    num = float(input('digite o numero'))
    cont += 1
    s += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('quer continuar?'))
media = s/cont


print('O maior numéro é {}'.format(maior))
print('O menor numéro é {}'.format(menor))
print('a média é {}'.format(media))

