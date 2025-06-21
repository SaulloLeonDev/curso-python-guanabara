from funcoes import moedas
p = float(input('Digite o preco:R$  '))
print(f'A metade de {moedas.moeda(p)} e {moedas.metade(p, True)}')
print(f'O dobro de {moedas.moeda(p)} e {moedas.dobro(p, True)}')
print(f'Aumentando 10%, temos {moedas.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moedas.diminuir(p, 13, True)}')