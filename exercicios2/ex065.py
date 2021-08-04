"""Crie um programa que leia vários numeros inteiros pelo teclado. No final da execução, mostre a media
entre todos os valores e qual foi o maior e menor valores lidos. O programa deve perguntar ao usuario
se ele quer ou não CONTINUAR a digitar valores."""

num = int(input('Digite um Numero inteiro: '))
med = [num]
passa = ' '
while passa not in 'Nn':
    out = int(input('Digite outro numero: '))
    med += [out]
    passa = str(input('Deseja continuar?[S/N] '))
quantidade = len(med)
media = sum(med) / quantidade
print(f'A quantidade de valores digitados é de {quantidade} ')
print(f'A media dos valores é de {media} ')
print(f'O Maior valor dentro dos digitados é o de {max(med)} e o menor é o {min(med)} ')
