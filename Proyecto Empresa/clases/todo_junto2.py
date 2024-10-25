import mysql.connector

class DatabaseConnection:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="gestion_empleados2"
        )
        self.cursor = self.connection.cursor()

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()

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
        
#nuevo_empleado = Empleado(
#    id=None,  # El ID se puede dejar como None si es autoincremental en la base de datos
#    nombre="Juan Perez",
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

# Insertar el nuevo empleado en la base de datos
#nuevo_empleado.insertar(db)

# Cerrar la conexión
#db.close()

#print("Empleado creado exitosamente.")
    
class TipoEmpleado:
    def __init__(self, id, tipo):
        self.id = id
        self.tipo = tipo

    # Métodos CRUD
    def insertar(self, db):
        query = "INSERT INTO TipoEmpleado (tipo) VALUES (%s)"
        db.cursor.execute(query, (self.tipo,))
        db.commit()

    @staticmethod
    def leer(db, tipo_id):
        query = "SELECT * FROM TipoEmpleado WHERE id = %s"
        db.cursor.execute(query, (tipo_id,))
        return db.cursor.fetchone()

    def actualizar(self, db):
        query = "UPDATE TipoEmpleado SET tipo = %s WHERE id = %s"
        db.cursor.execute(query, (self.tipo, self.id))
        db.commit()

    @staticmethod
    def eliminar(db, tipo_id):
        query = "DELETE FROM TipoEmpleado WHERE id = %s"
        db.cursor.execute(query, (tipo_id,))
        db.commit()


class Departamento:
    def __init__(self, id, nombre, id_empleado):
        self.id = id
        self.nombre = nombre
        self.id_empleado = id_empleado

    # Métodos CRUD
    def insertar(self, db):
        query = "INSERT INTO Departamento (nombre, id_empleado) VALUES (%s, %s)"
        db.cursor.execute(query, (self.nombre, self.id_empleado))
        db.commit()

    @staticmethod
    def leer(db, departamento_id):
        query = "SELECT * FROM Departamento WHERE id = %s"
        db.cursor.execute(query, (departamento_id,))
        return db.cursor.fetchone()

    def actualizar(self, db):
        query = "UPDATE Departamento SET nombre = %s, id_empleado = %s WHERE id = %s"
        db.cursor.execute(query, (self.nombre, self.id_empleado, self.id))
        db.commit()

    @staticmethod
    def eliminar(db, departamento_id):
        query = "DELETE FROM Departamento WHERE id = %s"
        db.cursor.execute(query, (departamento_id,))
        db.commit()

class Proyecto:
    def __init__(self, id, nombre, descripcion, fecha_inicio, fecha_plazo):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.fecha_plazo = fecha_plazo

    # Métodos CRUD
    def insertar(self, db):
        query = "INSERT INTO Proyecto (nombre, descripcion, fecha_inicio, fecha_plazo) VALUES (%s, %s, %s, %s)"
        db.cursor.execute(query, (self.nombre, self.descripcion, self.fecha_inicio, self.fecha_plazo))
        db.commit()

    @staticmethod
    def leer(db, proyecto_id):
        query = "SELECT * FROM Proyecto WHERE id = %s"
        db.cursor.execute(query, (proyecto_id,))
        return db.cursor.fetchone()

    def actualizar(self, db):
        query = "UPDATE Proyecto SET nombre=%s, descripcion=%s, fecha_inicio=%s, fecha_plazo=%s WHERE id=%s"
        db.cursor.execute(query, (self.nombre, self.descripcion, self.fecha_inicio, self.fecha_plazo, self.id))
        db.commit()

    @staticmethod
    def eliminar(db, proyecto_id):
        query = "DELETE FROM Proyecto WHERE id = %s"
        db.cursor.execute(query, (proyecto_id,))
        db.commit()


