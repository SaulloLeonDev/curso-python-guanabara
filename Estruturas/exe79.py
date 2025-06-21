lista = []
opcao = ''
while opcao != 'N':
    num = int(input(f'Digite um numero: '))
    if num in lista:
        print(f'numero ja existe')
    else:
        lista.append(num)
        print(f'adcionado com sucesso')
    opcao = str(input('Quer continuar? S/N: ')).upper()
    if opcao == 'N':
        break
print(f'Voce digitou os valore {sorted(lista)}')
