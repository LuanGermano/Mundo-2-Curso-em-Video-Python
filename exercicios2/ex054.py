#Crie o programa que leia o ano de nascimento de sete pessoas. No final,
#Mostre quantas pessoas ainda não atingiram a maioridade e quantas ja são maiores,
# maior é 21
from datetime import date
ano = date.today().year
maior = 0
menor = 0
pessoas = int(input('Escreva Quantas pessoas serão consideradas: '))
for name in range(1, pessoas+1):
    nasci = int(input(f'Digite o ano de nascimento da {name}ª pessoa: '))
    if (ano - nasci) >= 21:
        maior = maior + 1
    elif (ano - nasci) < 20:
        menor = menor + 1
print(f'Nesse grupo de {pessoas} pessoas temos {maior} que ja atingiram a maioridade e {menor} menores de idade ')
