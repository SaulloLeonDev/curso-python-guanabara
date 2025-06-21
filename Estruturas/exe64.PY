p = int(input('[Digite 999 para parar]: '))
soma = p
cont = 1
while p != 999:
    soma += p
    cont += 1
    p = int(input('[Digite 999 para parar]: '))
print('voce digitou {} numeros e o  resultado da soma e {}!'.format(cont, soma))
    