# empleado_db_mysql.py
import mysql.connector
from mysql.connector import Error

# Conexión a la base de datos MySQL.
def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',     # Cambia 'tu_usuario' por tu usuario de MySQL.
            password='', # Cambia 'tu_contraseña' por tu contraseña.
            database='empresa'     # Asegúrate de tener una base de datos llamada 'empresa'.
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos.")
        return conexion
    except Error as e:
        print(f"Error de conexión: {e}")
        return None

# Función para crear la tabla de empleados si no existe.
def crear_tabla(conexion):
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS empleados (
            id INT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            correo VARCHAR(100) UNIQUE NOT NULL,
            salario DECIMAL(10, 2) NOT NULL,
            fecha_inicio DATE NOT NULL
        )
    ''')
    conexion.commit()
    print("Tabla 'empleados' creada o ya existe.")


# Función para crear un empleado.
def crear_empleado(conexion, id, nombre, correo, salario, fecha_inicio):
    try:
        cursor = conexion.cursor()
        cursor.execute('''
            INSERT INTO empleados (id, nombre, correo, salario, fecha_inicio)
            VALUES (%s, %s, %s, %s, %s)
        ''', (id, nombre, correo, salario, fecha_inicio))
        conexion.commit()
        print(f"Empleado {nombre} creado exitosamente.")
    except Error as e:
        print(f"Error al crear el empleado: {e}")


# Función para actualizar un empleado.
def actualizar_empleado(conexion, id, nombre=None, correo=None, salario=None, fecha_inicio=None):
    cursor = conexion.cursor()
    empleado = buscar_empleado_por_id(conexion, id)
    if empleado:
        query = "UPDATE empleados SET "
        parametros = []
        if nombre:
            query += "nombre = %s, "
            parametros.append(nombre)
        if correo:
            query += "correo = %s, "
            parametros.append(correo)
        if salario:
            query += "salario = %s, "
            parametros.append(salario)
        if fecha_inicio:
            query += "fecha_inicio = %s, "
            parametros.append(fecha_inicio)

        query = query.rstrip(', ') + " WHERE id = %s"
        parametros.append(id)

        cursor.execute(query, tuple(parametros))
        conexion.commit()
        print(f"Empleado con ID {id} actualizado exitosamente.")
    else:
        print(f"No se encontró un empleado con ID {id}.")


# Función para eliminar un empleado.
def eliminar_empleado(conexion, id):
    cursor = conexion.cursor()
    cursor.execute('DELETE FROM empleados WHERE id = %s', (id,))
    conexion.commit()
    print(f"Empleado con ID {id} eliminado exitosamente.")


# Función para buscar un empleado por ID.
def buscar_empleado_por_id(conexion, id):
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM empleados WHERE id = %s', (id,))
    return cursor.fetchone()


# Función para mostrar todos los empleados.
def mostrar_todos_los_empleados(conexion):
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM empleados')
    empleados = cursor.fetchall()
    if empleados:
        for emp in empleados:
            print(f"ID: {emp[0]}, Nombre: {emp[1]}, Correo: {emp[2]}, "
                  f"Salario: {emp[3]}, Fecha de Inicio: {emp[4]}")
    else:
        print("No hay empleados registrados.")


# Ejemplo de uso.
if __name__ == "__main__":
    conexion = crear_conexion()
    if conexion:
        crear_tabla(conexion)

        # Crear empleados.
        crear_empleado(conexion, 1, "Ana", "ana@email.com", 50000, "2024-01-10")
        crear_empleado(conexion, 2, "Luis", "luis@email.com", 45000, "2023-11-05")

        # Mostrar todos los empleados.
        mostrar_todos_los_empleados(conexion)

        # Actualizar un empleado.
        actualizar_empleado(conexion, 1, nombre="Ana María", salario=52000)

        # Mostrar información actualizada.
        mostrar_todos_los_empleados(conexion)

        # Eliminar un empleado.
        eliminar_empleado(conexion, 2)

        # Mostrar la lista después de eliminar.
        mostrar_todos_los_empleados(conexion)

        # Cerrar la conexión al final.
        conexion.close()
