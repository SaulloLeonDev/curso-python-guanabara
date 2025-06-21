n1 = float(input('Primeiro Segmento: '))
n2 = float(input('Segundo Segmento: '))
n3 = float(input('Terceiro Segmento: '))


if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Formam um triangulo!', end=' ')
    if n1 == n2 == n3:
        print('Equilatero')
    elif n1 != n2 != n3 != n1:
        print('Escaleno')
    else:
        print('Isosceles')
else:
    print('Nao formam um triangulo!')


