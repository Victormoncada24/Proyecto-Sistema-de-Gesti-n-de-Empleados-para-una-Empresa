from datetime import datetime 
import tipo_empleado_empleado,tipo_empleado

class empleado():
    def __init__(self,id_empleado,nombre_empleado,fecha_contrato,salario,correo,telefono,direccion,id_tipo_empleado,id_tipo_empleado_emp,rut,fecha_nacimiento,password,cod):
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
        self.cod = cod

    def validar_datos():
        pass

    def validar_edad():
        pass
#        hoy = datetime.now()
#        edad = hoy.year - self.fecha_nac.year - ((hoy.month, hoy.day) < (self.fecha_nac.month, self.fecha_nac.day))

#        if edad >= 18:
#            print(f"El empleado {self.nombre} tiene {edad} años y es mayor de edad.")
#            return True
#        else:
#            print(f"El empleado {self.nombre} tiene {edad} años y es menor de edad.")
#            return False

    def habilitar_modulos():
        pass    

    def encriptar_password():
        pass

    def desencriptar_password():
        pass
