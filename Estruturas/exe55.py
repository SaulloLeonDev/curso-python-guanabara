pesos =[]
for pessoa in range(1, 5):
    peso = float(input('{} peso: '.format(pessoa)))
    pesos.append(peso)
print('O maior peso foi {} KG e o menor foi {} KG'.format(max(pesos), min(pesos)))
