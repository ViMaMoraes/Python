try:
    valor = int(input('Digite o valor do seu produto: '))
    print(type(valor))
    print(valor)
except ValueError:
    print('Favor digitar um valor em números.')
finally:
    print('Codigo ok')

'''
else:
    print('Usuário digitou um valor correto')
    resultado = valor * 2
    print(resultado)
'''

print('Mais codigo abaixo')
