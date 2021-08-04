# Faça um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario.
# O programa será interrompido quando o numero solicitado for negativo.

num = int(input('Diga um numero que vc deseja ver a tabuada: '))
while num > 0:
    print('-=-' * 12 )
    for n in range(1, 11):
        tab = num * n
        print(f'{num} x {n} = {tab} ')
    print('-=-' * 12)
    num = int(input('Deseja saber de outro Numero? se não digite um valor negativo: '))
print('Encerrando programa')