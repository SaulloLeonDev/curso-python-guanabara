from math import factorial
from time import sleep
n = int(input('Digite um numero para saber seu fatorial: '))
#fat = factorial(n)
c = n
f = 1
print(' Calculando....')
sleep(3)
print('{}!'.format(n), end=' ')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f), end='')
