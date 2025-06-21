numero = int(input('Digite um numero inteiro: '))
print('voce digitou {} !'.format(numero))
print(' Qaual base quer converter: ')
print('[1] converter para binario')
print('[2] converter para octal')
print('[3] converter para hexadecimal')
opcao = int(input('Sua Opcao: '))
b = bin(numero)
o = oct(numero)
h = hex(numero)
if opcao == 1:
    print('Em binario {}'.format(b))
elif opcao == 2:
    print('Seu Numero em octal e {}'.format(o))
elif opcao == 3:
    print('Seu Numero em Hexadecimal e {}'.format(h))
else:
    print('numero invalido!')

    