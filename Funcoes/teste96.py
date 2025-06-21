def multiplica(a, b):
    res = a * b
    print(f'A area de um terreno {a} x {b} e de {res} m2.')


print('Controle de terrenos')
print('---' * 8)
a = float(input('LARGURA (m): '))
b = float(input('COMPRIMENTO (m): '))
multiplica(a, b)
