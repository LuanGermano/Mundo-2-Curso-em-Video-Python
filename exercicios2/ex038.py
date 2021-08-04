#Escreva um programa que leia 'dois numeros' inteiros e compare-os,
#mostrando na tela uma mensagem:
#-O primeiro valor é maior
#-O segundo Valor é maior
#-não existe valor maior, os dois são iguais

num1 = int(input('Digite um Valor inteiro: '))
num2 = int(input('Digite outro valor inteiro: '))
if num1 > num2:
    print('O primeiro valor é maior!')
elif num2 > num1:
    print('O segundo valor é maior!')
else:
    print('Os valores são iguais!')