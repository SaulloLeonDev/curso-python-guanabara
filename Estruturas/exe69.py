
print('_' * 13)
print('CADASTRE UMA PESSOA')
print('_' * 13)
sexo = ''
idade = contm = contf = maior = menor = 0
opcao ='S'
while opcao != 'N':
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]')).upper().split()[0]
    opcao = str(input('Quer continuar? [S/N]')).upper().split()[0]
    if sexo == 'M':
        contm += 1
    else:
        contf += 1
    if idade <= 18:
        if sexo == 'F':
            menor += 1
    elif idade >= 18:
        maior +=1
print(f'Total de pessoas com mais de 18 anos {maior}')
print(f'Ao todo sao {contm} homens cadastrados!')
print(f'e temos {menor} mulheres com menos de 20 anos!')
