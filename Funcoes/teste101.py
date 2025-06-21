def voto(num):
    from datetime import date
    hoje = date.today().year
    idade = hoje - num
    if idade < 16:
        print(f'Com {idade} anos. NAO VOTA.')
    if idade > 18 and idade < 65:
        print(f'Com {idade} anos. VOTO OBRIGATORIO.')
    else:
        print(f'Com {idade} anos. VOTO OPCIONAL.')

ano = int(input('Em que ano voce nasceu?: '))
voto(ano)
