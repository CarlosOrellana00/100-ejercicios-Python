'''
Ejercicio 69
Escribe una funcion para calcular
la tasa de desmepleo

td = no_desempleados/fuerza laboralx100
'''
def tasa_desempleo(no_emp, si_emp):
  return (no_emp / si_emp) * 100

resultado = tasa_desempleo(100,900)

print(resultado)
