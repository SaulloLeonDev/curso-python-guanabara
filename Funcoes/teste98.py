from time import sleep
def cont(a, b, c):
    print('-=' * 15)
    print(f'Contagem de {a} ate {b} de {c} em {c}')
    if a > b:
        for i in range(a, b - 1, -c):
            print(f'{i}', end=' ', flush=True)
            sleep(0.5)
    else: 
        for i in range(a, b + 1, c):
            print(f'{i}', end=' ', flush=True)
            sleep(0.5)         
    print('FIM!')
    

cont(1, 10, 1)
cont(10, 0, 2)
print('-=' * 15)
print('Agora e sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
cont(ini, fim, passo)
print()
print('<<< PROGRAMA ENCERRADO >>>')
