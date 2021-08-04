# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while.
# An = a1 +(n-1) *r
#a1 é o primeiro termo
#n é o limite da PA
#r é a razão

cont = 0
termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
print(f'Sua progressão aritmetica com termo {termo} e razão de {razao} foi a seguinte: ')
while cont != 10:
    pa = termo + cont * razao
    cont += 1
    print(pa, end=" ")
print('FIM')
