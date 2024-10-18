# modulo.py
from clases.empleado import Empleado
from clases.departamento import Departamento
from clases.proyecto import Proyecto
from clases.registro_tiempo import RegistroTiempo

class SistemaGestion:
    def __init__(self):
        self.empleados = []
        self.departamentos = []
        self.proyectos = []

    def agregar_empleado(self, id, nombre, correo, salario, fecha_inicio):
        empleado = Empleado(id, nombre, correo, salario, fecha_inicio)
        self.empleados.append(empleado)
        return empleado

    def agregar_departamento(self, nombre, gerente):
        departamento = Departamento(nombre, gerente)
        self.departamentos.append(departamento)
        return departamento

    def agregar_proyecto(self, nombre, descripcion, fecha_inicio):
        proyecto = Proyecto(nombre, descripcion, fecha_inicio)
        self.proyectos.append(proyecto)
        return proyecto

    def asignar_empleado_a_departamento(self, empleado, departamento):
        departamento.agregar_empleado(empleado)

    def asignar_empleado_a_proyecto(self, empleado, proyecto):
        proyecto.asignar_empleado(empleado)

    def generar_informes(self):
        for emp in self.empleados:
            print(emp.mostrar_informacion())
