# Crie um programa que leia uma frase qualquer
# e diga se ela é um PALINDROMO, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).lower().strip()
f1 =frase[::-1]
sf1 = frase.split()
sf2 = f1.split()
jf1 = ''.join(sf1)
jf2 = ''.join(sf2)
print(f'A frase {jf1} vira {jf2}')
if jf1 == jf2:
    print('É um palindromo!')
else:
    print('Não é um Palindromo')
