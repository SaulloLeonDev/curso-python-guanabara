from random import randint
from time import sleep
itens = ('Pedra' , 'Papel', 'Tesoura')
comp = randint(0, 2)
print(""" [0] Pedra\n [1] Papel\n [2] Tesoura\n """)
jogador = int(input('Sua Opcao: '))
print('JO')
sleep(1.5)
print('KEN')
sleep(1.5)
print('PO')
if jogador == 0:
    print('pedra')
    if comp == jogador:
        print('Computador: {}'.format(itens[comp]))
        print('Empate')
    elif comp == 1:
        print('Computador: {}'.format(itens[comp]))
        print('Voce Perdeu')
    elif comp == 2:
        print('Computador: {}'.format(itens[comp]))
        print('Voce ganhou')
elif jogador == 1:
    print('Papel')
    if comp == jogador:
        print('Computador: {}'.format(itens[comp]))
        print('Empate')
    elif comp == 0:
        print('Computador: {}'.format(itens[comp]))
        print('Voce Ganhou')
    elif comp == 2:
        print('Computador: {}').format(itens[comp])
        print('Voce Perdeu')   
elif jogador == 2:
    print('Tesoura')
    if comp == 2:
        print('Computador: {}'.format(itens[comp]))
        print('Empate')
    elif comp == 0:
        print('Computador: {}'.format(itens[comp]))
        print('Voce Perdeu')
    elif comp == 1:
        print('Computador: {}'.format(itens[comp]))
        print('Voce Ganhou')
else:
    print('Invalido')
