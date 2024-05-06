contidade = conthomens = contmulher = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Digite a idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    continuar = str(input('Quer continuar: [S/N] ')).strip().upper()[0]
    if idade > 18:
        contidade += 1
    if sexo == 'M':
        conthomens += 1
    if sexo == 'F' and idade < 20:
        contmulher += 1
    if continuar == 'N':
        break
print(f'A {contidade} pessoas maiores de 18 anos')
print(f'A {conthomens} homens cadastrados no sistema')
print(f'A {contmulher} mulheres menores de 20 anos')