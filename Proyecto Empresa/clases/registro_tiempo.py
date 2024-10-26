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
