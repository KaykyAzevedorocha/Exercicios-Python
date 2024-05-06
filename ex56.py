s = 0
idadevelho = 0
nomevelho = ''
contador = 0
for p in range(1, 5):
    print("------ {}° PESSOA------".format(p))
    nome= str(input('qual seu nome: ')).strip()
    idade = int(input('qual sua idade: '))
    sexo = str(input('qual seu sexo [M/F]: ')).strip()
    s += idade
    if p == 1 and sexo in 'Mm':
        idadevelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > idadevelho:
        idadevelho = idade
        nomevelho= nome
    if idade < 20 and sexo in 'Ff':
        contador += 1
print('{} mulheres tem menos de 20 anos'.format(contador))
print('O homem mais velho tem {} anos e seu nome é {}'.format(idadevelho,nomevelho))

media = s/4
print('A média de idade do grupo é {}'.format(media))


