from random import randint
print('-' * 5 , 'Sou seu computador e estou pensando um pouco......', '-' * 5)
print('acabei de pensar eum um numero de 0 a 10.\n Sera que consegue acertar? voce tera apenas 4 chances')
pc = randint(0, 10)
cont = 0
eu = int(input('Arrisque-se: '))
while eu != pc:
    print('ERROU')
    eu = int(input('Arrisque-se: '))
    cont += 1  
    if eu == pc:
        cont += 1
        print('Acerotu mizeravi com {} tentativa '.format(cont)) 
    elif cont >= 2:
        print('Acabou suas chances o numero era {}'.format(pc))      
print('Parabens Acertou mizeravi')
