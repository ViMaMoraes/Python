# Desafio do IMC - Índice de Massa Corporal

'''
Qual é a sua altura em cm:
Qual é o seu peso em kg:
'''

'''
Menor que 18,5 MAGREZA
ENTRE 18,5 E 24,9 NORMAL
ENTRE 25,0 E 29,9 SOBREPESO
ENTRE 30,0 E 39,9 OBESIDADE
MAIOR QUE 40,0 OBESIDADE GRAVE
'''

'''
Formula de IMC = PESO / ALTURA * ALTURA or PESO / ALTURA² * 10000
'''

altura = float(input("Qual e a sua altura em cm: "))
peso = float(input("Qual e o seu peso em kg: "))

#metro = (altura * altura)
imc = peso / (altura/100)**2

if imc < 18.5:
    print("MAGREZA")
elif imc >= 18.5 and imc <= 24.9:
    print("NORMAL")
elif imc >= 25.0 and imc <= 29.9:
    print("SOBREPESO")
elif imc >= 30.0 and imc <= 39.9:
    print("OBESIDADE")
else:
    print("OBESIDADE GRAVE")
