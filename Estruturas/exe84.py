temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    res = str(input('Quer continuar: [S/N]'))
    if res in 'N':
        break
print(f'Ao todo foram cadastrados {len(princ)} pessoas!')
print(f'O maior peso foi {mai}', end=' ')
for p in princ:
    if p[1] == mai:
        print(f'peso de [{p[0]}]', end=' ')
print()        
print(f'O menor peso foi {men}', end=' ')      
for p in princ:
    if p[1] == men:
       print(f'peso de [{p[0]}]', end=' ') 
