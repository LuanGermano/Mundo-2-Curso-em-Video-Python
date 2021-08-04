# Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem PARES.
# Se o valor digitado for IMPAR, desconsidere-o
soma = 0
cont = 0
for n in range(1, 7):
    n = int(input('Digite um Valor inteiro: '))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print(f'A soma dos {cont} valores pares informado é {soma} ')
