# registro_tiempo_db_mysql.py
import mysql.connector
from mysql.connector import Error

# Conexión a la base de datos MySQL.
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

# Crear la tabla para registros de tiempo.
def crear_tabla_registro_tiempo(conexion):
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS registro_tiempo (
            id INT AUTO_INCREMENT PRIMARY KEY,
            empleado_id INT NOT NULL,
            proyecto_id INT NOT NULL,
            fecha DATE NOT NULL,
            horas DECIMAL(5, 2) NOT NULL,
            descripcion TEXT,
            FOREIGN KEY (empleado_id) REFERENCES empleados(id) ON DELETE CASCADE,
            FOREIGN KEY (proyecto_id) REFERENCES proyectos(id) ON DELETE CASCADE
        )
    ''')
    conexion.commit()
    print("Tabla 'registro_tiempo' creada o ya existe.")

# Función para registrar el tiempo de un empleado en un proyecto.
def crear_registro_tiempo(conexion, empleado_id, proyecto_id, fecha, horas, descripcion):
    try:
        cursor = conexion.cursor()
        cursor.execute('''
            INSERT INTO registro_tiempo (empleado_id, proyecto_id, fecha, horas, descripcion)
            VALUES (%s, %s, %s, %s, %s)
        ''', (empleado_id, proyecto_id, fecha, horas, descripcion))
        conexion.commit()
        print(f"Registro de tiempo creado para el empleado {empleado_id} en el proyecto {proyecto_id}.")
    except Error as e:
        print(f"Error al crear el registro de tiempo: {e}")

# Función para actualizar un registro de tiempo.
def actualizar_registro_tiempo(conexion, id, horas=None, descripcion=None):
    cursor = conexion.cursor()
    query = "UPDATE registro_tiempo SET "
    parametros = []

    if horas:
        query += "horas = %s, "
        parametros.append(horas)
    if descripcion:
        query += "descripcion = %s, "
        parametros.append(descripcion)

    query = query.rstrip(', ') + " WHERE id = %s"
    parametros.append(id)

    cursor.execute(query, tuple(parametros))
    conexion.commit()
    print(f"Registro de tiempo con ID {id} actualizado exitosamente.")

# Función para eliminar un registro de tiempo.
def eliminar_registro_tiempo(conexion, id):
    cursor = conexion.cursor()
    cursor.execute('DELETE FROM registro_tiempo WHERE id = %s', (id,))
    conexion.commit()
    print(f"Registro de tiempo con ID {id} eliminado exitosamente.")

# Función para mostrar los registros de tiempo de un proyecto.
def mostrar_registros_por_proyecto(conexion, proyecto_id):
    cursor = conexion.cursor()
    cursor.execute('''
        SELECT r.id, e.nombre, r.fecha, r.horas, r.descripcion
        FROM registro_tiempo r
        JOIN empleados e ON r.empleado_id = e.id
        WHERE r.proyecto_id = %s
    ''', (proyecto_id,))
    registros = cursor.fetchall()

    if registros:
        for reg in registros:
            print(f"ID: {reg[0]}, Empleado: {reg[1]}, Fecha: {reg[2]}, "
                  f"Horas: {reg[3]}, Descripción: {reg[4]}")
    else:
        print(f"No hay registros de tiempo para el proyecto {proyecto_id}.")

# Función para mostrar todos los registros de tiempo.
def mostrar_todos_los_registros(conexion):
    cursor = conexion.cursor()
    cursor.execute('''
        SELECT r.id, e.nombre, p.nombre, r.fecha, r.horas, r.descripcion
        FROM registro_tiempo r
        JOIN empleados e ON r.empleado_id = e.id
        JOIN proyectos p ON r.proyecto_id = p.id
    ''')
    registros = cursor.fetchall()

    if registros:
        for reg in registros:
            print(f"ID: {reg[0]}, Empleado: {reg[1]}, Proyecto: {reg[2]}, "
                  f"Fecha: {reg[3]}, Horas: {reg[4]}, Descripción: {reg[5]}")
    else:
        print("No hay registros de tiempo disponibles.")

# Ejemplo de uso.
if __name__ == "__main__":
    conexion = crear_conexion()
    if conexion:
        crear_tabla_registro_tiempo(conexion)

        # Crear registros de tiempo.
        crear_registro_tiempo(conexion, 1, 1, "2024-10-28", 8.0, "Desarrollo del módulo A")
        crear_registro_tiempo(conexion, 2, 1, "2024-10-28", 6.5, "Pruebas de integración")

        # Mostrar todos los registros de tiempo.
        print("Registros de tiempo:")
        mostrar_todos_los_registros(conexion)

        # Actualizar un registro.
        actualizar_registro_tiempo(conexion, 1, horas=8.5, descripcion="Actualización del módulo A")

        # Mostrar registros por proyecto.
        print("Registros del proyecto 1:")
        mostrar_registros_por_proyecto(conexion, 1)

        # Eliminar un registro.
        eliminar_registro_tiempo(conexion, 2)

        # Mostrar todos los registros después de la eliminación.
        mostrar_todos_los_registros(conexion)

        # Cerrar la conexión al final.
        conexion.close()
