#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
#e mostre sua categoria, de acordo com a idade:
#-Ate 9 anos: Mirim
#-ate 14 anos: infantil
#-ate 19 anos: junior
#-ate 25 anos: senior
#-Acima:MASTER

from datetime import date
nasc = int(input('Digite o seu ano de nascimento: '))
year = date.today().year
age = year - nasc
if age > 25:
    catego = 'Master'
elif age <= 9:
    catego = 'Mirim'
elif age <= 14:
    catego = 'Infantil'
elif age <= 19:
    catego = 'Junior'
elif age <= 25:
    catego = 'Senior'

print(f'A categoria que o atleta se encontra é a de {catego}! ')
