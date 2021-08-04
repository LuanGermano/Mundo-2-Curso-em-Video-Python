# Desenvola um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a media de idade do grupo.
# Qual é o nome do homem mais velho
# Quantas mulheres tem menos de 20 anos.
h = []
m = []
i = []
im = []
ih = []
index = 0
hvelho = 0
num = int(input('Quantas pessoas serão analisadas: '))
for pess in range(0, num):
    print(f'=-=-=-= {pess+1}ª pessoa =-=-=-=')
    nome = str(input('Diga o Seu nome: ')).title().strip()  # nome dos candidatos q vai repetir
    idade = int(input('Digite sua idade: '))  # idade que sera colocada numa lista
    i += [idade]  # Lista com as idades
    sexo = str(input('Qual o seu sexo( M//F ) : ')).lower().strip()  # sexo da pessoa se homem ou mulher

    if sexo == 'm':
        h += [nome]  # se for homem adiciona o nome nessa lista
        ih += [idade]  # idade dele nessa lista
    elif sexo == 'f':
        m += [nome]  # se for mulher vem pra essa lista
        im += [idade]
    else:
        print('informação errada')
        break  # Interrompe o programa no erro enquanto ainda n sei repetir
print(f'=-=-=-='* 3)
med = sum(i) / num  # preciso somar os valores dentro de uma lista e dividir por pess

if len(ih) != 0:
    index = ih.index(max(ih))
    hvelho = h[index]  # preciso pegar a maior idade do grupo de homens e bater com a posição na lista de nomes

menor = [x for x in im if x < 20]  # Ver quais numeros são menos que 20 na lista de idade das mulheres e só isso mesmo
mmenores = len(menor)

print(f'A média de idade desse grupo é de {med:.1f} anos. ')
if hvelho == 0: #n tem lista de homens né
    print("Não existem homens nessa lista ")
else:
    print(f'O homem mais velho da lista é o {hvelho} com {max(ih)} anos')
if len(m) == 0:
    print(f'Não existem Mulheres nessa lista')
else:
    print(f'Existem {mmenores} mulheres com menos de 20 anos ')

'''Ele basicamente faz um for loop na lista que tu definir ali dps do "in"
E gera outra lista, pra cada item da lista im ele cria uma variavel local x e verifica se é menor que 20 por causa da condiçao que tu definiu
E tu pode fazer mais coisa com isso
Tipo...
[x**2 for x in im if x < 20]
Ele eleva ao quadrado todos os itens que forem menor que 20 é o equivalente a tu fazer 
novaLista = []
for x in im:
   if x < 20:
       novaLista.append(x**2)'''
