# Desafio com 'Sets'

'''
Criar um programa que gera 3 listas de acordo com a necessaidade logo abaixo:

Lista1 = Funcioários que tem carro e trabalham a noite
Lista2 = Funcioários que tem carro e trabalham durante o dia
Lista3 = Funcioários que não tem carro

'''

funcionarios = ['Ana', 'Marcos', 'Alice',
                'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_carro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

Lista1 = set(tem_carro).intersection(turno_noite)
print(Lista1)

Lista2 = set(tem_carro).intersection(turno_dia)
print(Lista2)

Lista3 = set(funcionarios).difference(tem_carro)
print(Lista3)
