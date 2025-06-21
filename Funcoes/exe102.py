def fatorial(n, show=False):
    """Fatorial(n, show=False)
    -> Calcula o fatorial de um numero.
    :param n: O numero a ser calculado.
    :param show: (opcional) Mostrar ou nao a conta.
    :return: O valor do Fatorial de um  numero n.
    Desenvolvido por: Gustavo Guanabara 
    """
    f = 1
    for c in range(n, 0, - 1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

# Porgrama Principal
print(fatorial(5, show=True))
#help(fatorial)
