# ----------------------------------------------------\
velocidade = 50

if velocidade > 110:

    print("Acima da velocidade permitida")
    print("Favor reduzir a sua velocidade")

elif velocidade < 60:

    print("Favor dirigir acima de 80km/h")

else:

    print("Velocidade OK")

# Primeira aula de If ELse

# ----------------------------------------------------/
# ----------------------------------------------------\
# Operadores Logicos

renda_acima_5mil = False
nome_limpo = False

if renda_acima_5mil or nome_limpo:

    print("Financiamento Aprovado")

else:

    print("Financiamento Negado")

# ----------------------------------------------------/
# ----------------------------------------------------\
# Operador ternário

idade = 15

'''if idade >= 16:

    resultado = print("Voto permitido")

else:

    resultado = print("Voto não permitido")'''

resultado = "Voto Permitido" if idade >= 16 else "Voto não permitido"

print(resultado)

# ----------------------------------------------------/
# ----------------------------------------------------\
# Multiplos operadores de comparação

valor = 20

# if valor >= 20 and valor < 40:
if 20 <= valor < 40:

    print("Produto foi aceito")

else:

    print("Produto não foi aceito")


# ----------------------------------------------------/
