#Escreva um programa para aprovar o emprestimo bancário para a compra de uma casa
#O Programa vai perguntar o 'Valor da casa', o 'Salario' do comprador e em quantos anos ele vai pagar
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario
#Ou então o emprestimo sera negado.

casa = float(input('Qual o Valor da casa que deseja? R$ '))
sal = float(input('Qual o seu salario atual? R$ '))
year = float(input('Em quantos anos pretende pagar? '))
prest = casa / (year * 12)

if prest >= sal * .3:
    print(f'Sinto muito, a prestação de R${prest:.2f} ultrapassa o valor de 30% do seu salario, logo seu emprestimo foi negado')
else:
    print(f'O valor da prestação da sua casa ficara no valor de R${prest:.2f}, agradecemos sua a preferencia! ')