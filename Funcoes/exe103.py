def ficha(jog='<desconhecido', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


# Programa Principal
n = str(input('Nome do Jogador: '))
g = str(input('Numero de Gols: '))
if g.snumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
