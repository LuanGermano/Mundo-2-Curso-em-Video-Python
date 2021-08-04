# Crie um programa que simule o funcionamento de um caixa eletronico.
# No inicio, pergunte ao usuario qual sera o VALOR A SER SACADO (int)
# e o programa vai informar quantas celular de cada valor serão entregues
# OBS só nota de 50, 20, 10 e 1 real.
valor = int(input('Digite o Valor que será sacado: '))
ncin = nvin = ndez = n1um = 0

ncin = valor // 50
valor %= 50
nvin = valor // 20
valor %= 20
ndez = valor // 10
valor %= 10
n1um = valor // 1


prif ncin > 0:
    print(f" Serão {ncin} notas de 50 reais ")
if nvin > 0:
    print(f' Serão {nvin} notas de 20 reais ')
if ndez > 0:
    print(f' Serão {ndez} notas de 10 reais ')
if n1um > 0:
    print(f' Serão {n1um} notas de 1 real ')