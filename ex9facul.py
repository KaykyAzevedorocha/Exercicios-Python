lista = ['ana', 'julia','kaio','luan','flavio','gustavo','davinci','daniel','rafael','hariel']
print(lista)


remover = str(input('digite o nome que deseja excluir da lista: '))
lista.remove(remover)
print('O nome {} ja foi removido da lista pode olhar'.format(remover))
print(lista)