'''
Ejercicio 68
Escribe una funcion que pida por teclado
la distancia y la velocidad
para poder calcular el tiempo de viaje
'''
def tiempo_viaje():
  distancia = int(input("Escribe la distancia: "))
  velocidad = int(input("Escribe la velocidad: "))

  return distancia /velocidad

resultado = tiempo_viaje()
print(resultado,"hrs es el tiempo total de viaje")