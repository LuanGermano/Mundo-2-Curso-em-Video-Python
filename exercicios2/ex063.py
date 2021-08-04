#escreva um programa que leia um numero N inteiro qualquer
# e mostre na tela os N primeiros elementos de uma sequencia de fibonacci;
#ex = 1- 1 - 2 - 3 - 5 - 8
# Fn = Fn - 1 + Fn - 2
fb = [0, 1]
n = int(input('Ate qual numero deseja? '))
c = 0
# print('Referencia é \n0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ')
print(f'A sequencia de fibonacci até o numero {n} é de:')
if n == 1:
    mostrar = fb[:1]
    print(mostrar)

else:
    while len(fb) != n:
        #EU QUERO O ANTECESSOR DO PROXIMO NUMERO JUNTO DO PROXIMO MENOS 2 NESSE CARALHO
        adic = (fb[(2 + c) - 1]) + (fb[(2 + c) - 2])
        fb += [adic]
        c += 1
    mostrar = fb[:(n+1)]
    print(mostrar)
