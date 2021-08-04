print('-' * 30)
print('Sequencia de Fibonacci')
print('-' * 30)
n = int(input('Quantos termos voce quer mostrar? '))
t1 = 0
t2 = 1
print('-' * 30)
cont = 3
while cont <= n:
    t3 = t1 +t2
    print(f' - {t3}',end='')
    t1 = t2  # to transformando o termo 1 no termo 2 e embaixo tornando o 2 no 3 assim sempre avançando
    t2 = t3
    cont += 1
print(' -FIM')