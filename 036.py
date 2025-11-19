'''
Ejercicio 36
Pide un caracter y determina
si es una vocal
'''
caracter = input("Ingresa caracter: ")
vocales = ['a','e','i','o','u']

if caracter.lower() in vocales:
  print("Es una vocal")
else:
  print("No es una vocal")