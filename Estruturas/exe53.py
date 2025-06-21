nome = input('digite seu nome: ')
print('\n',nome)
nome = nome.lower().replace(" ","").replace(",","").replace(".","")
inv ="".join(reversed(nome))
if nome == inv:
    print('\n Nome Palindromo {}'.format(inv))
else:
    print('Palavra nao e Palindromo'.format(inv))
