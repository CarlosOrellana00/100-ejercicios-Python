'''
Ejercicio 80
Obtener la cantidad de memoria RAM
en mi computadora o laptop


***  es necesario instalar PC "psutil" ***
1.- debemos de ir a la consola en la carpeta que estemos trabajando
2.- debemos escribir en consola lo siguiente:
  pip install psutil
3.- psutil es una libreria externa, por eso debemos instalarla.
'''
import psutil

def obtener_ram():
  memoria = psutil.virtual_memory()
  memmoria_total = memoria.total / (1024 ** 3)
  return memmoria_total

memoria = obtener_ram()
print("la Memoria RAM del equipo es: ",memoria," GB")

