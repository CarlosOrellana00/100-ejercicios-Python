'''
Ejercicio 72
Crea una clase Circulo con
los siguientes atributos:
* radio: radio del circulo
la clase debe de tener los siguientes metodos:

* __init__(self, radio): inicializa los atributos de la clase
* calcular_area(self): calcula y devuelve el area del circulo
* calcular_perimetro(self): calcular y devuelve el perimetro del circulo

'''
import math

class Circulo:
  def __init__(self, radio):
    self.radio = radio

  def calcular_area(self):
    return math.pi * self.radio ** 2

  def calcular_perimetro(self):
    return 2 * math.pi * self.radio

circulo1 = Circulo(5)
print(f"el area es: { circulo1.calcular_area() }")
print(f"el perimetro es: { circulo1.calcular_perimetro() }")