lista = []
soma = 0
for n in range(6):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        lista.append(num)
        soma += num
print('A soma dos numeros pares sao {}'.format(soma))        
print('os numeros sao:{}'.format(lista))


        
