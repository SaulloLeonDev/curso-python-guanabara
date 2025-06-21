lista = list()
cad = dict()
def cadastrar():
    print('-' *40)
    print(f'{"NOVO CADASTRO":^40}')
    print('-' *40)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    cad['nome'] = nome
    cad['idade'] = idade
    print(f'Novo registro de {cad['nome']} adcionado.' )
    return lista.append(cad.copy())

def cadastros():
    for v in lista:
        print(f'{v['nome']:<5} {v['idade']:>8}')
    


    