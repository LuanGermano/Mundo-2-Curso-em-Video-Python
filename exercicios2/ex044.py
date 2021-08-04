# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento
# à vista dinheiro, cheque: 10% de desconto
# a vista no cartão: 5% de desconto
# Em até 2x no cartão: Preço Normal
# 3x ou mais no cartão: 20% de juros.
print(f'{"Lojas Guanabara":=^40}')
val = float(input('Qual o valor do produto? R$ '))
met = str(input('Escolha o método de pagamento?\nCheque-1   Dinheiro-2   Débito-3   Crédito-4\nO método: ')).strip()

# para parcelas no cartão
if met == "4":
    cart = str(input('Digite o número de parcelas: '))
else:
    cart = 0
pre = 0
if met == '1' or met == '2':
    pre = val * 0.90
elif met == '3' or cart == '1':
    pre = val * 0.95
elif met == '4' and cart == '2':
    pre = val
elif met == '4':
    pre = val * 1.2
else: # caso nenhum numero aceito.
    print('informação invalida')
    exit()
print(f"Agradecemos a preferencia, sua compra saiu no valor de R${pre:.2f} ")
if cart != 0:
    print(f'Sua parcela foi em {cart}x e saira cada parcela no valor de R${(pre / int(cart)):.2f} ')
print(f'{"Lojas Guanabara":=^40}')