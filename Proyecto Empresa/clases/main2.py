from conn import DatabaseConnection
from empleado import Empleado
from tipo_empleado import TipoEmpleado
from rol import Rol
from departamento import Departamento
from proyecto import Proyecto

db = DatabaseConnection()

# Funciones CRUD para tabla Empleado
def crear_empleado():
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
    
    empleado = Empleado(nombre, fecha_contrato, salario, correo, telefono, direccion, id_tipo_empleado, rut, fecha_nac, password, id_rol)
    empleado.insertar(db)
    print("Empleado agregado exitosamente.")
    pass

def leer_empleados():
    empleado_id = int(input("ID del empleado a consultar: "))
    empleado = Empleado.leer(db, empleado_id)
    if empleado:
        print("Datos del empleado:", empleado)
        pass
    else:
        print("Empleado no encontrado volviendo al menú anterior...")
        pass

def actualizar_empleado():
    empleado_id = int(input("ID del empleado a actualizar: "))
    empleado = Empleado.leer(db, empleado_id)
    if empleado:
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
        
        empleado = Empleado(empleado_id, nombre, fecha_contrato, salario, correo, telefono, direccion, id_tipo_empleado, rut, fecha_nac, password, id_rol)
        empleado.actualizar(db)
        print("Empleado actualizado exitosamente.")
        pass
    else:
        print("Empleado no encontrado volviendo al menú anterior...")
        pass

def eliminar_empleado():
    empleado_id = int(input("ID del empleado a eliminar: "))
    empleado = Empleado.leer(db, empleado_id)
    if empleado:
        Empleado.eliminar(db, empleado_id)
        print("Empleado eliminado exitosamente.")
        pass
    else:
        print("Empleado no encontrado volviendo al menú anterior...")
        pass

# Funciones CRUD para la tabla Tipo_Empleado
def crear_tipo_empleado():
    tipo = input("Nombre:")

    tipo = TipoEmpleado(nombre)
    tipo.insertar(db)
    print("Tipo de empleado creado con éxito.")
    pass

def leer_tipo_empleado():
    tipo_id = int(input("ID del tipo de empleado a consultar:"))
    tipo = TipoEmpleado.leer(db, tipo_id)
    if tipo:
        print("Datos del tipo de empleado:", tipo)
        pass
    else:
        print("Tipo de empleado no encontrado volviendo al menú anterior...")
        pass      

def actualizar_tipo_empleado():
    tipo_id = int(input("ID del tipo de empleado a actulizar: "))
    tipo = TipoEmpleado.leer(db, tipo_id)
    if tipo:
        tipo = input("Nombre")
        tipo = TipoEmpleado(nombre)
        tipo.actualizar(db)
        print("Tipo de empleado actualizado con éxito.")
        pass
    else:
        print("Tipo de empleado no encontrado volviendo al menú anterior...")
        pass

def eliminar_tipo_empleado():
    tipo_id = int(input("ID del tipo a eliminar: "))
    tipo = TipoEmpleado.leer(db, tipo_id)
    if tipo:
        TipoEmpleado.eliminar(db, tipo_id)
        print("Tipo de empleado eliminado con éxito.")
        pass
    else:
        print("Tipo de empleado no encontrado volviendo al menú anterior...")
        pass    

# Funciones CRUD para la tabla Roles
def crear_rol():
    rol = input("Rol: ")
    permisos = input("Permisos (GER-EMP o EMP):")

    rol = Rol(rol,permisos)
    rol.insertar(db)
    print("Rol creado con éxito.")
    pass

def leer_roles():
    rol_id = int(input("ID del Rol a consulta: "))
    rol = Rol.leer(db, rol_id)
    if rol:
        print("Datos del rol: ", rol)
        pass
    else:
        print("Rol no encontrado volviendo al menú anterior...")
        pass

def actualizar_rol():
    rol_id = int(input("ID del rol: a actualizar: "))
    rol = Rol.leer(db, rol_id)
    if rol:
        rol = input("Rol:")
        permisos = input("Permisos (GER-EMP o EMP):")

        rol = Rol(db, rol_id, rol, permisos)
        rol.actualizar(db)
        print("Rol actualizado con éxito.")
        pass
    else:
        print("Rol no encontrado volviendo al menú anterior...")
        pass   

def eliminar_rol():
    rol_id = int(input("ID del rol a eliminar: "))
    rol = Rol.leer(db, rol_id)
    if rol:
        Rol.eliminar(db, rol_id)
        print("Rol eliminado con éxito.")
        pass
    else:
        print("Rol no encontrado volviendo al menú anterior...")
        pass

# Funciones CRUD para la tabla Departamento
def crear_departamento():
    nombre = input("Nombre del departamento: ")
    id_empleado = input("ID del Gerente a cargo: ")

    departamento = Departamento(nombre, id_empleado)
    departamento.insertar(db)
    print("Departamento creado con éxito.")
    pass

def leer_departamentos():
    departamento_id = int(input("ID del departamento a consulta: "))
    departamento = Departamento.leer(db, departamento_id)
    if departamento:
        print("Datos del Empleado: ", departamento)
        pass
    else:
        print("Departamento no encontrado volviendo al menú anterior...")
        pass

def actualizar_departamento():
    departamento_id = int(input("ID del departamento a actualizar: "))
    departamento = Departamento(db, nombre, id_empleado, departamento_id)
    if departamento:
        nombre = input("Nombre: ")
        id_empleado = int(input("ID gerente"))

        departamento = Departamento(nombre, id_empleado, departamento_id)
        departamento.actualizar(db)
        print("Departamento actualizado exitosamente.")
        pass
    else:
        print("Departamento no encontrado volviendo al menú anterior...")
        pass

