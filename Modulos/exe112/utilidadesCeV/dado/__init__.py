def leiaDinheiro(num):
    while True:
        try:
            n = float(input('Digite o preco:R$  '))
            return n
        except ValueError:
            print('ERRO! Digite um numero inteiro:') 
           
           
def leiadin(msg):
    valido = False
    while not valido:
        entrada = str(input('Digite um um preco: ')).replace(',', '.').strip().upper()
        if entrada.isalpha() or entrada == '':
            print(f'\33[0;31mERRO! \"{entrada}\" \033[mE um preco invalido!')
        else:
            valido = True
            return float(entrada)
          