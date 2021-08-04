# faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo.
num = int(input('Digite um Numero: '))
# um numero é primo qnd é divisivel somente por si mesmo e 1

for c in range(2, num):
    if num % c == 0:
        print(f'o seu numero {num} n é primo! ')
        break
else:
    print('O numero digitado é primo')
