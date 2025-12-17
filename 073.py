'''
Ejercicio 73
Crear una clase Libro
atriburtos:
titulo, autor, editorial, año de publicacion
Metodos:
cosntructor para inicializar atributos
'''
class Libro:
  def __init__(self, titulo, autor, editorial, anyo_publicacion):
    self.titulo = titulo
    self.autor = autor
    self.editorial = editorial
    self.anyo_publicacion = anyo_publicacion

mi_libro = Libro(
  'Titulo Libro',
  "Elba Neado",
  "Editorial 1",
  "1990")

print(mi_libro.__dict__)