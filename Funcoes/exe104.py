def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\33[0;31mErro! Dgite um numero inteiro valido.\33[m')
        if ok:
            break
    return valor


# Porgrama Principal
n = leiaInt('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')
