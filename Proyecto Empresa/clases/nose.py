#ejemplo para añadir

nuevo_empleado = Empleado(
    id=None,  # El ID se puede dejar como None si es autoincremental en la base de datos
    nombre="Juan Morales",
    fecha_contrato="2023-10-01",
    salario=50000,
    correo="juan.perez@example.com",
    telefono="123456789",
    direccion="Calle Falsa 123",
    id_tipo_empleado=1,
    rut="12345678-9",
    fecha_nac="1990-05-20",
    password="password123",
    id_rol=1,
    id_tipo=1
)

#Insertar el nuevo empleado en la base de datos
nuevo_empleado.insertar(db)

#Cerrar la conexión
db.close()

print("Empleado creado exitosamente.")

# Ejemplo de uso del método eliminar
empleado_id_a_eliminar = 2  # Cambia este valor por el ID del empleado que quieres eliminar

Empleado.eliminar(db, empleado_id_a_eliminar)
print(f"Empleado con ID {empleado_id_a_eliminar} eliminado.")    