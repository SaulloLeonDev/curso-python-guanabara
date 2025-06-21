
termo = int(input('Digite o primeiro termo: '))
rz = int(input('Digite a razao: '))
res = termo + rz
#print('{}'.format(termo), end=' + ')
c = 1
contador = 0
while c <= 10: 
    print('{}'.format(res), end=' ')
    print(' → 'if c < 10 else ' ', end=' ' )
    res += rz
    c += 1
    contador += 1
termo2 = int(input('\nQuantos termos mais: '))
total = res
c = 1
if termo2 == 0:
    print('FIM')
else:
    while c <= termo2:
        total += termo2
        print('{}'.format(total), end=' ')
        print(' → 'if c < termo2 else ' ', end=' ')
        c += 1
        contador += 1
print('\nFinalizadas com {} progressoes'.format(contador))
print('FIM')
    