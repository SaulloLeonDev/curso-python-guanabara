def metade(n1=0):
    res = n1 / 2
    return res


def dobro(n1=0):
    res = n1 * 2
    return res


def aumentar(n1=0, n2=0):
    r = n1 + (n1 / 100 * n2)
    return  r


def diminuir(n1=0, n2=0):
    r = n1 - (n1 / 100 * n2)
    return  r


def moeda(n=0,):
    form = f'R$ {n:.2f}'.replace('.', ',')
    return form
