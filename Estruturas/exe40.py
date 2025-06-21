nota1 = float(input('Pimeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2 
if media <= 5:
    print('sua media foi {} reprovado!'.format(media))
elif media >= 7:
    print('Sua media foi {} Aprovado'.format(media))
else:
    print('Sua media foi {} recuperacao!'.format(media))
