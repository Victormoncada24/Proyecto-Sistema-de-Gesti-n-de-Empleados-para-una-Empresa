import tipo_empleado_empleado,tipo_empleado

class empleado():
    def __init__(self,id_empleado,nombre_empleado,fecha_contrato,salario,correo,telefono,direccion,id_tipo_empleado,id_tipo_empleado_emp,rut,fecha_nacimiento,password,id_rol):
        self.id_empleado = id_empleado
        self.nombre_empleado = nombre_empleado
        self.fecha_contrato = fecha_contrato
        self.salario = salario
        self.correo = correo
        self.telefono = telefono
        self.direccion = direccion
        self.id_tipo_empleado = id_tipo_empleado
        self.id_tipo_empleado_emp = id_tipo_empleado_emp
        self.rut = rut
        self.fecha_nacimiento = fecha_nacimiento
        self.password = password
        self.id_rol = id_rol