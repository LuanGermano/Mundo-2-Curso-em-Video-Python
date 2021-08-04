# Faça um programa que leia um numero qualquer e mostre seu 'FATORIAL'
# ex: 5! =5x4x3x2x1 = 120
'''num = int(input('Digite um Valor: '))
cont = num
fact = 1
print(f'O valor {num}! será de ', end='')
while cont > 0:
    print(f'{cont}', end='')
    print(f' x' if cont > 1 else '=', end=' ')
    fact *= cont
    cont -= 1
print(fact)'''
fact = 1
n = int(input('Diga um valor: '))
print(f'O calculo de {n}! é de:')
for c in range(n, 0, -1):
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ', end='')
    fact *= c
print(fact)
