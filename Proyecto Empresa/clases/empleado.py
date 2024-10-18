# empleado.py
class Empleado:
    def __init__(self, id, nombre, correo, salario, fecha_inicio):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.salario = salario
        self.fecha_inicio = fecha_inicio
        self.departamento = None

    def asignar_departamento(self, departamento):
        self.departamento = departamento

    def mostrar_informacion(self):
        return (f"ID: {self.id}, Nombre: {self.nombre}, Correo: {self.correo}, "
                f"Salario: {self.salario}, Fecha de Inicio: {self.fecha_inicio}, "
                f"Departamento: {self.departamento.nombre if self.departamento else 'Ninguno'}")


    def desencriptar_password():
        pass
