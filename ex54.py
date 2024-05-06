from datetime import date
contmaior = 0
contmenor = 0
atual = date.today().year
for c in range(7):
    nasc = int(input('qual sua data de nascimento'))
    idade = atual - nasc

    if idade >= 18:
        contmaior += 1
    else:
        contmenor += 1

print('{} são maiores de idade, e {} são menores de idade'.format(contmaior,contmenor))