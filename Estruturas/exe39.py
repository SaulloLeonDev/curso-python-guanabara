from datetime import date
hoje = date.today().year
data = int(input('Digite seu ano de nascimento: ' ))
idade = hoje - data
print('Quem nasceu em {}, hoje em {} tem {} anos'.format(data, hoje, idade ))

if idade <= 17:
    saldo = 17 - idade
    anos = hoje - saldo
    print('voce ainda nao pode se alistar faltam {} anos'.format(saldo))
    print('Ainda faltam {} anos'.format(anos))
elif idade == 18: 
    print('esta na hora de se alistar')
elif idade >= 20:   
    saldo = idade - 20
    anos = hoje - saldo   
    print('passou do tempo foi em {}'.format(anos))
    print('Ja se passaram {} anos'.format(saldo))
