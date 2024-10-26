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
        