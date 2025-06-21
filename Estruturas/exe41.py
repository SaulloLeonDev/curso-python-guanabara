from datetime import date
ano = date.today().year
nasc = int(input('Digite seu ano de nascimento: ')) 
res = ano - nasc
if res <= 9:
    print('Voce esta na categoria Mirim {} anos'.format(res))
elif res <= 14:
    print('Voce esta na categoria Infantil {} anos'.format(res))
elif res <= 19:
    print('Voce esta na categoria Junior {} anos'.format(res))
elif res <= 25:
    print('Voce esta na categoria Senior {} anos'.format(res))
else:
    print('Voce esta na categoria Master {} anos'.format(res))
    