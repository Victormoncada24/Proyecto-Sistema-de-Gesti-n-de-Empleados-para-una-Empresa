from conexion import obtener_conexion

def crear_proyecto(nombre, descripcion, fecha_inicio):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "INSERT INTO proyectos (nombre, descripcion, fecha_inicio) VALUES (%s, %s, %s)"
    cursor.execute(sql, (nombre, descripcion, fecha_inicio))
    conexion.commit()
    cursor.close()
    conexion.close()

def leer_proyectos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM proyectos")
    proyectos = cursor.fetchall()
    cursor.close()
    conexion.close()
    return proyectos

def actualizar_proyecto(id_proyecto, nombre):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "UPDATE proyectos SET nombre = %s WHERE id_proyecto = %s"
    cursor.execute(sql, (nombre, id_proyecto))
    conexion.commit()
    cursor.close()
    conexion.close()

def eliminar_proyecto(id_proyecto):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "DELETE FROM proyectos WHERE id_proyecto = %s"
    cursor.execute(sql, (id_proyecto,))
    conexion.commit()
    cursor.close()
    conexion.close()