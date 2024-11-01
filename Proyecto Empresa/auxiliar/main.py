from conn import DatabaseConnection
from empleado import Empleado
#from asignacion import Asignacion
#from departamento import Departamento
#from proyecto import Proyecto
#from registro_tiempo import RegistroTiempo
#from tipo_empleado import TipoEmpleado

def menu():
    print("Seleccione una opción:")
    print("1. Agregar Empleado")
    print("2. Leer Empleado")
    print("3. Actualizar Empleado")
    print("4. Eliminar Empleado")
    print("5. Salir")

def agregar_empleado(db):
    id = input("ID:")
    nombre = input("Nombre: ")
    fecha_contrato = input("Fecha de contrato (YYYY-MM-DD): ")
    salario = float(input("Salario: "))
    correo = input("Correo: ")
    telefono = input("Teléfono: ")
    direccion = input("Dirección: ")
    id_tipo_empleado = int(input("ID Tipo Empleado: "))
    rut = input("RUT: ")
    fecha_nac = input("Fecha de nacimiento (YYYY-MM-DD): ")
    password = input("Contraseña: ")
    id_rol = int(input("ID Rol: "))
    id_tipo = int(input("ID Tipo: "))
    
    empleado = Empleado(id, nombre, fecha_contrato, salario, correo, telefono, direccion, id_tipo_empleado, rut, fecha_nac, password, id_rol, id_tipo)
    empleado.insertar(db)
    print("Empleado agregado exitosamente.")

def leer_empleado(db):
    empleado_id = int(input("ID del empleado a consultar: "))
    empleado = Empleado.leer(db, empleado_id)
    if empleado:
        print("Datos del empleado:", empleado)
    else:
        print("Empleado no encontrado.")

def actualizar_empleado(db):
    empleado_id = int(input("ID del empleado a actualizar: "))
    empleado = Empleado.leer(db, empleado_id)
    if empleado:
        id = input("ID:")
        nombre = input("Nombre: ")
        fecha_contrato = input("Fecha de contrato (YYYY-MM-DD): ")
        salario = float(input("Salario: "))
        correo = input("Correo: ")
        telefono = input("Teléfono: ")
        direccion = input("Dirección: ")
        id_tipo_empleado = int(input("ID Tipo Empleado: "))
        rut = input("RUT: ")
        fecha_nac = input("Fecha de nacimiento (YYYY-MM-DD): ")
        password = input("Contraseña: ")
        id_rol = int(input("ID Rol: "))
        id_tipo = int(input("ID Tipo: "))
        
        empleado = Empleado(empleado_id, nombre, fecha_contrato, salario, correo, telefono, direccion, id_tipo_empleado, rut, fecha_nac, password, id_rol, id_tipo)
        empleado.actualizar(db)
        print("Empleado actualizado exitosamente.")
    else:
        print("Empleado no encontrado.")

def eliminar_empleado(db):
    empleado_id = int(input("ID del empleado a eliminar: "))
    Empleado.eliminar(db, empleado_id)
    print("Empleado eliminado exitosamente.")

def main():
    db = DatabaseConnection()
    while True:
        menu()
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            agregar_empleado(db)
        elif opcion == "2":
            leer_empleado(db)
        elif opcion == "3":
            actualizar_empleado(db)
        elif opcion == "4":
            eliminar_empleado(db)
        elif opcion == "5":
            db.close()
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
if __name__ == "__main__":
    main()
