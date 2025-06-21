sexo = str(input(' Digite seu Sexo: ')).strip().lower()[0]
while sexo not in 'MmFf':
        sexo = str(input('Digite o sexo correto: ')).lower().strip()[0]
print('voce e {} e foi registrado'.format(sexo))

    