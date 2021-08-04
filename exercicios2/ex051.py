#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. no final,
# mostre os 10 primeiros termos da progressão.
# (progressão aritmetica)
termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Qual será a razão da PA: '))
ulti = int(input('Qual será o ultimo termo da PA: '))
print(f'Sua progressão aritmetica em {ulti} termos tem os seguintes valores:')

for c in range(1, ulti+1):
    pa = termo + (c - 1) * razao
    print(pa,end=' → ')
print('Encerrou')