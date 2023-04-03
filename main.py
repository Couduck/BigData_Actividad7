# Importaciones del conector y random
import mysql.connector as mysql
import random as r

def creacionDByTablas():

    db =mysql.connect(
        host="localhost",
        user="root",
        passwd="",
    )

    cursor = db.cursor()

    # Definición del nombre de la base de datos
    nombre = "bigData_Actividad7"


    # Base de Datos creada en caso de no existir
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {nombre}")
    db.database = nombre

    # Tablas creadas en caso de no existir
    cursor.execute("CREATE TABLE IF NOT EXISTS tabla_pasajeros1"
                   "(id int PRIMARY KEY NOT NULL AUTO_INCREMENT,"
                   " cabina VARCHAR(10) NOT NULL,"
                   " supervivencia ENUM('1', '0') NOT NULL)")

    cursor.execute("CREATE TABLE IF NOT EXISTS tabla_pasajeros2"
                   "(id int PRIMARY KEY NOT NULL AUTO_INCREMENT,"
                   " cabina VARCHAR(10) NOT NULL,"
                   " supervivencia ENUM('1', '0') NOT NULL)")

def insercionDatos():
    # Arreglo con el nombre de las tablas a usar
    tablas = ["tabla_pasajeros1","tabla_pasajeros2"]

    # Conector
    db = mysql.connect(
        host="localhost",
        user="root",
        passwd="",
        database="bigData_Actividad7"
    )

    cursor = db.cursor(buffered=True)

    # Se comprueba que no haya registros en una de las tablas, si los hay, solo se imprime la información de ambas
    cursor.execute("SELECT * FROM tabla_pasajeros1")

    # Por cada tabla se añaden 100 registros aleatorizados
    if cursor.rowcount == 0:
        for i in range(0, 2):
            for j in range(0, 100):
                cabina = generarCabina()
                supervivencia = generarSupervivencia()
                cursor.execute(f"INSERT INTO {tablas[i]} (cabina, supervivencia) VALUES (%s, %s)",(cabina, supervivencia))
        db.commit()

    # Se imprime la información de las tablas
    print("-----------------------------\nTabla de pasajeros 1\n\n")
    cursor.execute("SELECT * FROM tabla_pasajeros1")
    for x in cursor:
        print(x)
    print("-----------------------------\n\n")

    print("-----------------------------\nTabla de pasajeros 2\n\n")
    cursor.execute("SELECT * FROM tabla_pasajeros2")
    for x in cursor:
        print(x)
    print("-----------------------------\n\n")

    db.close()

# Metodo para la generación de cabinas aleatorias
def generarCabina():
    letras = ['A', 'B', 'C', 'D', 'E', 'F']

    indexLetras = r.randint(0,5)
    numeroCabina = r.randint(1,110)

    cabinaCompleta = letras[indexLetras] + "-" + str(numeroCabina)

    return cabinaCompleta

# Metodo para la generación de estados de supervivencia aleatorios
def generarSupervivencia():
    return str(r.randint(0,1))


# Ejecución métodos principales
creacionDByTablas()
insercionDatos()
