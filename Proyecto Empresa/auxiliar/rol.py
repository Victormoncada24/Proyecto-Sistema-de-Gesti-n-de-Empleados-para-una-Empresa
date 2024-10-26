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