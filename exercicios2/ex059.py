''' Crie um programa que leia dois valores e mostre um menu na tela:
[1] Somar
[2]multiplicar
[3]maior
[4]novos numeros
[5]sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
from math import prod
from cor import cores

comando = 4
while comando != 5:
    if comando == 4:
        val =[]
        for v in range(0, 2):
            valor = int(input('Digite um Valor: '))
            val += [valor]
    print('=-=' * 8)
    print(f'{cores["Bgre"]}Digite um Comando: \n[1]Somar \n[2]Multiplicar \n[3]Maior \n[4]Novos numeros \n[5]Sair do programa {cores["cle"]}')
    print('=-=' * 8)
    comando = int(input('Diga um comando: '))
    print('=-='*8)
    if comando == 1:
        soma = sum(val)
        print(f'{cores["Bblu"]}A soma dos valores {val[0]} e {val[1]} é de: {soma}{cores["cle"]} ')
        sleep(1)
    elif comando == 2:
        mult = prod(val)
        print(f'{cores["Bblu"]}A multiplicação dos valores {val[0]} e {val[1]} é de : {mult}{cores["cle"]} ')
        sleep(1)
    elif comando == 3:
        maior =max(val)
        if val[0] == val[1]:
            print(f'{cores["Bblu"]} Ambos numeros são iguais{cores["cle"]} ')
        else:
            print(f'{cores["Bblu"]}O maior numero entre {val[0]} e {val[1]} é o {maior}{cores["cle"]}')
        sleep(1)
    elif comando != 5 and comando != 4:
        print('Comando invalido')
print('O programa foi encerrado!')

