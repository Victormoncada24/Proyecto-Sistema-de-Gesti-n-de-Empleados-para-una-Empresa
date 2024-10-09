import departamento,empleado

class asignacion(departamento,empleado):
    def __init__(self,id_asignacion,id_departamento,id_empleado):
        super().__init__(id_departamento,id_empleado)
        self.id_asignacion = id_asignacion