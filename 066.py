'''
Ejercicio 66
Escribe una funcion para calcular
el promedio de una lista de numeros
'''
def promedio(lista):
  return sum(lista) /len(lista)

resultado = promedio([4,6,8,10])

print(resultado)