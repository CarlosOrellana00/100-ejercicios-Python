'''
Ejercicio 093
Filtrar numeros negativos de una lista
utilizando filter
'''
numeros = [-3, 1,-5, 5,-4,8]
negativos = list(filter(lambda x:  x < 0, numeros))

print(negativos)
