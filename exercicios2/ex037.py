#escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher
#qual sera a base da conversão:
#-1 para binario
#-2 para octal
#-3 para hexadecimal
from cor import cores
num = int(input('Digite um numero: '))
print(f'Para Sistemas Binario digite {cores["Bred"]}[1]{cores["cle"]}\n'
      f'Para Sistemas octal digite {cores["Bblu"]}[2]{cores["cle"]}\n'
      f'Para Sistemas hexadecimal digite {cores["Bgre"]}[3]{cores["cle"]}')
conv = float(input('Digite qual: '))
if conv == 1:
      print(f'O seu numero {num} em binario se tornará: {num:b}. ')
elif conv == 2:
      print(f'O seu numero {num} em Octal se tornara: {num:o}.')
elif conv == 3:
      print(f'O seu numero {num} em Hexadecimal se tornara: {num:x}.')
else:
      print('Opção invalida')
