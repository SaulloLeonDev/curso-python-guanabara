lista = [[], []]
for c in range(1, 7):
    num = int(input(f'Digite o {c} valor: '))
    if num % 2 == 0:
        lista[0].append(num)    
    else:
        lista[1].append(num)       
lista[0].sort()
lista[1].sort()   
print(f'Os valores pares sao: {lista[0]}')
print(f'Os valores impares sao: {lista[1]}')

    
    