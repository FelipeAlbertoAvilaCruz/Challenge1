import math

def velocidad (latitud):
    "Formula principal: velocidad = distancia recorrida entre el tiempo transcurrido (tiempo = 24 horas)."
    "Formula de la circunferencia del paralelo que corresponde a la latitud:"
    "distancia= 2(pi)*RT*cos(a), distancia = circunferencia, RT = radio medio de la tierra (6371km), cos(latitud) = coseno de la latitud."
    radioTierra = 6371 
    distancia = ((2*(math.pi))*radioTierra*math.cos(latitud))
    tiempo = 24
    resultado = distancia/tiempo 
    return resultado

"Las latitudes de cada respectiva coordenada, para obtener la velocidad de rotación de la tierra no es necesaria la longitud"
latitud1 = 18.60646
latitud2 = -38.373825292521154

print("Resultado 1.",velocidad(latitud1),"km/h")
print("Resultado 2.",velocidad(latitud2),"km/h")
