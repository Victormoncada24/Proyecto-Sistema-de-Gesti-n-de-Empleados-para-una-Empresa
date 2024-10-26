import proyecto,empleado

class ProyectoEmpleado:
    def __init__(self, id, id_empleado, id_proyecto):
        self.id = id
        self.id_empleado = id_empleado
        self.id_proyecto = id_proyecto

    # Métodos CRUD
    def insertar(self, db):
        query = "INSERT INTO ProyectoEmpleado (id_empleado, id_proyecto) VALUES (%s, %s)"
        db.cursor.execute(query, (self.id_empleado, self.id_proyecto))
        db.commit()

    @staticmethod
    def leer(db, proyecto_empleado_id):
        query = "SELECT * FROM ProyectoEmpleado WHERE id = %s"
        db.cursor.execute(query, (proyecto_empleado_id,))
        return db.cursor.fetchone()

    def actualizar(self, db):
        query = "UPDATE ProyectoEmpleado SET id_empleado=%s, id_proyecto=%s WHERE id=%s"
        db.cursor.execute(query, (self.id_empleado, self.id_proyecto, self.id))
        db.commit()

    @staticmethod
    def eliminar(db, proyecto_empleado_id):
        query = "DELETE FROM ProyectoEmpleado WHERE id = %s"
        db.cursor.execute(query, (proyecto_empleado_id,))
        db.commit()