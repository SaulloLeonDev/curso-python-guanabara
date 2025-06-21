

mais = int(input('Quantos termos:'))
cont = 1
n1 = 0
n2 = 1
sum = 0
while cont  <= mais :
    n1 = n2
    n2 = sum
    sum = n1 + n2  
    print('{} → '.format(sum), end='')
    cont += 1
print('FIM')
