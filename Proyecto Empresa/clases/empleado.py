from conn import DatabaseConnection

db = DatabaseConnection
class Empleado:
    def __init__(self, nombre, fecha_contrato, salario, correo, telefono, direccion, id_tipo_empleado, rut, fecha_nac, password, id_rol):
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

    # Métodos CRUD
    def insertar(self, db):
        query = """INSERT INTO Empleado (nombre, fecha_contrato, salario, correo, telefono, direccion, id_tipo_empleado, rut, fecha_nac, password, id_rol)
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (self.nombre, self.fecha_contrato, self.salario, self.correo, self.telefono, self.direccion, self.id_tipo_empleado, self.rut, self.fecha_nac, self.password, self.id_rol)
        db.cursor.execute(query, values)
        db.commit()

    @staticmethod
    def leer(db, empleado_id):
        query = "SELECT * FROM Empleado WHERE id = %s"
        db.cursor.execute(query, (empleado_id,))
        return db.cursor.fetchone()

    def actualizar(self, db):
        query = """UPDATE Empleado SET id=%s, nombre=%s, fecha_contrato=%s, salario=%s, correo=%s, telefono=%s, direccion=%s, id_tipo_empleado=%s, rut=%s, fecha_nac=%s, password=%s, id_rol=%s
                   WHERE id=%s"""
        values = (self.id, self.nombre, self.fecha_contrato, self.salario, self.correo, self.telefono, self.direccion, self.id_tipo_empleado, self.rut, self.fecha_nac, self.password, self.id_rol, self.id)
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

#nuevo_empleado = Empleado(
#    id=None,  # El ID se puede dejar como None si es autoincremental en la base de datos
#    nombre="Juan Morales",
#    fecha_contrato="2023-10-01",
#    salario=50000,
#    correo="juan.perez@example.com",
#    telefono="123456789",
#    direccion="Calle Falsa 123",
#    id_tipo_empleado=1,
#    rut="12345678-9",
#    fecha_nac="1990-05-20",
#    password="password123",
#    id_rol=1,
#    id_tipo=1
#)

#Insertar el nuevo empleado en la base de datos
#nuevo_empleado.insertar(db)

#Cerrar la conexión
#db.close()

#print("Empleado creado exitosamente.")

# Ejemplo de uso del método eliminar
#empleado_id_a_eliminar = 2  # Cambia este valor por el ID del empleado que quieres eliminar

#Empleado.eliminar(db, empleado_id_a_eliminar)
#print(f"Empleado con ID {empleado_id_a_eliminar} eliminado.")    