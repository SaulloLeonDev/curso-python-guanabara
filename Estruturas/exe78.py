valor = []
for cont in range(0, 5):
    valor.append(int(input(f'Digite um valor para a posicao {cont}: ')))
maior = max(valor)
menor = min(valor)
posmaior = []
posmenor = []
for pos , item in enumerate(valor):
    if maior == item:
        posmaior.append(pos)
    if menor == item:
        posmenor.append(pos)
print(f'Voce digitou os valores {valor}')
print(f'O maior valor foi {maior} na posicao {posmaior}')
print(f'O menor valor foi {menor} na posicao {posmenor}')
