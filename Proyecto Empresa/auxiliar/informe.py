# informe_db_mysql.py
import mysql.connector
from mysql.connector import Error

# Conexión a la base de datos MySQL.
def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',      # Cambia por tu usuario.
            password='', # Cambia por tu contraseña.
            database='empresa'      # Asegúrate de que la BD 'empresa' exista.
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos.")
        return conexion
    except Error as e:
        print(f"Error de conexión: {e}")
        return None

class Informe:
    def generar_informe_empleados(self, conexion):
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, correo, salario, fecha_inicio FROM empleados")
        empleados = cursor.fetchall()

        print("Informe de Empleados:")
        if empleados:
            for emp in empleados:
                print(f"ID: {emp[0]}, Nombre: {emp[1]}, Correo: {emp[2]}, "
                      f"Salario: {emp[3]}, Fecha de Inicio: {emp[4]}")
        else:
            print("No hay empleados registrados.")

    def generar_informe_departamentos(self, conexion):
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre FROM departamentos")
        departamentos = cursor.fetchall()

        print("\nInforme de Departamentos:")
        if departamentos:
            for dep in departamentos:
                print(f"ID: {dep[0]}, Nombre: {dep[1]}")
        else:
            print("No hay departamentos registrados.")

    def generar_informe_proyectos(self, conexion):
        cursor = conexion.cursor()
        cursor.execute("SELECT id, nombre, descripcion, fecha_inicio FROM proyectos")
        proyectos = cursor.fetchall()

        print("\nInforme de Proyectos:")
        if proyectos:
            for proy in proyectos:
                print(f"ID: {proy[0]}, Nombre: {proy[1]}, "
                      f"Descripción: {proy[2]}, Fecha de Inicio: {proy[3]}")
        else:
            print("No hay proyectos registrados.")

# Ejemplo de uso.
if __name__ == "__main__":
    conexion = crear_conexion()
    if conexion:
        informe = Informe()

        # Generar los informes.
        informe.generar_informe_empleados(conexion)
        informe.generar_informe_departamentos(conexion)
        informe.generar_informe_proyectos(conexion)

        # Cerrar la conexión.
        conexion.close()
