from funcoes import moedas

p = float(input('Digite o preco:R$  '))
print(f'A metade de {moedas.moeda(p)} e {moedas.metade(p)}')
print(f'O dobro de {moedas.moeda(p)} e {moedas.dobro(p)}')
print(f'Aumentando 10%, temos {moedas.moeda(moedas.aumentar(p, 10))}')
print(f'Reduzindo 13%, temos {moedas.moeda(moedas.diminuir(p, 13))}')
