'''
Ejercicio 81
Crear una clase Rectangulo con los siguientes atributos
- base: base del rectangulo
- altura: altura del rectangulo

La Clase debe tener los siguientes metodos:
  ** __int__(self, base, altura): inicializa los atributos de la clase
  ** calcular_area(self):calcula y devuelve el area del rectangulo
  ** calcula_perimetro(self): calcula y devuelve el perimetro del rectangulo
'''

class Rectangulo:
  def __init__(self, base, altura):
    self.base = base
    self.altura = altura

  def calcular_area(self):
    return self.base * self.altura

  def calcular_perimetro(self):
    return 2 * (self.base + self.altura)

rec1 = Rectangulo(5,3)
print(f"Area: {rec1.calcular_area()}")
print(f" Perimetro: {rec1.calcular_perimetro()}")
