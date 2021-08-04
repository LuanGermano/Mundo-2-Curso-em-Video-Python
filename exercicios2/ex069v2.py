# Crie um programa que leia a IDADE e o SEXO de varias pessoas.
# A cada pessoa cadastrada, o programa devera perguntar se quer ou não continuar.
# no final mostre:
# A) pessoas maiores de 18
# B) Quantos Homens foram cadastrados.
# C) quantas mulheres tem menos de 20

idade = []
sexo = []
idadef = []
idadem = []
continuar = 'S'

while continuar == 'S':
    idad = int(input('Digite a idade: '))
    idade.append(idad)

    sx = str(input('Digite o Sexo[M/F]: ')).upper().strip()
    while sx not in 'MF':
        sx = str(input('Por favor digite seu Sexo[M/F]: ')).upper().strip()
    sexo.append(sx)
    if sx == 'F':
        idadef.append(idad)
    elif sx == 'M':
        idadem.append(idad)

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar a operação [S/N]: ')).upper().strip()
        if continuar == 'N':
            break

idade18 = [num for num in idade if num < 18]
mulher20 = [num for num in idadef if num < 20]

print(f'a) Existem {len(idade18)} pessoas maiores de 18 anos.')
print(f'b) Foram cadastrados {sexo.count("M")} homens.')
print(f'c) Existem {len(mulher20)} mulheres com menos de 20 anos.')
