from conn import DatabaseConnection
from empleado import Empleado
from asignacion import Asignacion
from departamento import Departamento
from proyecto import Proyecto

# Funciones CRUD para cada tabla
db = DatabaseConnection

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
    id_tipo = int(input("ID Tipo: "))
    
    empleado = Empleado(nombre, fecha_contrato, salario, correo, telefono, direccion, id_tipo_empleado, rut, fecha_nac, password, id_rol, id_tipo)
    empleado.insertar(db)
    print("Empleado agregado exitosamente.")

def leer_empleados():
    empleado_id = int(input("ID del empleado a consultar: "))
    empleado = Empleado.leer(db, empleado_id)
    if empleado:
        print("Datos del empleado:", empleado)
    else:
        print("Empleado no encontrado.")

def actualizar_empleado():
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

def eliminar_empleado():
    empleado_id = int(input("ID del empleado a eliminar: "))
    Empleado.eliminar(db, empleado_id)
    print("Empleado eliminado exitosamente.")

# Funciones CRUD para la tabla Tipo_empleado
def crear_tipo_empleado(db):
    tipo = input("Tipo de empleado: ")
    sql = "INSERT INTO Tipo_empleado (tipo) VALUES (%s)"
    cursor.execute(sql, (tipo,))
    conexion.commit()
    print("Tipo de empleado creado con éxito.")

def leer_tipo_empleado(db):
    cursor.execute("SELECT * FROM Tipo_empleado")
    tipos = cursor.fetchall()
    for tipo in tipos:
        print(tipo)

def actualizar_tipo_empleado(db):
    tipo_id = int(input("ID del tipo de empleado a actualizar: "))
    nuevo_tipo = input("Nuevo tipo de empleado: ")
    sql = "UPDATE Tipo_empleado SET tipo = %s WHERE id = %s"
    valores = (nuevo_tipo, tipo_id)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Tipo de empleado actualizado con éxito.")

def eliminar_tipo_empleado(db):
    tipo_id = int(input("ID del tipo de empleado a eliminar: "))
    sql = "DELETE FROM Tipo_empleado WHERE id = %s"
    cursor.execute(sql, (tipo_id,))
    conexion.commit()
    print("Tipo de empleado eliminado con éxito.")

# Funciones para Roles (similares para las demás tablas como Departamento, Proyecto, etc.)
def crear_rol(db):
    rol = input("Rol: ")
    permisos = input("Permisos: ")
    sql = "INSERT INTO Roles (rol, permisos) VALUES (%s, %s)"
    cursor.execute(sql, (rol, permisos))
    conexion.commit()
    print("Rol creado con éxito.")

def leer_roles(db):
    cursor.execute("SELECT * FROM Roles")
    roles = cursor.fetchall()
    for rol in roles:
        print(rol)

def actualizar_rol(db):
    rol_id = int(input("ID del rol a actualizar: "))
    nuevo_rol = input("Nuevo rol: ")
    permisos = input("Nuevos permisos: ")
    sql = "UPDATE Roles SET rol = %s, permisos = %s WHERE id = %s"
    valores = (nuevo_rol, permisos, rol_id)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Rol actualizado con éxito.")

def eliminar_rol(db):
    rol_id = int(input("ID del rol a eliminar: "))
    sql = "DELETE FROM Roles WHERE id = %s"
    cursor.execute(sql, (rol_id,))
    conexion.commit()
    print("Rol eliminado con éxito.")

# Funciones CRUD para la tabla Departamento
def crear_departamento(db):
    nombre = input("Nombre del departamento: ")
    sql = "INSERT INTO Departamento (nombre) VALUES (%s)"
    cursor.execute(sql, (nombre,))
    conexion.commit()
    print("Departamento creado con éxito.")

def leer_departamentos(db):
    cursor.execute("SELECT * FROM Departamento")
    departamentos = cursor.fetchall()
    for dept in departamentos:
        print(dept)

def actualizar_departamento(db):
    dept_id = int(input("ID del departamento a actualizar: "))
    nuevo_nombre = input("Nuevo nombre del departamento: ")
    sql = "UPDATE Departamento SET nombre = %s WHERE id = %s"
    valores = (nuevo_nombre, dept_id)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Departamento actualizado con éxito.")

def eliminar_departamento(db):
    dept_id = int(input("ID del departamento a eliminar: "))
    sql = "DELETE FROM Departamento WHERE id = %s"
    cursor.execute(sql, (dept_id,))
    conexion.commit()
    print("Departamento eliminado con éxito.")

# Funciones CRUD para la tabla Proyecto
def crear_proyecto(db):
    nombre = input("Nombre del proyecto: ")
    descripcion = input("Descripción del proyecto: ")
    fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
    fecha_plazo = input("Fecha de plazo (YYYY-MM-DD): ")
    sql = "INSERT INTO Proyecto (nombre, descripcion, fecha_inicio, fecha_plazo) VALUES (%s, %s, %s, %s)"
    valores = (nombre, descripcion, fecha_inicio, fecha_plazo)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Proyecto creado con éxito.")

def leer_proyectos(db):
    cursor.execute("SELECT * FROM Proyecto")
    proyectos = cursor.fetchall()
    for proyecto in proyectos:
        print(proyecto)

def actualizar_proyecto(db):
    proyecto_id = int(input("ID del proyecto a actualizar: "))
    nuevo_nombre = input("Nuevo nombre del proyecto: ")
    nueva_descripcion = input("Nueva descripción del proyecto: ")
    sql = "UPDATE Proyecto SET nombre = %s, descripcion = %s WHERE id = %s"
    valores = (nuevo_nombre, nueva_descripcion, proyecto_id)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Proyecto actualizado con éxito.")

def eliminar_proyecto(db):
    proyecto_id = int(input("ID del proyecto a eliminar: "))
    sql = "DELETE FROM Proyecto WHERE id = %s"
    cursor.execute(sql, (proyecto_id,))
    conexion.commit()
    print("Proyecto eliminado con éxito.")

# Funciones CRUD para la tabla Registro_Tiempo
def crear_registro_tiempo(db):
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

def leer_registros_tiempo(db):
    cursor.execute("SELECT * FROM Registro_Tiempo")
    registros = cursor.fetchall()
    for registro in registros:
        print(registro)

def actualizar_registro_tiempo(db):
    registro_id = int(input("ID del registro de tiempo a actualizar: "))
    nueva_cantidad_horas = int(input("Nueva cantidad de horas: "))
    nueva_descripcion = input("Nueva descripción: ")
    sql = "UPDATE Registro_Tiempo SET cantidad_horas = %s, descripcion = %s WHERE id = %s"
    valores = (nueva_cantidad_horas, nueva_descripcion, registro_id)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Registro de tiempo actualizado con éxito.")

def eliminar_registro_tiempo(db):
    registro_id = int(input("ID del registro de tiempo a eliminar: "))
    sql = "DELETE FROM Registro_Tiempo WHERE id = %s"
    cursor.execute(sql, (registro_id,))
    conexion.commit()
    print("Registro de tiempo eliminado con éxito.")

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
cursor.close()
conexion.close()
