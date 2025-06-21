def voto(ano):
    from datetime import date
    hoje = date.today().year
    idade = hoje - ano
    if idade < 16:
        return f'Com {idade} anos. NAO VOTA.'
    elif idade > 18 and idade < 65:
        return f'Com {idade} anos. VOTO OBRIGATORIO.'
    else:
        return f'Com {idade} anos. VOTO OPCIONAL.'


# Programa Principal
nasc = int(input('Em que ano voce nasceu?: '))
print(voto(nasc))
