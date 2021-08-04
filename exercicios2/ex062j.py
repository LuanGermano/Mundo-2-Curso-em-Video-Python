termo = int(input('Digite o Termo da PA: '))
razao = int(input('Digite a razão: '))
ulti = int(input('Qual o termo da PA para ser mostrado: '))  # valor de entrada dos termos pra PA.
while ulti != 0:
    resp = "n/a"
    while resp not in 'SsNn':  # acontecimento pra resp errado
        resp = str(input('Vc gostaria de ver o caminho até o termo solicitado? [S/N]: ')).upper().strip()  # Decisão que vai separar entre sim e não os acontecimentos.
        if resp in 'Ss':  # caso Sim
            for c in range(1, ulti+1):
                pa = termo + (c - 1) * razao
                print(pa, end=' ',)
            print(end='\n')
            break
        elif resp in 'Nn':  # Caso não
            pa = termo + (ulti-1) * razao
            print(pa, end='\n')
            break
        print('Por favor Responda se gostaria de ver o termo solicitado')

    ulti = int(input('Qual o termo da PA para ser mostrado: '))
print('Encerrando o Programa')
print('=-='*12)