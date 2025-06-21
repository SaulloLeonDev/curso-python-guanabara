num1 = int(input('Primeiro numero: '))
num2 = int(input('Segundo numero: '))
print('==' *12)
print("""[1] somar\n[2] multiplicar\n[3] maior\n[4] novos numeros\n[5] sair do programa """)
print('==' *12)
opcao = int(input('Qual sua opcao: '))
soma = num1 + num2
mult = num1 * num2
sair = False

while not  sair:
    if opcao == 1:
        print('O resultado e {} '.format(soma))
        print('==' *20)
        print('==' *20)
        print("""[1] somar\n[2] multiplicar\n[3] maior\n[4] novos numeros\n[5] sair do programa """)
        print('==' *20)
        opcao = int(input('Qual sua opcao: '))
        print('==' *20)
    elif opcao == 2:
            print('O resultado e {}'.format(mult))
            print('==' *20)
            print("""[1] somar\n[2] multiplicar\n[3] maior\n[4] novos numeros\n[5] sair do programa """)
            print('==' *20)
            opcao = int(input('Qual sua opcao: '))    
            print('==' *20)
    elif opcao == 3:
            if num1 > num2:
                print('Esse aqui e o maior {}: '.format(num1))
                print('==' *20)
                opcao = int(input('Qual sua opcao: '))
            elif num1 < num2:
                print('Esse aqui e o maior {}: '.format(num2))
                print('==' *20)
                opcao = int(input('Qual sua opcao: '))
            elif num1 == num2:
                print('os numeros tem o mesmo valor')
                print('==' *20)
                print("""[1] somar\n[2] multiplicar\n[3] maior\n[4] novos numeros\n[5] sair do programa """)
                print('==' *20)  
                opcao = int(input('Qual sua opcao: ')) 
    elif opcao == 4:
        num3 = int(input('Primeiro numero: '))
        num4 = int(input('Segundo numero: '))
        print("""[1] somar\n[2] multiplicar\n[3] maior\n[4] novos numeros\n[5] sair do programa """)
        opcao = int(input('Qual sua opcao: '))
        print('==' *12)
        if opcao == 1:
            res = num3 + num4
            print('O resultao e {}'.format(res))
            opcao = int(input('Qual sua opcao: '))
        elif opcao == 2:
            res = num3 + num4
            print('O resultao e {}'.format(res))
            opcao = int(input('Qual sua opcao: '))                 
    if opcao == 5:
        print('FIM')
        sair = True
print('FECHOU')
      