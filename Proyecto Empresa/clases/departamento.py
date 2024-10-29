# departamento_db_mysql.py
import mysql.connector
from mysql.connector import Error

class Departamento:
    def __init__(self, id=None, nombre=None, gerente=None):
        self.id = id
        self.nombre = nombre
        self.gerente = gerente
        self.empleados = []

    # Agregar empleado al departamento (solo en memoria)
    def agregar_empleado(self, empleado):
        empleado.asignar_departamento(self)
        self.empleados.append(empleado)

    # Eliminar empleado del departamento (solo en memoria)
    def eliminar_empleado(self, empleado):
        if empleado in self.empleados:
            self.empleados.remove(empleado)
            empleado.departamento = None

    # Mostrar empleados del departamento
    def mostrar_empleados(self):
        return [emp.nombre for emp in self.empleados]

    # Agregar un departamento a la base de datos
    @staticmethod
    def agregar_departamento(conexion, nombre, gerente):
        try:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO departamentos (nombre) VALUES (%s)", (nombre,)
            )
            conexion.commit()
            print(f"Departamento '{nombre}' agregado exitosamente.")
        except Error as e:
            print(f"Error al agregar departamento: {e}")

    # Actualizar información de un departamento
    @staticmethod
    def actualizar_departamento(conexion, departamento_id, nuevo_nombre, nuevo_gerente):
        try:
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE departamentos SET nombre = %s, gerente = %s WHERE id = %s",
                (nuevo_nombre, nuevo_gerente, departamento_id)
            )
            conexion.commit()
            print(f"Departamento ID {departamento_id} actualizado exitosamente.")
        except Error as e:
            print(f"Error al actualizar departamento: {e}")

    # Eliminar un departamento de la base de datos
    @staticmethod
    def eliminar_departamento(conexion, departamento_id):
        try:
            cursor = conexion.cursor()
            cursor.execute(
                "DELETE FROM departamentos WHERE id = %s", (departamento_id,)
            )
            conexion.commit()
            print(f"Departamento ID {departamento_id} eliminado exitosamente.")
        except Error as e:
            print(f"Error al eliminar departamento: {e}")

# Función para crear la conexión a la base de datos
def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',      
            password='', 
            database='empresa'      
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos.")
        return conexion
    except Error as e:
        print(f"Error de conexión: {e}")
        return None

# Ejemplo de uso
if __name__ == "__main__":
    conexion = crear_conexion()
    if conexion:
        # Agregar un departamento
        Departamento.agregar_departamento(conexion, "Recursos Humanos", "Carlos García")

        # Actualizar el departamento
        Departamento.actualizar_departamento(conexion, 1, "RRHH", "María López")

        # Eliminar un departamento
        Departamento.eliminar_departamento(conexion, 1)

        # Cerrar la conexión
        conexion.close()
