'''
Ejercicio 70
Escribe una funcion para
calisificar si una sustancia
es acida, basica o neutra
a partir de su PH
'''

def sustancia(ph):
  if ph < 7:
    return "Acida"
  elif ph > 7:
    return "Basica"
  else:
    return "Neutro"

resultado =sustancia(7)

print(resultado)