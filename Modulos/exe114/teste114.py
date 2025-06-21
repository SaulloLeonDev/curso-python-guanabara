import requests

nome = 'freebit'
try:
    response = requests.get('https://freebitco.in/?op=home')
    response.raise_for_status()
    if response.status_code == 200:
        print(f'Site {nome} esta Online')
except:
    print(f'Site {nome} esta fora do ar')
finally:
    print(f'<< ATE MAIS >>')
    