'''
Ejercicio 98
Escribir en un archivo HTML
"Hola que tal Autodidacta?
'''
def escribir(nombre_archivo, contenido):
  with open(nombre_archivo,'w') as archivo:
    archivo.write(contenido)

escribir('index.html', 'Hola. que tal autodidacta?')