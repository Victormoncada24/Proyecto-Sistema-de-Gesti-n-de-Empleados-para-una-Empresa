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