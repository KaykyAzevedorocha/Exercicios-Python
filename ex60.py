n = int(input('digite um número para descobrir o fatorial: '))
c = n
f = 1

while c > 0:
    f*= c
    c-= 1
print(f)