'''
Ejercicio 77
Crear una clase llamada Persona
con los atriburos: nombre, edad
* un constructor, donde los datos pueden estar vacios
* los setters y getters
para cada uno de los atributos.
* mostrar(): Muestra los datos  de la persona.
* esMayorDeEdad(): Devuelve un valor logico indicando si es mayor de edad
'''
class Persona:
    def __init__(self, nombre=None, edad=None):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre  # <- NO self.nombre = ...

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad

    def mostrar(self):
        print(self.__dict__)

    def mayor_edad(self):
        return self.edad is not None and self.edad >= 18


persona1 = Persona("Eldo Larito", 25)
print(persona1.mayor_edad())
persona1.mostrar()
