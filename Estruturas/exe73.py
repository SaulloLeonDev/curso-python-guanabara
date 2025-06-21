
times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo',
 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás', 'Bahia', 'Vasco', 'Atlético-MG',
'Fluminense', 'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print(f'=='* 20)
print(f'Os 5 primeiros sao: {times[0:5]}')
print(f'=='* 20)
print(f'Os ultimos 4 sao: {times[-4:]}')
print(f'=='* 65)
print(f'Times em orem alfabetica{sorted(times)}')
print(f'=='* 65)
print(f'Chapecoense esta na posicao {times.index("Chapecoense") + 1}')
print(f'=='* 20)
