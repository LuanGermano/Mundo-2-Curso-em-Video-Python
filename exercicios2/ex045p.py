from random import randint
from time import sleep
itens = ('pedra','papel', 'tesoura')
computador = randint (0,2)
print('''Suas opçções
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('-=' * 11)
print('JO')
sleep(0.25)
print('KEN')
sleep(0.25)
print('PO')
sleep(0.25)
print('-=' * 11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[computador]}')
print('-=' * 11)
if computador == 0:
    if jogador == 0:
        print('EMPATE ')
    elif jogador == 1:
        print('JOgador Venceu ')
    elif jogador == 2:
        print('Computador Venceu ')
    else:
        print('Jogada Invalida ')
elif computador == 1:
    if jogador == 0:
        print('COmputador Venceu')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador Venceu ')
    else:
        print('Jogada invalida')
elif computador == 2:
    if jogador == 0:
        print('Jogador venceu')
    elif jogador == 1:
        print('Computador venceu')
    elif jogador == 2:
        print('Empate')
    else:
        print('Jogada Invalida')