# Crie um programa que leia a IDADE e o SEXO de varias pessoas.
# A cada pessoa cadastrada, o programa devera perguntar se quer ou não continuar.
# no final mostre:
# A) pessoas maiores de 18
# B) Quantos Homens foram cadastrados.
# C) quantas mulheres tem menos de 20

idade = []  # Informação de todas as idades
sexo = []  # Informação de todos os sexos
idade18 = []  # Idade de todos os Homens
idadef = []  # Idade de todas as mulheres
idadefemenor = []  # Idade de todas mulheres menores de 20
continuar = 'n/a'

while continuar not in 'nN':
    id = int(input('Digite a sua idade: '))
    idade.append(id)  # lista com idades
    if id > 18:
        idade18.append(id)
    sx = str(input('Diga qual é o seu sexo [M/F]: ')).upper().strip()

    while sx not in "MmFf":
        sx = str(input('Por favor digite seu Sexo[M/F]:')).upper().strip()
    if sx == "F":
        idadef.append(id)  # Lista com as idades femininas
        if id < 20:
            idadefemenor.append(id)

    sexo.append(sx)  #lista com os Sexos
    continuar = str(input('Deseja continuar?[S/N]: ')).lower().strip()
    while continuar not in "SsNn":
        continuar = str(input('Deseja continuar?[S/N]: ')).lower().strip()

print(f'A) tem {len(idade18)} pessoas acima de 18 anos   ')  # Conferir quantidade total maior q 18
print(f'B) Foram cadastrados {sexo.count("M")} homens na lista ')   # Conferir Lista de homens
print(f'C) Tem {len(idadefemenor)} mulheres abaixo de 18 anos')   # Conferir mulheres menos de 20


