# Refaça o Desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado:
# -Equilatero: Todos os lados iguais.
# -isósceles: dois lados iguais.
# - Escaleno: todos os lados diferentes.
l1 = float(input('Digite o valor do Primeiro lado: '))
l2 = float(input('Digite o valor do segundo lado: '))
l3 = float(input('Digite o valor do Terceiro lado: '))

if (l2 + l3) > l1 > (l2 - l3) and (l1 + l3) > l2 > (l1 - l3) and (l1 + l2) > l3 > (l1 - l3):
    possib = 1
else:
    possib = 0

if l1 == l2 == l3:
    tri = 'Equilatero'
elif l1 == l2 or l2 == l3:
    tri = 'Isósceles'
else:
    tri = 'Escaleno'

if possib == 0:
    print(f'O triangulo é possível de ser formado e tem a propriedade de ser um triangulo {tri}')
else:
    print('Com os lados informados não será possivel a formação de um triangulo.')
