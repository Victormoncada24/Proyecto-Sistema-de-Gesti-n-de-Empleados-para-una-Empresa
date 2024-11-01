from conn import DatabaseConnection
import tipo_empleado

class TipoEmpleadoEmp:
    def __init__(self, id, id_empleado, id_tipo_empleado):
        self.id = id
        self.id_empleado = id_empleado
        self.id_tipo_empleado = id_tipo_empleado

    # Métodos CRUD
    def insertar(self, db):
        query = "INSERT INTO TipoEmpleadoEmp (id_empleado, id_tipo_empleado) VALUES (%s, %s)"
        db.cursor.execute(query, (self.id_empleado, self.id_tipo_empleado))
        db.commit()

    @staticmethod
    def leer(db, tipo_empleado_emp_id):
        query = "SELECT * FROM TipoEmpleadoEmp WHERE id = %s"
        db.cursor.execute(query, (tipo_empleado_emp_id,))
        return db.cursor.fetchone()

    def actualizar(self, db):
        query = "UPDATE TipoEmpleadoEmp SET id_empleado=%s, id_tipo_empleado=%s WHERE id=%s"
        db.cursor.execute(query, (self.id_empleado, self.id_tipo_empleado, self.id))
        db.commit()

    @staticmethod
    def eliminar(db, tipo_empleado_emp_id):
        query = "DELETE FROM TipoEmpleadoEmp WHERE id = %s"
        db.cursor.execute(query, (tipo_empleado_emp_id,))
        db.commit()
        
