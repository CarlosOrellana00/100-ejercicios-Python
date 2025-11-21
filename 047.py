'''
Ejercicio 47
Hacer un menu de opciones que incluya la opcion
de salir del programa
'''
while True:
  print("1.- Sumar")
  print("2.- Restar")
  print("3.- Salir")

  opcion = int(input("Escribe tu opcion: "))

  if opcion == 1:
    print("Opcion Sumar")
  elif opcion == 2:
    print("opcion Restar")
  elif opcion == 3:
    break
  else:
    print("Opcion no valida")

print("Nos Vemos")
