from empleado import Empleado
from departamento import Departamento

# Crear un empleado
empleado = Empleado(nombre="Juan Perez", direccion="Calle 123", telefono="12345678", email="juan@correo.com", salario=1000, id_departamento=1)
empleado.crear()

# Leer todos los empleados
empleados = Empleado.leer_todos()
for emp in empleados:
    print(emp)

# Actualizar un empleado
empleado.id_empleado = 1  # Suponiendo que el ID es 1
empleado.nombre = "Juan Pérez Actualizado"
empleado.salario = 1200
empleado.actualizar()

# Eliminar un empleado
empleado.eliminar()

# Crear un departamento
departamento = Departamento(nombre="Desarrollo", gerente="Carlos Manager")
departamento.crear()

# Leer todos los departamentos
departamentos = Departamento.leer_todos()
for dep in departamentos:
    print(dep)
