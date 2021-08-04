# Faça um programa que leia o peso de Cinco pessoas, no final, mostre qual foi o Maior e menor peso lidos.
list = [] #lista vazia
num = int(input('Qual o numero de pessoas: '))
for n in range(0, num):
    peso = float(input(f'Digite o {n+1}º peso: '))
    list += [peso] # enchendo a lista
print(f'Na sua lista de {num} pessoas, o maior peso entre elas é o de {max(list)}Kg e o de menor é o {min(list)}Kg ')

