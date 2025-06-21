lista = []
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > lista[-1]:
        print('Adcionado ao final da lista')
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                print(f'Adcionado na posicao  {pos} da lista...')
                lista.insert(pos, num)
                break
            pos += 1
print(f'{lista}')
