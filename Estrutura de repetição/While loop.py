# ----------------------------------------------------\
# Excelente para loops dependentes de uma condição.
# Criar uma promoção para um produto no valor de R$ 100,00

valor = 100
dia = 1

while valor > 20:
    print(f' No dia {dia} o produto vai ser vendido por R$ {valor}')
    dia += 1
    valor -= 5
