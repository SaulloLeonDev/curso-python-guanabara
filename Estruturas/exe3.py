casa = float(input('Digite o valor da casa: '))
salario = float(input('seu salario: '))
anos = int(input('quantos anos vai pagar: '))
prestacao = casa / (anos * 12) 
print('total da prestacao vai ser de R$ {:.2f}:  '.format(prestacao))

if salario < (prestacao / 0.3):
    print(' seu emprestimo foi negado!')
else:
    print('seu emprestimo foi liberado')
    
