#Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status
#de acordo com a tabela abaixo:
#Abaixo de 18.5 abaixo do peso
#entre 18.5 e 25 peso ideal
#25 ate 30 sobrepeso
#30 ate 40 obesidade
#acima de 40 obesidade morbida

peso = float(input('Digite o valor do seu peso em Kilogramas: '))
alt = float(input('Digite o valor da sua altura em centimetros: ')) / 100
imcval = peso / (alt * alt)
if imcval < 18.5:
    imcres = 'Abaixo do peso'
elif imcval < 25:
    imcres = "Peso ideal"
elif imcval < 30:
    imcres = 'Sobrepeso'
elif imcval < 40:
    imcres = 'Obesidade'
else:
    imcres = 'Obesidade morbida'

print(f'O valor do seu IMC deu {imcval:.2f}kg/m2 e o seu status é o de {imcres}. ')