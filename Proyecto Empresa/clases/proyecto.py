# proyecto_db_mysql.py
import mysql.connector
from mysql.connector import Error

# Conexión a la base de datos MySQL.
def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',      # Cambia esto por tu usuario de MySQL.
            password='', # Cambia por tu contraseña.
            database='empresa'      # Asegúrate de tener una base de datos llamada 'empresa'.
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos.")
        return conexion
    except Error as e:
        print(f"Error de conexión: {e}")
        return None

# Crear tablas (proyectos y relación empleados-proyectos).
def crear_tablas(conexion):
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS proyectos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            descripcion TEXT,
            fecha_inicio DATE NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS proyecto_empleado (
            proyecto_id INT,
            empleado_id INT,
            PRIMARY KEY (proyecto_id, empleado_id),
            FOREIGN KEY (proyecto_id) REFERENCES proyectos(id) ON DELETE CASCADE,
            FOREIGN KEY (empleado_id) REFERENCES empleados(id) ON DELETE CASCADE
        )
    ''')
    conexion.commit()
    print("Tablas 'proyectos' y 'proyecto_empleado' creadas o ya existen.")

# Función para crear un proyecto.
def crear_proyecto(conexion, nombre, descripcion, fecha_inicio):
    try:
        cursor = conexion.cursor()
        cursor.execute('''
            INSERT INTO proyectos (nombre, descripcion, fecha_inicio)
            VALUES (%s, %s, %s)
        ''', (nombre, descripcion, fecha_inicio))
        conexion.commit()
        print(f"Proyecto '{nombre}' creado exitosamente.")
    except Error as e:
        print(f"Error al crear el proyecto: {e}")

# Función para actualizar un proyecto.
def actualizar_proyecto(conexion, id, nombre=None, descripcion=None, fecha_inicio=None):
    cursor = conexion.cursor()
    query = "UPDATE proyectos SET "
    parametros = []

    if nombre:
        query += "nombre = %s, "
        parametros.append(nombre)
    if descripcion:
        query += "descripcion = %s, "
        parametros.append(descripcion)
    if fecha_inicio:
        query += "fecha_inicio = %s, "
        parametros.append(fecha_inicio)

    query = query.rstrip(', ') + " WHERE id = %s"
    parametros.append(id)

    cursor.execute(query, tuple(parametros))
    conexion.commit()
    print(f"Proyecto con ID {id} actualizado exitosamente.")

# Función para eliminar un proyecto.
def eliminar_proyecto(conexion, id):
    cursor = conexion.cursor()
    cursor.execute('DELETE FROM proyectos WHERE id = %s', (id,))
    conexion.commit()
    print(f"Proyecto con ID {id} eliminado exitosamente.")

# Función para asignar un empleado a un proyecto.
def asignar_empleado_a_proyecto(conexion, proyecto_id, empleado_id):
    try:
        cursor = conexion.cursor()
        cursor.execute('''
            INSERT INTO proyecto_empleado (proyecto_id, empleado_id)
            VALUES (%s, %s)
        ''', (proyecto_id, empleado_id))
        conexion.commit()
        print(f"Empleado {empleado_id} asignado al proyecto {proyecto_id}.")
    except Error as e:
        print(f"Error al asignar empleado: {e}")

# Función para desasignar un empleado de un proyecto.
def desasignar_empleado_de_proyecto(conexion, proyecto_id, empleado_id):
    cursor = conexion.cursor()
    cursor.execute('''
        DELETE FROM proyecto_empleado 
        WHERE proyecto_id = %s AND empleado_id = %s
    ''', (proyecto_id, empleado_id))
    conexion.commit()
    print(f"Empleado {empleado_id} desasignado del proyecto {proyecto_id}.")

# Función para mostrar los empleados asignados a un proyecto.
def mostrar_empleados_asignados(conexion, proyecto_id):
    cursor = conexion.cursor()
    cursor.execute('''
        SELECT e.id, e.nombre 
        FROM empleados e
        JOIN proyecto_empleado pe ON e.id = pe.empleado_id
        WHERE pe.proyecto_id = %s
    ''', (proyecto_id,))
    empleados = cursor.fetchall()
    if empleados:
        for emp in empleados:
            print(f"ID: {emp[0]}, Nombre: {emp[1]}")
    else:
        print("No hay empleados asignados a este proyecto.")

# Función para mostrar todos los proyectos.
def mostrar_todos_los_proyectos(conexion):
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM proyectos')
    proyectos = cursor.fetchall()
    if proyectos:
        for proyecto in proyectos:
            print(f"ID: {proyecto[0]}, Nombre: {proyecto[1]}, "
                  f"Descripción: {proyecto[2]}, Fecha de Inicio: {proyecto[3]}")
    else:
        print("No hay proyectos registrados.")

# Ejemplo de uso.
if __name__ == "__main__":
    conexion = crear_conexion()
    if conexion:
        crear_tablas(conexion)

        # Crear proyectos.
        crear_proyecto(conexion, "Proyecto Alpha", "Descripción del Proyecto Alpha", "2024-10-01")
        crear_proyecto(conexion, "Proyecto Beta", "Descripción del Proyecto Beta", "2024-11-01")

        # Mostrar todos los proyectos.
        mostrar_todos_los_proyectos(conexion)

        # Asignar empleados a proyectos.
        asignar_empleado_a_proyecto(conexion, 1, 1)  # Asigna empleado 1 al proyecto 1.
        asignar_empleado_a_proyecto(conexion, 1, 2)  # Asigna empleado 2 al proyecto 1.

        # Mostrar empleados asignados al proyecto 1.
        print("Empleados asignados al proyecto 1:")
        mostrar_empleados_asignados(conexion, 1)

        # Actualizar proyecto.
        actualizar_proyecto(conexion, 1, descripcion="Descripción actualizada del Proyecto Alpha")

        # Eliminar proyecto.
        eliminar_proyecto(conexion, 2)

        # Mostrar proyectos después de eliminar.
        mostrar_todos_los_proyectos(conexion)

        # Cerrar la conexión al final.
        conexion.close()
