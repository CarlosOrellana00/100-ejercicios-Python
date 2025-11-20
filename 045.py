'''
Ejercicio 45
Imprime la tabla de multiplicar de
un numero ingresado por el resultado
'''
numero = int(input("Ingresa el numero: "))
i = 1

while i <= 10:
  print(f"{numero} x {i} = {numero * i}")
  i = i +1