def maior(*num):
    print('-=' * 20)
    print('Analisando os valores passados...')
    for i, v in enumerate(num, start=1):
        print(f'{v} ', end=' ')
    print(f'Foram iformados {len(num)} valores ao todo.', end=' ')
    print(f'\nO maior valor informado foi {max(num)}' if len(num) > 0 else '\nO maior valor informado foi 0')
 
    
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
