# faça um programa que calcule a soma entre todos os numeros impares que são multiplos de 3 e se encontrem
# no intervalo de 1 ate 500.
soma = 0
cont = 0
f = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print(f'a soma de todos os numeros dará {soma} com {cont} valores ')
# ce podia ter usado o 6
for b in range(3, 501, 6):
    f += b
print(f)
