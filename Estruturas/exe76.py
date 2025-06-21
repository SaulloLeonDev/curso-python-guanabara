print('___' * 16)
print(f'{"Mercado Digital":^46}')
print('___' * 16)
tupla = ('Carro', 11.000, 'Moto', 7.500, 'Van', 6.000, 'Bike Eletrical', 120.00, 'Patins', 500)
for pos in range(0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<20}', end="")
    if pos % 2 == 1:
        print(f'R$ {tupla[pos]:.3f}')
