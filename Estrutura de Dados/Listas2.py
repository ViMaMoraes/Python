from array import array
cores_list = ['amarelo', 'verde', 'azul', 'vermelho']
cores_tuple = ('amarelo', 'verde', 'azul', 'vermelho')

# cores_tuple.append('roxo')

# print(cores_list)


letras = ['a', 'b', 'c', 'd']
numeros_i = [10, 20, 30, 40]
numeros_f = [1.2, 2.2, 3.2]

'''
print(letras)
print(numeros_i)
print(numeros_f)
print()
'''

letras = array('u', ['a', 'b', 'c', 'd'])
numeros_i = array('i', [10, 20, 30, 40])
numeros_f = array('f', [1.2, 2.2, 3.2])

'''
print(letras)
print(numeros_i)
print(numeros_f)
'''

list1 = [10, 20, 30, 40, 50]
list2 = [10, 20, 60, 70]

num1 = set(list1)
num2 = set(list2)

'''
print(num1 | num2)  # Union
print(num1 - num2)  # Difference
print(num1 ^ num2)  # Symmetric Difference
print(num1 & num2)  # And
print(len(num1))
print(num1[0])
'''

list3 = [1, 2, 3, 4, 5, 6]
s1 = {1, 2, 3, 4, 5, 6}
s1.update([7, 8, 9, 10])
s1.remove(10)
s1.discard(9)

'''
print(list3)
print(s1)
'''

set1 = {'a', 'b', 'c'}
set2 = {'a', 'd', 'e'}
set3 = {'c', 'd', 'f'}

set4 = set1.symmetric_difference(set3)

# print(set4)

aluno = {
    'nome': 'Ana',
    'idade': 16,
    'nota_final': 'A',
    'aprovação': True,
    'materias': ['Fisica', 'Matemactica', 'Ingles']
}

'''
aluno['nome'] = 'Jose'
aluno.update({'nome': 'Mirela', 'nota_final': 'B'})
print(aluno)

aluno.update({'endereço': 'A'})

del aluno['idade']
print(aluno)

for keys, values in aluno.items():
    print(f'{keys}: {values}')

print(aluno.items())
print(aluno.keys())
print(aluno.values())
'''


def somar(x):
    def func2(x): return x + 10
    return func2(x) * 4


# print(somar(2))

lista1 = [1, 2, 3, 4]


# def multi(x):
#   return x * 2


#lista2 = map(lambda x: x * 2, lista1)

#print(list(map(lambda x: x * 2, lista1)))

valores = [10, 12, 34, 44, 57]


'''
def remover20(x):
    return x > 20


print(list(filter(remover20, valores)))
'''

print(list(filter(lambda x: x > 20, valores)))

frutas1 = ['abacate', 'banana', 'morango', 'kiwi', 'abacaxi']
#frutas2 = []

'''
for iten in frutas1:
    if 'n' in iten:
        frutas2.append(iten)
'''

frutas2 = [iten for iten in frutas1 if 'b' in iten]

print(frutas2)
