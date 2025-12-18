'''
Ejercicio 100
Conectarte a una base de datos mysql, hacer
una consulta a una tabla y mostrar la informacion
en la consola
'''
import mysql.connector

class Conexion:
  def conectar(self):
    conexion = mysql.connector.connect(
      host='localhost',
      user='root',
      password='',
      database='visitas'
    )
    return conexion

class Visitas(Conexion):
  def consulta_select(self):
    conexion = self.conectar()
    sql = "SELECT id, ap_paterno FROM t_visitas"
    cursor = conexion.cursor()
    cursor.execute(sql)
    registros = cursor.fetchall()
    cursor.close()
    conexion.close()
    return registros

  def imprimir_datos(self):
    datos = self.consulta_select()
    for fila in datos:
      print(fila)

visita = Visitas()
visita.imprimir_datos()