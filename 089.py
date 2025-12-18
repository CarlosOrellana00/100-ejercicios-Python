'''
Ejercicio 89
Comprobar si una palabra es
palindro usando lambda
'''

palindromo = lambda palabra: palabra == palabra [::-1]

print(palindromo("radar"))
print(palindromo("python"))