def eliminar_departamento():
    departamento_id = int(input("ID del departamento a eliminar."))
    departamento = Departamento.leer(db, departamento_id)
    if departamento:
        Departamento.eliminar(db, departamento_id)
        print("Departamento eliminado exitosamente.")
        pass
    else:
        print("Departamento no encontrado volviendo al menú anterior...")
        pass

# Funciones CRUD para la tabla Proyecto
def crear_proyecto():
    nombre = input("Nombre: ")
    descripcion = ("Descripcion del proyecto: ")
    fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
    fecha_plazo = input("Fecha del plazo (YYYY-MM-DD): ")

    proyecto = Proyecto(nombre, descripcion, fecha_inicio, fecha_plazo)
    proyecto.insertar(db)
    print("Proyecto agregado exitosamente.")
    pass

def leer_proyectos():
    proyecto_id = int(input("ID del proyecto"))
    proyecto = Proyecto.leer(db, proyecto_id)
    if proyecto:
        print("Datos del proyecto:", proyecto)
        pass
    else:
        print("Proyecto no encontrado volviendo al menú anterior...")
        pass

def actualizar_proyecto():
    proyecto_id = int(input("ID del proyecto a actualizar: "))
    proyecto = Proyecto.leer(db, proyecto_id)
    if proyecto:
        nombre = input("Nombre: ")
        descripcion = input("Descripcion: ")
        fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
        fecha_plazo = input("Fecha del plazo (YYYY-MM-DD): ")

        proyecto = Proyecto(proyecto_id, nombre, descripcion, fecha_inicio, fecha_plazo)
        proyecto.actualizar(db)
        print("Proyecto actualizado exitosamente.")
        pass
    else:
        print("Proyecto no encontrado volviendo al menú anterior...")
        pass

def eliminar_proyecto():
    proyecto_id = int(input("ID del proyecto a eliminar:"))
    proyecto = Proyecto.leer(db, proyecto_id)
    if proyecto:
        Proyecto.eliminar(db, proyecto_id)
        print("Proyecto eliminado exitosamente.")
        pass
    else:
        print("Proyecto no encontrado volviendo al menú anterior...")
        pass

# Submenús para cada tabla
def submenu_empleado():
    while True:
        print("\n--- Menú Empleado ---")
        print("1. Crear Empleado")
        print("2. Leer Empleados")
        print("3. Actualizar Empleado")
        print("4. Eliminar Empleado")
        print("5. Volver al menú principal")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            crear_empleado()
        elif opcion == "2":
            leer_empleados()
        elif opcion == "3":
            actualizar_empleado()
        elif opcion == "4":
            eliminar_empleado()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

def submenu_tipo_empleado():
    while True:
        print("\n--- Menú Tipo Empleado ---")
        print("1. Crear Tipo Empleado")
        print("2. Leer Tipo Empleados")
        print("3. Actualizar Tipo Empleado")
        print("4. Eliminar Tipo Empleado")
        print("5. Volver al menú principal")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            crear_tipo_empleado()
        elif opcion == "2":
            leer_tipo_empleado()
        elif opcion == "3":
            actualizar_tipo_empleado()
        elif opcion == "4":
            eliminar_tipo_empleado()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

def submenu_roles():
    while True:
        print("\n--- Menú Roles ---")
        print("1. Crear Rol")
        print("2. Leer Roles")
        print("3. Actualizar Rol")
        print("4. Eliminar Rol")
        print("5. Volver al menú principal")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            crear_rol()
        elif opcion == "2":
            leer_roles()
        elif opcion == "3":
            actualizar_rol()
        elif opcion == "4":
            eliminar_rol()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

def submenu_departamento():
    while True:
        print("\n--- Menú Departamento ---")
        print("1. Crear Departamento")
        print("2. Leer Departamentos")
        print("3. Actualizar Departamento")
        print("4. Eliminar Departamento")
        print("5. Volver al menú principal")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            crear_departamento()
        elif opcion == "2":
            leer_departamentos()
        elif opcion == "3":
            actualizar_departamento()
        elif opcion == "4":
            eliminar_departamento()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

def submenu_proyecto():
    while True:
        print("\n--- Menú Proyecto ---")
        print("1. Crear Proyecto")
        print("2. Leer Proyectos")
        print("3. Actualizar Proyecto")
        print("4. Eliminar Proyecto")
        print("5. Volver al menú principal")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            crear_proyecto()
        elif opcion == "2":
            leer_proyectos()
        elif opcion == "3":
            actualizar_proyecto()
        elif opcion == "4":
            eliminar_proyecto()
        elif opcion == "5":
            break
        else:
            print("Opción inválida.")

# Menú principal
def menu_principal():
    db = DatabaseConnection
    while True:
        print("\n--- Menú Principal ---")
        print("1. Tabla Empleado")
        print("2. Tabla Tipo Empleado")
        print("3. Tabla Roles")
        print("4. Tabla Departamento")
        print("5. Tabla Proyecto")
        print("6. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            submenu_empleado()
        elif opcion == "2":
            submenu_tipo_empleado()
        elif opcion == "3":
            submenu_roles()
        elif opcion == "4":
            submenu_departamento()
        elif opcion == "5":
            submenu_proyecto()
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida.")

# Ejecutar el menú principal
menu_principal()

# Cerrar la conexión
db.close()
