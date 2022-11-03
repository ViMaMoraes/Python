# ----------------------------------------------------\

def boas_vindas_Marcus():
    print('Olá Marcus!')
    print('Temos 5 laptops em estoque')


# boas_vindas()

def somar_dois_numeros():
    numero1 = 10
    numero2 = 5
    resultado = numero1 + numero2
    print(resultado)


# somar_dois_numeros()

def boas_vindas_Ronaldo():
    print('Olá Ronaldo!')
    print('Temos 5 laptops em estoque')


def boas_vindas_Linda():
    print('Olá Linda!')
    print('Temos 5 laptops em estoque')


'''
boas_vindas_Marcus()
boas_vindas_Ronaldo()
boas_vindas_Linda()
'''


def boas_vindas(nome, quantidade=6):
    print(f'Olá {nome}!')
    print(f'Temos {str(quantidade)} laptops em estoque')


#boas_vindas('Richard', 5)

def cliente1(nome):
    print(f'Olá {nome}')


def cliente2(nome):
    return f'Olá {nome}'


'''
x = cliente1('Maria')
y = cliente2('José')

print(x)
print(y)
'''


def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado


#x = soma(2, 3, 4, 7)
# print(x)

def agencia(**carro):
    return carro


print(agencia(Modelo='Gol', Cor='Branca', motor=1.0, placa=1234))
print(agencia(Modelo='Gol', Cor='Preto', motor=1.0))
print(agencia(Modelo='Gol', Cor='Vermelho', motor=1.0, placa=4444))
