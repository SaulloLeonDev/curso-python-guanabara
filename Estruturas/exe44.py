preco = float(input('Qual o valor: '))
print("""[1] A vista Dinheiro/cheque: 10% de Desconto \n [2] A vista no Cartao: 5% de desconto\n [3] Em ate 2x no Cartao: Preco normal\n [4] 3x ou mais: 20% de Juros""")
condicao = int(input('Qual a condicao: '))
if condicao == 1:
    valor = preco * 10 / 100
    total = preco - valor
    print('O valor de R$ {:.2f} vai ficar R$ {:.2f} com o desconto de 10%: '.format(preco, total))
elif condicao == 2:
    valor = preco * 5 / 100
    total = preco - valor
    print('O valor de R$ {:.2f} vai ficar R$ {:.2f} com o desconto de 5%: '.format(preco, total))
elif condicao == 3:
    print('Sem Dsecontos!')
elif condicao == 4:
    vezes = int(input('Quantas x no cartao: '))
    if vezes == 4 and 5 and 6 and 7:
        valor = preco / 100 * 20
        total = preco + valor
        print('O valor de R$ {:.2f} vai ficar {:.2f} com acrescimo de juros de 20%:'.format(preco, total))
else:
    print('invalido')
