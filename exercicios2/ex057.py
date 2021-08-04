# Faça um programa que leia o Sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

s = ''
while s != 'F' and s != 'M':
    s = str(input('Digite seu sexo:[M/F]: ')).upper().strip()
    print('digite novamente')
print('Ola ')


# while s not in 'MmFf':