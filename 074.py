'''
Ejercicio 74
Crear una clase persona con los atributos:
*** nombre, edad, DNI ***
con los metodos:
- init()
- es_mayor_de_edad() -> este retorna True si es mayor de edad.
'''
class Persona:
  def __init__(self, nombre, edad, dni):
    self.nombre = nombre
    self.edad = edad
    self.dni = dni

  def es_mayor_de_edad(self):
    if self.edad >= 18:
      return True

persona1 = Persona('Jose',20,'24501-k')

print("El nombre es: ", persona1.nombre)
print(f"La edad de : {persona1.nombre} es : ", persona1.edad)
if persona1.es_mayor_de_edad():
  print("Es Mayor de edad")
else:
  print("Es menor de edad")
