def ajuda(msg):
    while msg != 'fim':
        msg = str(input('Funcao ou Biblioteca > ')).lower()
        print('~' * 40)
        print(f'Acessando o manual do comando {msg.upper()}')
        print('~' * 40)
        print(f'{help(msg)}')
    return msg   
print('~' * 40)
print('\033[0;31MAJUDA PY HELP\033[m')
print('~' * 40)
msg = ajuda('Funcao ou Biblioteca > ')
