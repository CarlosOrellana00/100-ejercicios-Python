'''
Ejercicio 60
Imprimir la suma de los
numeros pares del 1 al 10
utilizando el ciclo for
'''

suma_pares = 0
for i in range(1, 11):
  if i % 2 == 0:
    suma_pares = suma_pares + i
    # print(suma_pares)

print("la suma de los numeros pares es: ", suma_pares)