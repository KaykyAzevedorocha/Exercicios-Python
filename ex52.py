num= int(input('digite um número: '))
totdiv= 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end='')
        totdiv+=1
    else:
        print('\033[34m' , end='')
    print('{}'.format(c), end=' ')
print('\n\033[mO número foi dividido {} vezes'.format(totdiv))
if totdiv == 2:
    print('o número é primo')
else:
    print('O número não é primo')