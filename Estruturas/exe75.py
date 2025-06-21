cont = 0
cont9 = 0
valor = []
pares = []
lista = []
p = 0
while True:
    p = int(input('digite um numero: '))       
    if p == 9:
        cont9 += 1
    if p % 2 == 0:
        pares.append(p)
    valor.append(p)
    cont += 1
    if cont == 4:
        break               
par = tuple(pares)   
valor = tuple(valor)
numerada = []
for i, num in enumerate(valor, start = 1):
    if num == 3:
        numerada.append(i)          
print(f'voce digitou os valores {valor}')
print(f'O valor 9 apareceu {cont9} vezes')
print(f'O numero 3 foi encontrado na posicao {numerada}' if numerada != [] else 'O numero 3 nao foi encontrado' )
print(f'Os numeros pares digitados foram {par}' if par != () else 'Sem numeros pares Digitados')
    
    