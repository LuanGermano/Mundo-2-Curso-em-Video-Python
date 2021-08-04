frase = str(input('Digite uma Frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
#para cada letra no Range, a gente ta pegando o valor total menos 1 pra corrigir; invertido; fazendo vir no caminho oposto.
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(f'O inverso de {junto} é {inverso}! ')
if inverso == junto:
    print('Temos um palindromo! ')
else:
    print('A frase digitada não é um palindromo ')