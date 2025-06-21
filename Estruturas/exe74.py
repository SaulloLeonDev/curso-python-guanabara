from random import randint
cont = 0
sort = []
while cont < 10:
    num = randint(0 , 20)
    sort.append(num)
    cont += 1
sorteador = tuple(sort)
print(f'{sorteador}')
print(f'O menor foi {min(sorteador)}')
print(f'O maior foi {max(sorteador)}')
