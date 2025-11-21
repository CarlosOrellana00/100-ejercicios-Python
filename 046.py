'''
Ejercicio 46
Solicita al usuario ingresar un numero
y cuenta cuantos digitos tiene.
'''
numero = int(input("Ingresa el numero: "))
contador = 0

while numero != 0:
# // es de division entera
  numero = numero // 10
  contador = contador + 1
print("Digitos son:  ", contador)