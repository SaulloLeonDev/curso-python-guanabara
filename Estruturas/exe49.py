num1 = int(input('Qual a tabuada: '))
num2 = int(input('Ate quantas vezes: '))

for num1 in range(num2 +1 ):
    res = num2 * num1
    print('{} x {} = {}'.format(num2, num1, res))
  