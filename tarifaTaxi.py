distancia = float(input("Ingresa la distancia recorrida en km: "))
hora = int(input("Ingresa a la hora que vas a salir (número entre 0 y 23)"))
tarifaBase= 1
if hora <= 19 and hora>=6:
    costoPorKm = 0.50
    horario = "Diurno"
else:
    costoPorKm = 0.65
    horario = "Nocturno"
if distancia > 10:
    recargo= 2
else:
    recargo=0
print (f"Vas a salir en horario {horario} \nLa distancia recorrida total es {distancia}km \nEl costo a pagar es: ${tarifaBase + (distancia * costoPorKm)+ recargo}")