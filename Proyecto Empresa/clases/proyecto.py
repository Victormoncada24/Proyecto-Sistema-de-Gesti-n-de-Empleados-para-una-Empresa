# proyecto.py
class Proyecto:
    def __init__(self, nombre, descripcion, fecha_inicio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha_inicio = fecha_inicio
        self.empleados_asignados = []

    def asignar_empleado(self, empleado):
        if empleado not in self.empleados_asignados:
            self.empleados_asignados.append(empleado)

    def desasignar_empleado(self, empleado):
        if empleado in self.empleados_asignados:
            self.empleados_asignados.remove(empleado)

    def mostrar_empleados(self):
        return [emp.nombre for emp in self.empleados_asignados]
