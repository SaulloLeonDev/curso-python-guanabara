from random import randint
from time import sleep


def sorteio(*num):
    print(f'sorteando 5 valores:', end='')
    for v in num:
        print(f'{v}',end=' ', flush=True)
        sleep(1)
    print('PRONTO!')


def somaPar(*num):
    tot = 0
    for v in lista:
        if v % 2 == 0:
            tot += v
    print(f'somando os valores {lista} temos {tot}')


lista = []
cont = 1
while cont <= 5:
    v = randint(0, 20)
    if v not in lista:
        lista.append(v)
        cont += 1
    else:
        lista.append(v)
        cont += 1
sorteio(*lista)
somaPar(*lista)
