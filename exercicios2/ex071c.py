# Crie um programa que simule o funcionamento de um caixa eletronico.
# No inicio, pergunte ao usuario qual sera o VALOR A SER SACADO (int)
# e o programa vai informar quantas celular de cada valor serão entregues
# OBS só nota de 50, 20, 10 e 1 real.

valorSaque = int(input('Valor do saque: R$ '))
print('-' * 40)
for nota in [50, 20, 10, 1]:
    quantidade = valorSaque // nota
    valorSaque = valorSaque % nota
    if quantidade > 0:
        print(f'{quantidade} notas de R$ {nota}')