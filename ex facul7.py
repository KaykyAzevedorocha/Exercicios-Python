import random
lista = []
for i in range(20):
    aleatorio = random.randint(0,9)
    lista.insert(i, aleatorio)
tenta = int(input('chute um número: '))
contagem = lista.count(tenta)
print(lista)
print('vc acertou o número {} vezes parabens'.format(contagem))
