'''
Ejercicio 40
Calcular el Indice de Masa Corporal e interpretarlo
'''
peso = 70
altura = 1.75

imc = peso /(altura ** 2)

print(imc)

if imc < 18.5:
  print("Peso Bajo")
elif imc < 25:
  print("Peso Normal")
elif imc < 30:
  print("Sobrepeso")
elif imc < 35:
  print("Obesidad Grado 1")
elif imc < 40:
  print("Obesidad Grado 2")
else:
  print("Obesidad grado 3")
