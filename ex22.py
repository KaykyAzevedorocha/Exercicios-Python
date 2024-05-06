nome = str(input('digite o seu nome ')).strip()
print('analizando seu nome...'.capitalize())
print('seu nome em letras maisculas fica assim: {}'.capitalize().format(nome.upper()))
print('seu nome em letras minusculas fica assim: {}'.capitalize().format(nome.lower()))
div = nome.split()
junta = ''.join(div).__len__()
print('seu nome tem {} letras'.format(junta))
prim= div[0].__len__()
print('seu primeiro nome te {} letras'.format(prim))


