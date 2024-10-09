import proyecto,empleado

class proyecto_empleado(proyecto,empleado):
    def __init__(self,id_proyecto_empleado,id_proyecto,id_empleado):
        super().__init__(id_proyecto,id_empleado)
        self.id_proyecto_empleado = id_proyecto_empleado