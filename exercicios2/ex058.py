# Melhore o jogo do Desafio 028 onde o computador vai "pensar" em um numero entre 0 e 10.
# só que agora o jogador vai tentar adivinhar até acertar.
#mostrando no final quantos palpites foram necessarios para vencer.
from random import randint
from time import sleep
tentativa = 0
sorteio = randint(0, 10)
jog = 0
while jog != sorteio:
    jog = int(input('Diga um numero de 0 a 10: '))
    tentativa += 1
    sleep(0.25)
    if jog != sorteio:
        print('Você errou, tente de novo!')
sleep(0.25)
print(f'Parabens, vc venceu com {tentativa} tentativas')