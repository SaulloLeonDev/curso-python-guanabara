maior = menor = cont = soma = num1 = num2 = 0
opcao = 'Y'
while opcao == 'Y':
    cont += 1
    num = int(input('Digite um numero: '))
    if num > maior:
        maior = num
    if num < maior:
        menor = num
    opcao = str(input('quer continuar Y/N: ')).upper().strip()[0]
    soma += num

media = soma / cont  
print('Voce digitou {} numeros  e a media e {:.4f}'.format(cont, media))
print('a soma foi {}'.format(soma), end=' ')
print(' \nO maior numero foi {} e o menor numero foi {}'.format(maior, menor))
 