def metade(n1=0, sit=False):
    res = n1 / 2
    if sit == True:
        r = moeda(res)
        return r
    else:
        return res


def dobro(n1=0, sit=False):
    res = n1 * 2
    if sit == True:
        r = moeda(res)
        return r
    else:
        return res


def aumentar(n1=0, n2=0, sit=False):
    res = n1 + (n1 / 100 * n2)
    if sit == True:
        r = moeda(res)
        return r
    else:
        return res


def diminuir(n1=0, n2=0, sit=False):
    res = n1 - (n1 / 100 * n2)
    if sit == True:
        r = moeda(res)
        return r
    else:
        return res


def moeda(n=0,):
    res = f'R$ {n:.2f}'.replace('.', ',')
    return res


def resumo(n, n1, n2):
    print('-' *40)
    print('RESUMO DO VALOR')
    print('-' *40)
    print(f'Preco analisado: \t{moeda(n,)}')
    print(f'O dobro do preco: \t{dobro(n, True)}')
    print(f'Metade do preco: \t{metade(n, True)}')
    print(f'{n1}% de aumento: \t{aumentar(n, n1, True)}')
    print(f'{n2}% de reducao: \t{diminuir(n, n2, True)}')
    print('-' *40)
   