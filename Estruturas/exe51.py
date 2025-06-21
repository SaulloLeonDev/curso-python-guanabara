
termo1 = int(input('Primeiro termo: '))
rz = int(input('Razao: '))
decimo = termo1 + (10 - 1) * rz
for c in range(termo1, decimo + rz , rz):
    print(c , end='-')
print('ACABOU')