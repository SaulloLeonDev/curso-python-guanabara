def ficha(nome, gol):
    if nome == '':
        nome = '<desconhecido>'
    if gol.isnumeric():
        gol = int(gol)
        print(f'O jogador {nome} fez {gol} gol(s) no campeonato')
    else:
        gol = 0
        print(f'O jogador {nome} fez {gol} gol(s) no campeonato')
    
    
nome = str(input('Nome do jogador: '))
gols = str(input('Numero de gols: '))
ficha(nome, gols)  
    