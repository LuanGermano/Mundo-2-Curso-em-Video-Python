#Refaça o desafio 009, mostrando a tabuada de um numero que o usuario escolher, só q com laço.

num = int(input('Digite um valor: '))
lim =int(input('Sua Tabuada será de 1 até: '))
print(f'a Tabuada do seu numero escolhido é a de:')
print('-=' *12)
for n in range(1, lim+1):
    tab = num * n
    print(f'{num} x {n} =',tab)
print('-=' *12)