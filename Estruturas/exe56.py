somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
contador = 0
menoridade = 0
for pessoa in range(1, 5):
    print('----- {} pessoa -----'.format(pessoa)) 
    nome = str(input('nome da {} pessoa: '.format(pessoa))).strip().lower()
    idade = int(input('idade da {} pessoa: '.format(pessoa)))
    sexo = str(input('M/F: ')).strip().lower()
    somaidade += idade
    if pessoa == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        contador += 1
           

mediaidade = somaidade / 2

print('a media do grupo e {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {} '.format(maioridadehomem, nomevelho))
print('total de mulheres menor que 20 anos: {}'.format(contador))    

