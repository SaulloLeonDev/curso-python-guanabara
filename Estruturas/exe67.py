while True:
    n = int(input('Digite a tabuada:'))
    if n < 0:
        print('FIM')
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
