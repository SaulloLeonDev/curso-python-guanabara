def factorial(n, show=True):
    """Fatorial(n, show=False)
    -> Calcula o fatorial de um numero.
    :param n: O numero a ser calculado.
    :param show: (opcional) Mostrar ou nao a conta.
    :return: O valor do Fatorial de um  numero n.
    Desenvolvido por: Saullo Dev 
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show==True:
                while n > 1:
                    print(f'{n}', end=' x ')
                    break
                if n == 1:
                    print(f'{n}', end=' = ')
                n -=1                       
    return f
n = int(input('digite um numero:'))
print(factorial(n, show=True))
