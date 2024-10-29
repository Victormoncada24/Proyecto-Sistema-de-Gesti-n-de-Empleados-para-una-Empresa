import mysql.connector
from conn import DatabaseConnection

db = DatabaseConnection()

class Empleado:
    def __init__(self, id, nombre, fecha_contrato, salario, correo, telefono, direccion, id_tipo_empleado, rut, fecha_nac, password, id_rol, id_tipo):
        self.id = id
        self.nombre = nombre
        self.fecha_contrato = fecha_contrato
        self.salario = salario
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
        self.id_tipo_empleado = id_tipo_empleado
        self.rut = rut
        self.fecha_nac = fecha_nac
        self.password = password
        self.id_rol = id_rol
        self.id_tipo = id_tipo

    # Métodos CRUD
    def insertar(self, db):
        query = """INSERT INTO Empleado (nombre, fecha_contrato, salario, correo, telefono, direccion, id_tipo_empleado, rut, fecha_nac, password, id_rol, id_tipo)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (self.nombre, self.fecha_contrato, self.salario, self.correo, self.telefono, self.direccion, self.id_tipo_empleado, self.rut, self.fecha_nac, self.password, self.id_rol, self.id_tipo)
        db.cursor.execute(query, values)
        db.commit()

    @staticmethod
    def leer(db, empleado_id):
        query = "SELECT * FROM Empleado WHERE id = %s"
        db.cursor.execute(query, (empleado_id,))
        return db.cursor.fetchone()

    def actualizar(self, db):
        query = """UPDATE Empleado SET nombre=%s, fecha_contrato=%s, salario=%s, correo=%s, telefono=%s, direccion=%s, id_tipo_empleado=%s, rut=%s, fecha_nac=%s, password=%s, id_rol=%s, id_tipo=%s
                   WHERE id=%s"""
        values = (self.nombre, self.fecha_contrato, self.salario, self.correo, self.telefono, self.direccion, self.id_tipo_empleado, self.rut, self.fecha_nac, self.password, self.id_rol, self.id_tipo, self.id)
        db.cursor.execute(query, values)
        db.commit()

    @staticmethod
    def eliminar(db, empleado_id):
        query = "DELETE FROM Empleado WHERE id = %s"
        db.cursor.execute(query, (empleado_id,))
        db.commit()

    def validar_datos():
        pass

    def validar_edad():
        pass
        hoy = datetime.now()
        edad = hoy.year - self.fecha_nac.year - ((hoy.month, hoy.day) < (self.fecha_nac.month, self.fecha_nac.day))

        if edad >= 18:
            print(f"El empleado {self.nombre} tiene {edad} años y es mayor de edad.")
            return True
        else:
            print(f"El empleado {self.nombre} tiene {edad} años y es menor de edad.")
            return False

    def habilitar_modulos():
        pass    

    def encriptar_password():
        pass

    def desencriptar_password():
        pass