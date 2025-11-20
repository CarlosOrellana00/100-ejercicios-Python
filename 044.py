'''
Ejercicio 44
Genera un numero aleatorio entre 1 y 10.
luego, pide al usuario adivinar el
numero hasta que lo haga correctamente
'''
import random
numero_secreto = random.random(1,10)
intentos = 0

while True:
  intento = int(input("Adivina el numwero"))
  intentos = intento + 1
  if intento  == numero_secreto:
    print(f"felicidades, adivinaste. solo te tomo {intentos} intentos lograrlo")
    break