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
        