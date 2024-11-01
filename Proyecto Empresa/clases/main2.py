from conn import DatabaseConnection
from empleado import Empleado
from tipo_empleado import TipoEmpleado
from rol import Rol
from departamento import Departamento
from proyecto import Proyecto
from registro_tiempo import RegistroTiempo

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
    Empleado.eliminar(db, empleado_id)
    print("Empleado eliminado exitosamente.")
    pass

# Funciones CRUD para la tabla Tipo_Empleado
def crear_tipo_empleado():
    tipo = input("Nombre:")

    tipo = TipoEmpleado(nombre)
    tipo.insertar(db)
    print("Tipo de empleado creado con éxito.")
    pass

def leer_tipo_empleado():
    tipo_id = int(input("ID del tipo a consultar:"))
    tipo = TipoEmpleado.leer(db, tipo_id)
    if tipo:
        print("Datos del rol:", tipo)
        pass
    else:
        print("Rol no encontrado volviendo al menú anterior...")
        pass      

def actualizar_tipo_empleado():
    tipo_id = int(input("ID del tipo a actulizar: "))
    tipo = TipoEmpleado.leer(db, tipo_id)
    if tipo:
        tipo = input("Nombre")
        tipo = TipoEmpleado(nombre)
        tipo.actualizar(db)
        print("Tipo de empleado actualizado con éxito.")
        pass
    else:
        print("Tipo no encontrado volviendo al menú anterior...")
        pass

def eliminar_tipo_empleado():
    tipo_id = int(input("ID del tipo a eliminar: "))
    TipoEmpleado.eliminar(db, tipo_id)
    print("Tipo de empleado eliminado con éxito.")
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
    Rol.eliminar(db, rol_id)
    print("Rol eliminado con éxito.")
    pass

# Funciones CRUD para la tabla Departamento
def crear_departamento():
    nombre = input("Nombre del departamento: ")
    sql = "INSERT INTO Departamento (nombre) VALUES (%s)"
    cursor.execute(sql, (nombre,))
    conexion.commit()
    print("Departamento creado con éxito.")
    db.close()

def leer_departamentos():
    cursor.execute("SELECT * FROM Departamento")
    departamentos = cursor.fetchall()
    for dept in departamentos:
        print(dept)
        db.close()

def actualizar_departamento():
    dept_id = int(input("ID del departamento a actualizar: "))
    nuevo_nombre = input("Nuevo nombre del departamento: ")
    sql = "UPDATE Departamento SET nombre = %s WHERE id = %s"
    valores = (nuevo_nombre, dept_id)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Departamento actualizado con éxito.")
    db.close()

def eliminar_departamento():
    dept_id = int(input("ID del departamento a eliminar: "))
    sql = "DELETE FROM Departamento WHERE id = %s"
    cursor.execute(sql, (dept_id,))
    conexion.commit()
    print("Departamento eliminado con éxito.")
    db.close()

# Funciones CRUD para la tabla Proyecto
def crear_proyecto():
    nombre = input("Nombre del proyecto: ")
    descripcion = input("Descripción del proyecto: ")
    fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
    fecha_plazo = input("Fecha de plazo (YYYY-MM-DD): ")
    sql = "INSERT INTO Proyecto (nombre, descripcion, fecha_inicio, fecha_plazo) VALUES (%s, %s, %s, %s)"
    valores = (nombre, descripcion, fecha_inicio, fecha_plazo)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Proyecto creado con éxito.")
    db.close()

def leer_proyectos():
    cursor.execute("SELECT * FROM Proyecto")
    proyectos = cursor.fetchall()
    for proyecto in proyectos:
        print(proyecto)
        db.close()

def actualizar_proyecto():
    proyecto_id = int(input("ID del proyecto a actualizar: "))
    nuevo_nombre = input("Nuevo nombre del proyecto: ")
    nueva_descripcion = input("Nueva descripción del proyecto: ")
    sql = "UPDATE Proyecto SET nombre = %s, descripcion = %s WHERE id = %s"
    valores = (nuevo_nombre, nueva_descripcion, proyecto_id)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Proyecto actualizado con éxito.")
    db.close()

def eliminar_proyecto():
    proyecto_id = int(input("ID del proyecto a eliminar: "))
    sql = "DELETE FROM Proyecto WHERE id = %s"
    cursor.execute(sql, (proyecto_id,))
    conexion.commit()
    print("Proyecto eliminado con éxito.")
    db.close()

# Funciones CRUD para la tabla Registro_Tiempo
def crear_registro_tiempo():
    id_empleado = int(input("ID del empleado: "))
    fecha = input("Fecha (YYYY-MM-DD): ")
    cantidad_horas = int(input("Cantidad de horas: "))
    descripcion = input("Descripción: ")
    dia_extraordinario = input("¿Es día extraordinario? (S/N): ").upper() == 'S'
    comentario = input("Comentario: ")
    sql = "INSERT INTO Registro_Tiempo (id_empleado, fecha, cantidad_horas, descripcion, dia_extraordinario, comentario) VALUES (%s, %s, %s, %s, %s, %s)"
    valores = (id_empleado, fecha, cantidad_horas, descripcion, dia_extraordinario, comentario)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Registro de tiempo creado con éxito.")
    db.close()

def leer_registros_tiempo():
    cursor.execute("SELECT * FROM Registro_Tiempo")
    registros = cursor.fetchall()
    for registro in registros:
        print(registro)
        db.close()

def actualizar_registro_tiempo():
    registro_id = int(input("ID del registro de tiempo a actualizar: "))
    nueva_cantidad_horas = int(input("Nueva cantidad de horas: "))
    nueva_descripcion = input("Nueva descripción: ")
    sql = "UPDATE Registro_Tiempo SET cantidad_horas = %s, descripcion = %s WHERE id = %s"
    valores = (nueva_cantidad_horas, nueva_descripcion, registro_id)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Registro de tiempo actualizado con éxito.")
    db.close()

def eliminar_registro_tiempo():
    registro_id = int(input("ID del registro de tiempo a eliminar: "))
    sql = "DELETE FROM Registro_Tiempo WHERE id = %s"
    cursor.execute(sql, (registro_id,))
    conexion.commit()
    print("Registro de tiempo eliminado con éxito.")
    db.close()

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

def submenu_registro_tiempo():
    while True:
        print("\n--- Menú Registro de Tiempo ---")
        print("1. Crear Registro de Tiempo")
        print("2. Leer Registros de Tiempo")
        print("3. Actualizar Registro de Tiempo")
        print("4. Eliminar Registro de Tiempo")
        print("5. Volver al menú principal")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            crear_registro_tiempo()
        elif opcion == "2":
            leer_registros_tiempo()
        elif opcion == "3":
            actualizar_registro_tiempo()
        elif opcion == "4":
            eliminar_registro_tiempo()
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
        print("6. Tabla Registro de Tiempo")
        print("7. Salir")
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
            submenu_registro_tiempo()
        elif opcion == "7":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida.")

# Ejecutar el menú principal
menu_principal()

# Cerrar la conexión
db.close()
