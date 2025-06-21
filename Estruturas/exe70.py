print('--' * 12)
print('LOJA SUPER BARATAO')
print('--' * 12)
soma = cont = maior = menor = 0
produto = ''
while True:    
    nome = str(input('Nome do produto: '))
    valor = int(input('Preco:R$ '))
    cont += 1
    if valor > 1000:
        maior += 1        
    if cont == 1 or valor < menor:
        menor = valor
        produto = nome
    soma += valor
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N]')).upper().split()[0]
    if opcao == 'N':
        break      
print(f'O total da compra foi {soma}')
print(f'Temos {maior} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {produto}  custando R${menor:.2f}')
     