# registro_tiempo.py
class RegistroTiempo:
    def __init__(self, empleado, proyecto, fecha, horas, descripcion):
        self.empleado = empleado
        self.proyecto = proyecto
        self.fecha = fecha
        self.horas = horas
        self.descripcion = descripcion

    def mostrar_registro(self):
        return (f"{self.empleado.nombre} trabajó {self.horas} horas en '{self.proyecto.nombre}' "
                f"el {self.fecha}: {self.descripcion}")
