pos = 0 
numero = list()
cont = 0
opcao = ''
while opcao != 'N':
    num = int(input('Digite um numero: '))
    cont += 1
    numero.append(num)
    opcao = str(input('Quer continuar? S/N: ')).upper()
    if opcao == 'N':
        break
numero.sort(reverse = True)
print(F'Voce digitou {cont} elementos.')
print(F'Os valores em oredem decrescente sao: {numero}')
print(F'O numero 5 foi digitado' if 5 in numero else 'O numero 5 nao foi digitado')
