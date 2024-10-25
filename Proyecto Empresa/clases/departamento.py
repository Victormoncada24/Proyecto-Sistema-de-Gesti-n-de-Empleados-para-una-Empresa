from conexion import obtener_conexion

class Departamento:
    def _init_(self,id_departamento,nombre,gerente):
        self.id_departamento = id_departamento
        self.nombre = nombre
        self.gerente = gerente

    def crear(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        sql = "INSERT INTO departamentos (nombre, gerente) VALUES (%s, %s)"
        cursor.execute(sql, (self.nombre, self.gerente))
        conexion.commit()
        cursor.close()
        conexion.close()

    @staticmethod
    def leer_todos():
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM departamentos")
        departamentos = cursor.fetchall()
        cursor.close()
        conexion.close()
        return departamentos

    def actualizar(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        sql = "UPDATE departamentos SET nombre = %s WHERE id_departamento = %s"
        cursor.execute(sql, (self.nombre, self.id_departamento))
        conexion.commit()
        cursor.close()
        conexion.close()

    def eliminar(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        sql = "DELETE FROM departamentos WHERE id_departamento = %s"
        cursor.execute(sql, (self.id_departamento,))
        conexion.commit()
        cursor.close()
        conexion.close()
