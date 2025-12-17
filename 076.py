'''
Ejercicio 76
Crear una clase animal con los atributos
especie y nombre
la clase debe tener los metodos:
- init y hablar()
el metodo hablar nos retorna una palabra
segun la interpretacion del sonido como perro seria "guau"
'''
class Animal:
  def __init__(self, especie, nombre):
    self.especie = especie
    self.nombre = nombre

  def hablar(self):
    if self.especie == "perro":
      print("Guarrw!!!")
    elif self.especie == "gato":
      print("Miauww!!!")
    else:
      print("animal no enconrado")

perro = Animal('perro',"Doko")
gato = Animal("gato", "Minino")

perro.hablar()
gato.hablar()
