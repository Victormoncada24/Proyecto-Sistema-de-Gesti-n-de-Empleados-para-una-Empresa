from conn import DatabaseConnection
db = DatabaseConnection
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