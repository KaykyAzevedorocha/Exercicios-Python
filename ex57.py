sexo = str(input('digite seu sexo [M/F]: ')).upper().strip()[0]
while not sexo in 'MF':
    sexo = str(input('-----dados invalidos----\ndigite seu sexo novamente:')).upper().strip()[0]
print('sexo {} registrado com sucesso'.format(sexo))
