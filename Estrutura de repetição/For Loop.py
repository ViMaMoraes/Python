# ----------------------------------------------------\
# For Loop - Utilizando números

# Tarefa: imprimir do 1 a 5

'''
print("1")
print("2")
print("3")
print("4")
print("5")
'''

# for numero in range(1, 301):

# print(numero)

# ----------------------------------------------------/
# ----------------------------------------------------\
# Foor Loop - Utilizando string

'''
palavra = "Espetacular"

for letra in palavra:

    print(f"{letra} - esta dentro da palavra {palavra}")
'''

# ----------------------------------------------------/
# ----------------------------------------------------\
# Foor Loop - Utilizando if e else
# Enviar um email com os detalhes da compra online
# (maximo 3 tentativas) para compras confirmadas.

compra_confirmada = False
dados_compa = "Compra no valor de R$ 12.50 e entrega confirmada"

for enviar in range(3):
    if compra_confirmada:
        print(dados_compa)
        print("Detalhes enviado para o seu email")
        break
else:
    print("Falha na compra")

# ----------------------------------------------------/
