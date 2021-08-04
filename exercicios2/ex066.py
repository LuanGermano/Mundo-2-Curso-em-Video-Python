# Crie um programa que leia VARIOS NUMEROS inteiros pelo teclado. O programa só vai parar quando o usuario digitar 999.
# No final, mostre quantos numeros foram digitados e qual foi a soma entre eles (sem o Flag)

num = 0
soma = []
while True:
    num = int(input('Digite um valor: '))
    if num == 999:
        break
    soma.append(num)
print(f'A quantidade de Numeros foi {len(soma)} e a soma deles é {sum(soma)} ')
