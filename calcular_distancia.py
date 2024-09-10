tempo_gasto = float(input("Digite aqui o tempo gasto do trajeto: "))
print("Seu trajeto tem o tempo de: ", tempo_gasto, "horas")

velocidade_media = float(input("Digite aqui a velocidade estimada para percorrer o trajeto: "))
print("A velocidade média a percorrer é de: ", velocidade_media, "km")

distancia = tempo_gasto * velocidade_media

litros_usados = distancia / 12

print("A quantidade de combustivel utilizado na viagem é de ", round(litros_usados, 1), "na velocidade média de ", velocidade_media,"km", "com o tempo de viagem de aproximadamente", tempo_gasto, "horas" )