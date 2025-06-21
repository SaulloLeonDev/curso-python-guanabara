fechado = aberto = cont = 0
exp = str(input('Digite sua expressao: '))
for item in exp:
    if exp == '(':
        aberto += 1
    if exp == ')':
        fechado += 1
    if aberto == fechado:
        cont += 1
print(f'expressao valida {exp}' if cont == 1 else f'expressao invalida {exp}')
