# Desafio com Funções

'''
Criar um programa que calcula a quantidade de tinta necessária para
pintar uma parede. O usuário deverá fornecer as seguintes
informações: Rendimento, altura e largura.
O programa deve mostrar na tela a mensagem 'Você necessita de x latas de tinta'

Formula1 = Altura / Rendimento * Largura
OU
Foruma2 = Largura / Rendimento * Altura
'''

rendimento = int(input("Qual e o rendimento da lata? "))
altura = int(input("Qual e a altuira da parede? "))
largura = int(input("Qaul e a largura da parede? "))


def calculate_parede():
    ret_calc = largura / rendimento * altura
    print(f'Você precisa de {ret_calc} latas de tinta')


calculate_parede()
