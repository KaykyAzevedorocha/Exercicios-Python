s= 0
cont = 0
for c in range(0,7):
    num= int(input('digite o número'))
    if num % 2 == 0 :
        s = s+num
        cont= cont+1
print('esses {} a soma é {}'.format(cont,s))
