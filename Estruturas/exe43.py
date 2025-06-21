#idade = int(input('Digite a sua Idade: '))
peso = float(input('Digite seu Peso: '))
altura = float(input('Digite sua Altura: '))

imc = peso / (altura**2)
if imc < 18.5:
   print('Abaixo do peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 40:
    print('Obesidade')
else:
    print('obesidade Morbida')
print(imc)
