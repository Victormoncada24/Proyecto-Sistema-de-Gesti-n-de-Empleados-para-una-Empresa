import tipo_empleado

class tipo_empleado_emp(tipo_empleado):
    def __init__(self,id_tipo_empleado_emp,id_tipo_empleado):
        super().__init__(id_tipo_empleado)
        self.id_tipo_empleado_emp = id_tipo_empleado_emp
        
