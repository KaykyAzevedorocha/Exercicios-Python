s = 0
c = 1
num = 0
while num != 999:
    num = int(input('digite o número: '))
    s += num
    if num == 999:
        c -= 1
        s -= 999
    else:
        c += 1
print('A soma dos números digitados é {} e foi digitado {} números'.format(s, c))