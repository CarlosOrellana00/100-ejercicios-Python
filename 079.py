'''
Ejercicio 79
Representa una cuenta bancaria
con deposito y retiuro
debe haber un titular y un sando
Utiliza POO
'''
class Cuenta():
  def __init__(self, titular, saldo):
    self.titular = titular
    self.saldo = saldo

  def depositar(self, cantidad):
    self.saldo += cantidad
    print("Se deposito la cantidad de: $", cantidad)

  def retirar(self, cantidad):
    self.saldo -= cantidad
    print("Se retiro la cantidad de: $", cantidad)

  def mostrar(self):
    print(self.__dict__)

cuenta1 = Cuenta("Eldo Larito", 550)
cuenta1.mostrar()
cuenta1.depositar(1000)
cuenta1.mostrar()
cuenta1.retirar(300)
cuenta1.mostrar()
