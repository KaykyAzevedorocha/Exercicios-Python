import random

lista1 = []
lista2 = []

for i in range(9):
    aleatorio = random.randint(1, 6)
    lista1.insert(i, aleatorio)
    aleatorio2 = random.randint(1, 6)
    lista2.insert(i, aleatorio2)
ultimo = int(input('digite o valor que deseja que seja inserido na lista: '))


lista1.append(ultimo)
lista2.append(ultimo)

print(lista1)
print(lista2)
concate = lista1 + lista2
print(concate)
lista1.sort()
print(lista1)
lista2.reverse()
print(lista2)