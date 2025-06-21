
termo = int(input('Digite o primeiro termo: '))
rz = int(input('Digite a razao: '))
res = termo
#print('{}'.format(termo), end=' + ')
c = 1
while c < 10: 
    print('{}'.format(res), end=' + ')
    res += rz
    c += 1
print('{} ACABOU'.format(res), end=' ') 
