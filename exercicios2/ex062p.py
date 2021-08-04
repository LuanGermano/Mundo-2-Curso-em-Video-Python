#

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -', end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos vc quer mostrar a mais? '))
print(f'progressão finalizada com {total} termos mostrados. \nFIM')
