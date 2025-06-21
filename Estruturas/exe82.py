opcao = ''
lista = []
par = []
impar = []
while opcao != 'N':
    num = int(input('Digite um numero: '))
    lista.append(num) 
    opcao = str(input('Quer continuar? S/N: ')).upper()
    if opcao == 'N':
        break
for n in lista:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n) 
print(f'A lista completa e {lista}')
print(f'A lista par e {par}')
print(f'A lista impar e {impar}')