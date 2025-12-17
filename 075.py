'''
Ejercicio 75
Crear una clase coche con los atributos:
marca, modelo, matricula, km
con los metodos:
- int como constructor
- avanzar()km este aumenta el valor de km en la cantidad
'''
class Auto:
  def __init__(self, marca, modelo, matricula, km):
    self.marca = marca
    self.modelo = modelo
    self.matricula = matricula
    self.km = km

  def avanzar(self, km):
    self.km = self.km + km

auto1 = Auto('Ford', '1997 Ford F-150 Pick Up',"XH*66*40", 5000)
print(auto1.__dict__)
auto1.avanzar(3000)
print(auto1.__dict__)

