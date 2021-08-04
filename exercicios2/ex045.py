#Crie um programa que faça o computador jogar Jokepo com voce
from random import randint
from time import sleep

jog = str(input('Diga sua Jogada: ')).lower().strip()
pc = randint(0,2)
if jog == 'pedra' and pc == 0 or jog == 'tesoura' and pc == 1 or jog == 'papel' and pc == 2:
    caso = 'Voces empataram'
elif jog == 'pedra' and pc == 2 or jog == 'tesoura' and pc == 0 or jog == 'papel' and pc == 1:
    caso ='Voce perdeu'
elif jog == 'pedra' and pc == 1 or jog == 'tesoura' and pc == 2 or jog == 'papel' and pc == 0:
    caso = 'Voce venceu!'
else:
    print("Jogada Invalida!!")
    exit()

pc = str(pc)

if pc == "0":
    pc = "Pedra"
elif pc == '1':
    pc = "Tesoura"
elif pc == '2':
    pc = 'papel'
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(0.25)
print(f'O Pc jogou {pc} e vc jogou {jog} logo {caso}')
