'''
Ejercicio 67
Escribe una funcion para calcular
el volumen de un cilindro
V = πr²h
'''
import math

def volumen_cilindro(radio, altura):
  return math.pi * radio  ** 2 * altura

resultado = volumen_cilindro(3,5)

print(resultado)

