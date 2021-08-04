'''Crie um programa que leia vários númerios inteiros pelo teclado.
o programa só vai parar quando o usuario digitar o valor 999, que é a condição de parada.
No final, mostre quantos numeros foram digitados e qual foi a soma entre eles
DESCONSIDERANDO O FLAG'''

print('Caso queira encerrar o programa digite 999.')
num = int(input('Digite um valor: '))
soma = []
print('-=-'*11)
while num != 999:
    soma += [num]
    print('Caso queira encerrar o programa digite 999.')
    num = int(input('Digite outro valor: '))
    print('-=-'*11)
print(f'A quantidade de numeros digitados foi {len(soma)} com a soma total sendo {sum(soma)}')