class RegistroTiempo:
    def __init__(self, id, fecha, cantidad_horas, descripcion, dia_extraordinario, comentario):
        self.id = id
        self.fecha = fecha
        self.cantidad_horas = cantidad_horas
        self.descripcion = descripcion
        self.dia_extraordinario = dia_extraordinario
        self.comentario = comentario

    # Métodos CRUD
    def insertar(self, db):
        query = "INSERT INTO RegistroTiempo (fecha, cantidad_horas, descripcion, dia_extraordinario, comentario) VALUES (%s, %s, %s, %s, %s)"
        db.cursor.execute(query, (self.fecha, self.cantidad_horas, self.descripcion, self.dia_extraordinario, self.comentario))
        db.commit()

    @staticmethod
    def leer(db, registro_id):
        query = "SELECT * FROM RegistroTiempo WHERE id = %s"
        db.cursor.execute(query, (registro_id,))
        return db.cursor.fetchone()

    def actualizar(self, db):
        query = """UPDATE RegistroTiempo SET fecha=%s, cantidad_horas=%s, descripcion=%s, dia_extraordinario=%s, comentario=%s
                   WHERE id=%s"""
        db.cursor.execute(query, (self.fecha, self.cantidad_horas, self.descripcion, self.dia_extraordinario, self.comentario, self.id))
        db.commit()

    @staticmethod
    def eliminar(db, registro_id):
        query = "DELETE FROM RegistroTiempo WHERE id = %s"
        db.cursor.execute(query, (registro_id,))
        db.commit()


class Informe:
    def __init__(self, id, id_empleado, fecha_hora):
        self.id = id
        self.id_empleado = id_empleado
        self.fecha_hora = fecha_hora

    # Métodos CRUD
    def insertar(self, db):
        query = "INSERT INTO Informe (id_empleado, fecha_hora) VALUES (%s, %s)"
        db.cursor.execute(query, (self.id_empleado, self.fecha_hora))
        db.commit()

    @staticmethod
    def leer(db, informe_id):
        query = "SELECT * FROM Informe WHERE id = %s"
        db.cursor.execute(query, (informe_id,))
        return db.cursor.fetchone()

    def actualizar(self, db):
        query = "UPDATE Informe SET id_empleado=%s, fecha_hora=%s WHERE id=%s"
        db.cursor.execute(query, (self.id_empleado, self.fecha_hora, self.id))
        db.commit()

    @staticmethod
    def eliminar(db, informe_id):
        query = "DELETE FROM Informe WHERE id = %s"
        db.cursor.execute(query, (informe_id,))
        db.commit()


class Modulo:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    # Métodos CRUD
    def insertar(self, db):
        query = "INSERT INTO Modulo (nombre) VALUES (%s)"
        db.cursor.execute(query, (self.nombre,))
        db.commit()

    @staticmethod
    def leer(db, modulo_id):
        query = "SELECT * FROM Modulo WHERE id = %s"
        db.cursor.execute(query, (modulo_id,))
        return db.cursor.fetchone()

    def actualizar(self, db):
        query = "UPDATE Modulo SET nombre=%s WHERE id=%s"
        db.cursor.execute(query, (self.nombre, self.id))
        db.commit()

    @staticmethod
    def eliminar(db, modulo_id):
        query = "DELETE FROM Modulo WHERE id = %s"
        db.cursor.execute(query, (modulo_id,))
        db.commit()


class Rol:
    def __init__(self, id, rol, permisos):
        self.id = id
        self.rol = rol
        self.permisos = permisos

    # Métodos CRUD
    def insertar(self, db):
        query = "INSERT INTO Rol (rol, permisos) VALUES (%s, %s)"
        db.cursor.execute(query, (self.rol, self.permisos))
        db.commit()

    @staticmethod
    def leer(db, rol_id):
        query = "SELECT * FROM Rol WHERE id = %s"
        db.cursor.execute(query, (rol_id,))
        return db.cursor.fetchone()

    def actualizar(self, db):
        query = "UPDATE Rol SET rol=%s, permisos=%s WHERE id=%s"
        db.cursor.execute(query, (self.rol, self.permisos, self.id))
        db.commit()

    @staticmethod
    def eliminar(db, rol_id):
        query = "DELETE FROM Rol WHERE id = %s"
        db.cursor.execute(query, (rol_id,))
        db.commit()
