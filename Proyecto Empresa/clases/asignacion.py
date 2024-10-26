class Asignacion:
    def __init__(self, id, id_departamento, id_empleado):
        self.id = id
        self.id_departamento = id_departamento
        self.id_empleado = id_empleado

    # Métodos CRUD
    def insertar(self, db):
        query = "INSERT INTO Asignacion (id_departamento, id_empleado) VALUES (%s, %s)"
        db.cursor.execute(query, (self.id_departamento, self.id_empleado))
        db.commit()

    @staticmethod
    def leer(db, asignacion_id):
        query = "SELECT * FROM Asignacion WHERE id = %s"
        db.cursor.execute(query, (asignacion_id,))
        return db.cursor.fetchone()

    def actualizar(self, db):
        query = "UPDATE Asignacion SET id_departamento=%s, id_empleado=%s WHERE id=%s"
        db.cursor.execute(query, (self.id_departamento, self.id_empleado, self.id))
        db.commit()

    @staticmethod
    def eliminar(db, asignacion_id):
        query = "DELETE FROM Asignacion WHERE id = %s"
        db.cursor.execute(query, (asignacion_id,))
        db.commit()