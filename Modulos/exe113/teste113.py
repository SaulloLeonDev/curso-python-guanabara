def leiaInt(n):
    ok = False
    while True:
        try:
            n = int(input('Digite um Inteiro: '))
            ok = True
        except (ValueError, TypeError):
            print(f'\33[0;31mErro! Dgite um numero inteiro valido.\33[m')
            continue
        except KeyboardInterrupt:
            print('O usuario preferiu nao informar valor')
            n = 0
            break
        if ok:
            break
    return n


def leiaReal(n):
    ok = False
    while True:
        try:
            n = float(input('Digite um numero Real: '))
            ok = True
        except (ValueError, TypeError):
            print(f'\33[0;31mErro! Dgite um numero Real valido.\33[m')
            continue
        except KeyboardInterrupt:
            print('O usuario preferiu nao informar valor')
            n = 0
            break
        if ok:
            break
    return n


# Porgrama Principal
inteiro = leiaInt('Digite um Inteiro: ')
real = leiaReal('Digite real: ')

print(f'o valor inteiro {inteiro} e o valor real {real}')

