import mysql.connector
from conn import DatabaseConnection

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