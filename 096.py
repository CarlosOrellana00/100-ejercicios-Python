'''
Ejercicio 096
Crear un excepcion que me ayude
a determminar si el indice de una
lista esta fuera de rango
'''

mi_lista = [1,2,3]

try:
  print(mi_lista[5])
except IndexError:
  print("Error, el indice no existe")
