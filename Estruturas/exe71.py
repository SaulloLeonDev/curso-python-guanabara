from time import sleep
print('==' * 20)
print('{:^40}'.format('BANCO CENTRAL'))
print('==' * 20)
sleep(3)
saque = int(input('Qual valor que sacar? '))
nota100 = saque // 100
resto100 = saque % 100
nota50 = resto100 // 50
resto50 = resto100 % 50
nota20 = resto50 // 20
resto20 = resto50 % 20
nota10 = resto20 // 10
resto10 = resto20 % 10
nota1 = resto10 // 1
print(f'Com seu saque de R${saque} Voce vai receber...')
sleep(5)
if nota100 != 0:
    print(f'voce vai receber R${nota100} notas de cem')
if nota50 != 0:
    print(f'voce vai receber R${nota50} notas de cinquenta')
if nota20 != 0:
    print(f'voce vai receber R${nota20} notas de vinte')
if nota10 != 0:
    print(f'voce vai receber R${nota10} notas de dez')
if nota1 != 0:
    print(f'voce vai receber R${nota1} notas de 1')
sleep(7)
print('==' * 20)
print('BANCO CENTRAL!')
print('==' * 20)


