'''
Ejercicio 49
Simular un lanzamiento de dado hasta obtener un 6
'''
import random
numero = 0

while numero != 6:
  numero = random.randint(1, 6)
  print(f"Has sacado un {numero} en este lanzamiento")

print("sacaste un 6! Felicidades :) ")