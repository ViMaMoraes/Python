'''
valores = []

for x in range(6):
    valores.append(x * 10)

print(valores)
'''

from sys import getsizeof
valores = [x * 10 for x in range(6)]

# print(valores)

numeros = [x * 10 for x in range(1000000)]

print(type(numeros))
print(getsizeof(numeros))

print('================================================================')

numeros = (x * 10 for x in range(1000000))

print(type(numeros))
print(getsizeof(numeros))
