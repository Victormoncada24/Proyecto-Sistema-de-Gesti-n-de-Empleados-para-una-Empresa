from conexion import obtener_conexion

def crear_registro(id_empleado, id_proyecto, fecha, horas_trabajadas, descripcion):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = """
        INSERT INTO registro_tiempo (id_empleado, id_proyecto, fecha, horas_trabajadas, descripcion) 
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (id_empleado, id_proyecto, fecha, horas_trabajadas, descripcion))
    conexion.commit()
    cursor.close()
    conexion.close()

def leer_registros():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM registro_tiempo")
    registros = cursor.fetchall()
    cursor.close()
    conexion.close()
    return registros

def actualizar_registro(id_registro, horas_trabajadas):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "UPDATE registro_tiempo SET horas_trabajadas = %s WHERE id_registro = %s"
    cursor.execute(sql, (horas_trabajadas, id_registro))
    conexion.commit()
    cursor.close()
    conexion.close()

def eliminar_registro(id_registro):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    sql = "DELETE FROM registro_tiempo WHERE id_registro = %s"
    cursor.execute(sql, (id_registro,))
    conexion.commit()
    cursor.close()
    conexion.close()