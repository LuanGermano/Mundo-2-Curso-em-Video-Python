# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade
# -Se ele ainda vai se alistar ao serviço militar.
# -Se é a hora de se alistar.
# Se já passou do Tempo do alistamento.
# Seu programa tambem devera mostrar o tempo que falta ou que passou do prazo.
from datetime import date

nasc = int(input("Qual o seu ano de nascimento? "))
year = date.today().year
idade = year - nasc
if idade >= 18:
    print(f'O prazo de alistamento no exercito já passou em {idade-18} anos, '
          f'caso não tenha feito, vá imediatamente numa unidade! ')
elif idade == 17:
    print('Está na época do seu alistamento, va pra unidade da sua região!')
else:
    print(f'Voce ainda não esta em idade de se alistar, faltam {18-idade} anos.')
