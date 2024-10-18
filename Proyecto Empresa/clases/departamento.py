# departamento.py
class Departamento:
    def __init__(self, nombre, gerente):
        self.nombre = nombre
        self.gerente = gerente
        self.empleados = []

    def agregar_empleado(self, empleado):
        empleado.asignar_departamento(self)
        self.empleados.append(empleado)

    def eliminar_empleado(self, empleado):
        if empleado in self.empleados:
            self.empleados.remove(empleado)
            empleado.departamento = None

    def mostrar_empleados(self):
        return [emp.nombre for emp in self.empleados]
