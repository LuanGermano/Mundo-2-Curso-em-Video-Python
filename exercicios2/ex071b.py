# Crie um programa que simule o funcionamento de um caixa eletronico.
# No inicio, pergunte ao usuario qual sera o VALOR A SER SACADO (int)
# e o programa vai informar quantas celular de cada valor serão entregues
# OBS só nota de 50, 20, 10 e 1 real.
valor = int(input('Digite o Valor que será sacado: '))
ncin = nvin = ndez = n1um = 0

while True:
    while valor - 50 >= 0:
        valor -= 50
        ncin += 1
    while valor - 20 >= 0:
        valor -= 20
        nvin += 1
    while valor - 10 >= 0:
        valor -= 10
        ndez += 1
    while valor - 1 >= 0:
        valor -= 1
        n1um += 1
    break
if ncin > 0:
    print(f" Serão {ncin} notas de 50 reais ")
if nvin > 0:
    print(f' Serão {nvin} notas de 20 reais ')
if ndez > 0:
    print(f' Serão {ndez} notas de 10 reais ')
if n1um > 0:
    print(f' Serão {n1um} notas de 1 real ')
