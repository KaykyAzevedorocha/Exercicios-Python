lista = []

for c in range(1,6):
    peso = float(input('digite o {}° peso: '.format(c)))
    lista.insert(c, peso)
maximo= max(lista)
minimo = min(lista)
print('O menor peso é {}, e o maior é {}'.format(maximo,minimo))