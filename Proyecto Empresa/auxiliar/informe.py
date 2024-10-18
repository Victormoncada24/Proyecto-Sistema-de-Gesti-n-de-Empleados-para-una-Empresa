# informe.py
class Informe:
    def generar_informe_empleados(self, empleados):
        print("Informe de Empleados:")
        for emp in empleados:
            print(emp)

    def generar_informe_departamentos(self, departamentos):
        print("\nInforme de Departamentos:")
        for dep in departamentos:
            print(dep)

    def generar_informe_proyectos(self, proyectos):
        print("\nInforme de Proyectos:")
        for proy in proyectos:
            print(proy)
