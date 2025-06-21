def leiaInt(n):
    while True:
        try:
            n = int(input('Digite um numero: '))
        except:
                print('\033[0;31mErro! Dgite um numero inteiro valido.\033[m')
        else:
            return n
    
               
n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')      
