#Crie um programa que leia duas notas de um aluno e calcule sua média,
#mostrando uma mensagem no final, de acordo com a média atinginda:
#-Media abaixo de 5.0 reprovado
#-Media entre 5 e 6,9 é recuperação:
#-Media 7 acima é aprovado.
from cor import cores
n1 = float(input('Qual a nota da prova pratica de portugues? '))
n2 = float(input('Qual a nota da prova pratica de matematica? '))
nm = (n1 + n2) / 2
cc = cores["cle"]
  #Programa da situação do aluno perante o ensino.
if nm < 5:
    aluno = 'Reprovado'
elif nm > 7:
    aluno = 'Aprovado'
else:
    aluno = 'Recuperação'
   #Programa de atribuição de cores para as notas
if n1 >= 5:
    c1 = cores["Bblu"]
else:
    c1 = cores["Bred"]

if n2 >=5:
    c2 = cores["Bblu"]
else:
    c2 = cores["Bred"]

if nm >= 5:
    c3 = cores["Bblu"]
else:
    c3 = cores["Bred"]

print(f'A Nota de portugues do Aluno foi {c1}{n1:.1f}{cc} e junto da nota de matematica que foi {c2}{n2:.1f}{cc} \nO aluno obteve uma media final de {c3}{nm:.1f}{cc}! ')
print(f'E a sua situação com a instituição de ensino é a de {aluno}!')
