def area(larg, comp):
    a = larg * comp
    print(f'A area de um terreno {larg} x {comp} e de {a} m2.')

# Programa Principal
print('Controle de terrenos')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)