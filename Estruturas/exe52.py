num = int(input('digite um numero: '))
count = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='') #amarelo divisivel 
        count += 1
    else:
        print('\033[31m', end='') # vermelho nao divisivel 
    print('{}'.format(c), end='')
print('\n\033[m O numero {} foi divisivel {} vezes '.format(num, count), end=' ')
if count == 2:
    print('\n Ele e numero Primo')
else:
    print('\n Ele nao e numero Primo!')

