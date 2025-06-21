from random import randint
print('=-=' * 20)
print('Vamos Jogar Par ou Impar')
print('=-=' * 20)
pc =  cont = soma = 0
while True:
    pc = randint(0, 10)
    jogador = int(input('Digite um valor: '))
    opcao = str(input('PAR OU IMPAR? [P/I]')).upper()[0]
    soma = pc + jogador
    if opcao == 'P' and soma % 2 == 0:
        print('voce ganhou')
        print(f'a soma foi {soma} PAR, pc foi {pc}, e voce jogou {jogador}')
        cont += 1
    if opcao == 'I' and soma % 2 == 1:
        print('voce ganhou')
        print(f'a soma foi {soma} IMPAR, pc foi {pc}, e voce jogou {jogador}')
        cont += 1
    if opcao == 'P' and soma % 2 == 1:
        print(f'{soma} IMPAR GAME OVER')
        break
    if opcao == 'I' and soma % 2 == 0:
        print(f'{soma} PAR  GAME OVER')
        break
print(f'voce ganhou {cont} x')
