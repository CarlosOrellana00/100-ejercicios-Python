'''
Ejercicio 33
Determina si un año es biciesto
Reglas de Negocio:
  - Divisible por 4.
  - No divisible por 100
  - Divisible por 400
'''
anyo = 2025

if (anyo % 4 == 0 and anyo  % 100 != 0) or \
    (anyo % 400 == 0):
    print("Es Año Bisiesto")
else:
  print("NO es Año Bisiesto")