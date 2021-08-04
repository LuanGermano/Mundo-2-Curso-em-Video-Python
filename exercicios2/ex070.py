# Crie um programa que leia o nome e o preço de varias produtos. O programa deve perguntar se o Usuario vai continuar
# No final Mostre:
# A) Qual a é o Total gasto na compra.
# B) Quantos produtos custam mais de R$1000
# C) Qual é o nome do produto mais barato

continuar = 'S'
prod = []
precos = []
cont = 0
while continuar == 'S':
    produto = str(input('Nome do produto: '))
    prod.append(produto)
    preco = float(input('Preço do produto: R$ '))
    if preco > 1000:
        cont += 1
    precos.append(preco)
    continuar = str(input('Deseja adicionar mais algo?[S/N] ')).upper().strip()

index = precos.index(min(precos))
barato = prod[index]

print(f'A soma dos deus produtos saiu no valor de R${sum(precos):.2f}. ')
print(f'Tem {cont} produtos acima de 1000 reais no seu carrinho. ')
print(f'O produto mais barato da sua cesta é o {barato} custando R${precos[index]:.2f}.')
