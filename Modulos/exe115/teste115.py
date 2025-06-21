from cadastro import pessoas
while True:
    print('-' *40)
    print(f'{"MENU PRINCIPAL":^40}')
    print('-' *40)
    print("""
    1 - Ver pessoas cadastradas
    2 - Cadastras nova Pessoa
    3 - Sair do sistema  """)
    print('-' *40)
    opcao = int(input('Sua Opcao:'))
    if opcao == 1:
        pessoas.cadastros()
    if opcao == 2:
        pessoas.cadastrar()
    if opcao == 3:
        print('-' *40)
        print(f'Obrigado e Volte sempre')
        print('-' *40)
        break
