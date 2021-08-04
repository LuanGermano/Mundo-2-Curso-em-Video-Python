# Faça um programa que jogue Par ou IMpar com o Computador. O Jogo só será interrompido quando o jogador PERDER
# mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.
from random import randint
pc = jog = cont = 0
esc = condi = ''
while True:
    esc = str(input('Escolha Par ou Impar: ')).lower().strip()
    while esc != 'par' and esc != 'impar':
        esc = str(input('Escolha ENTRE PAR OU IMPAR!: ')).lower().strip()
    jog = int(input('Digite um valor de 0 a 10: '))

    while jog > 10:
        jog = int(input('Digite um valor de ZERO E DEZ!: '))

    pc = randint(0, 10)
    jogada = jog + pc
    print(f'O computador jogou {pc} e A jogada deu {jogada} ')

    if jogada % 2 == 0 and esc == 'par':
        print('Você venceu! ')
        cont += 1
    elif jogada % 2 != 0 and esc == 'impar':
        print('Voce venceu! ')
        cont += 1
    else: # jogador perder
        condi = 'Derrota'
        print('Voce perdeu')
        break
if cont > 1:
    compl = 'es'
else:
    compl = ' '
print(f'Acabou o jogo e vc venceu {cont} vez{compl}')
