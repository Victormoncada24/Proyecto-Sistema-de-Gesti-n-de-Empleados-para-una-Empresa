from conexion import obtener_conexion

class Empleado:
    def _init_(self,id_empleado,nombre,direccion,telefono,email,salario,id_departamento):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email
        self.salario = salario
        self.id_departamento = id_departamento

    def crear(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        sql = """
            INSERT INTO empleados (nombre, direccion, telefono, email, salario, id_departamento) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (self.nombre, self.direccion, self.telefono, self.email, self.salario, self.id_departamento))
        conexion.commit()
        cursor.close()
        conexion.close()

    @staticmethod
    def leer_todos():
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM empleados")
        empleados = cursor.fetchall()
        cursor.close()
        conexion.close()
        return empleados

    def actualizar(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        sql = "UPDATE empleados SET nombre = %s, salario = %s WHERE id_empleado = %s"
        cursor.execute(sql, (self.nombre, self.salario, self.id_empleado))
        conexion.commit()
        cursor.close()
        conexion.close()

    def eliminar(self):
        conexion = obtener_conexion()
        cursor = conexion.cursor()
        sql = "DELETE FROM empleados WHERE id_empleado = %s"
        cursor.execute(sql, (self.id_empleado,))
        conexion.commit()
        cursor.close()
        conexion.close()
