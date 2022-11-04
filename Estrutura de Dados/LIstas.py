# ----------------------------------------------------\
# Armazenar mais de uma informação em variáveis
# Manter a sequencia dos dados em uma variável

cidade1 = 'Rio de Janeiro'
cidade2 = 'São Paulo'
cidade3 = 'Salvador'

cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Goiana']
#                  0              1           2           3

# cidades.append('Santa Catarina')
# cidades.remove('Salvador')
# cidades.insert(1, 'Santa Catarina')
# cidades.pop(0)
# cidades.sort()

# print(cidades)

numeros = [2, 3, 4, 5]
letras = ['a', 'b', 'c', 'd']

numeros.extend(letras)
# print(numeros)

itens = [['item1', 'item2'], ['item3', 'item4']]

# print(itens[1][1])

produtos = ['arroz', 'feijão', 'laranja', 'banana', 1, 3, 5, 6]

item1, item2, *outros, item8 = produtos

'''
print(item1)
print(item2)
print(item8)
print(outros)
'''

valores = [50, 80, 110, 150, 170]

for x in valores:
    result = 'O valor final do produto é de R${x}.'

#cor_cliente = input('Digite a cor desejada: ')
cor = ['amarelo', 'verde', 'azul', 'vermelho']
'''
if cor_cliente.lower() in cor:
    retorno = 'Em estoque'
else:
    retorno = 'Não temos essa cor em estoque'
'''

cores = ['amarelo', 'verde', 'azul', 'vermelho']
valores = [10, 20, 30, 40]

duas_listas = zip(valores, cores)

# print(list(duas_listas))

frutas_usuario = input('Digite o nome das frutas separados por virgula: ')

frutas_lista = frutas_usuario.split(', ')

print(frutas_lista)
