from datetime import date
contador_nascimento = 2
cont_maior = 0
cont_menor = 0
ano = date.today().year
for c in range(contador_nascimento):
    nasc = int(input('Digite seu ano de nascimento: '))
    i = (ano - nasc)
    if i <= 17:
        cont_menor += 1
    else:
        cont_maior += 1          
print('Ao todo tivemos {} pessoas maiores de idade'.format(cont_maior))
print('E tambem tivemos {} pessoas menores de idade'.format(cont_menor))
