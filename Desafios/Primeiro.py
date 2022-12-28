# Desafios com (IF, ELIF, ELSE)
'''
Criar um programa que dependendo da temperatura (em celsius) do steak
ele retorna o ponto de cozimento em portugues. O usuário deverá
fornercer a temperatura

Temperatura - Cozimento
120ºF ou 48ºC - Rare (Selada)
130ºF ou 54ºC - Medium rare (Ao ponto para o mal)
140ºF ou 60ºC - Medium (Ao ponto)
150ºF ou 65ºC - Medium well (Ao ponto para o bem)
160ºF ou 71ºC - Well done (Bem passada)

Se estiver com menos de 120ºF ou 48ºC - retornar Cozinhar por mais alguns minutos
Se estiver com mais de 160ºF ou 71ºC - Continuar com o retorno de Bem passada
'''

temperatura_steak = int(input("Qual e a temperatura da carne? "))

if temperatura_steak < 48:
    print("Cozinhar por mais alguns minutos")
elif temperatura_steak in range(48, 53):
    print("Selada")
elif temperatura_steak in range(54, 59):
    print("Ao ponto para o mal")
elif temperatura_steak in range(60, 64):
    print("Ao ponto")
elif temperatura_steak in range(65, 70):
    print("Ao ponto para o bem")
elif temperatura_steak >= 71:
    print("Bem passada")
