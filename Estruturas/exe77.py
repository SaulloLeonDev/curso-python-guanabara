batman = (
    "Batman", "Bruce", "Wayne", "Gotham", "Coringa", "Alfred", "Robin", "Batmovel",
    "Espantalho", "Charada", "Pinguim", "Duas-Caras", "Mulher-Gato", "Bane", "Asilo",
    "Arkham", "Capuz", "Morcego", "Noite", "Justiça"
)
vogais = ('A', 'E', 'I', 'O', 'U')
palavras = tuple(palavra.upper() for palavra in batman)
for palavra in palavras:
    vogal = {letra for letra in palavra if letra in vogais}
    print(f'palavra {palavra}: {vogal}')

