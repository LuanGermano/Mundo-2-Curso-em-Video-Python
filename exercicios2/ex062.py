# Melhore o desafio 061, perguntando para o usuario se ele uer mostrar mais alguns termos.
# o programa encerra qnd ele disser q quer mostrar 0 termos (mostrar mais termos)

termo = int(input('Digite o Termo da PA: '))
razao = int(input('Digite a razão: '))
ulti = int(input('Qual o termo da PA para ser mostrado: '))
while ulti != 0:
    resp = 'jean'
    while resp not in 'SsNn':  # acontecimento pra resp errado
        resp = str(input('Vc gostaria de ver o caminho até o termo solicitado? [S/N]: ')).upper().strip()
        if resp == 'S':  # caso Sim
            for c in range(1, ulti+1):
                pa = termo + (c - 1) * razao
                print(pa, end=' ',)
            print(end='\n')
        elif resp == 'N':  # Caso não
            pa = termo + (ulti-1) * razao
            print(pa, end='\n')
        else:
            print('Por favor Responda se gostaria de ver o termo solicitado')

    ulti = int(input("Qual o termo da PA para ser mostrado: "))
print('Encerrando o Programa')
print('=-='*12)
