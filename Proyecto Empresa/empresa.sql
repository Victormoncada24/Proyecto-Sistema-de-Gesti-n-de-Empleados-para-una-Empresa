-- Crear la base de datos si no existe y usarla
CREATE DATABASE IF NOT EXISTS empresa;
USE empresa;

-- Tabla Tipo_empleado
CREATE TABLE IF NOT EXISTS Tipo_empleado (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(255) NOT NULL
);

-- Tabla Roles
CREATE TABLE IF NOT EXISTS Roles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    rol VARCHAR(255) NOT NULL,
    permisos TEXT
);

-- Tabla Empleado
CREATE TABLE IF NOT EXISTS Empleado (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    fecha_contrato DATE,
    salario DECIMAL(10, 2),
    correo VARCHAR(255),
    telefono VARCHAR(50),
    direccion VARCHAR(255),
    id_tipo_empleado INT,
    id_rol INT,
    fecha_nac DATE,
    password VARCHAR(255),
    rut VARCHAR(20),
    FOREIGN KEY (id_tipo_empleado) REFERENCES Tipo_empleado(id),
    FOREIGN KEY (id_rol) REFERENCES Roles(id)
);

-- Tabla Departamento
CREATE TABLE IF NOT EXISTS Departamento (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    id_empleado INT,
    FOREIGN KEY (id_empleado) REFERENCES Empleado(id)
);

-- Tabla Proyecto
CREATE TABLE IF NOT EXISTS Proyecto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    fecha_inicio DATE,
    fecha_plazo DATE
);

-- Tabla Proyecto_Empleado (relación muchos a muchos entre Proyecto y Empleado)
CREATE TABLE IF NOT EXISTS Proyecto_Empleado (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_empleado INT,
    id_proyecto INT,
    FOREIGN KEY (id_empleado) REFERENCES Empleado(id),
    FOREIGN KEY (id_proyecto) REFERENCES Proyecto(id)
);

-- Tabla Registro_Tiempo
CREATE TABLE IF NOT EXISTS Registro_Tiempo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_empleado INT,
    fecha DATE NOT NULL,
    cantidad_horas INT NOT NULL,
    descripcion TEXT,
    dia_extraordinario BOOLEAN,
    comentario TEXT,
    FOREIGN KEY (id_empleado) REFERENCES Empleado(id)
);

-- Tabla Informe
CREATE TABLE IF NOT EXISTS Informe (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_empleado INT,
    fecha_hora TIMESTAMP,
    FOREIGN KEY (id_empleado) REFERENCES Empleado(id)
);

-- Tabla Modulos
CREATE TABLE IF NOT EXISTS Modulos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL
);

-- Tabla Tipo_empleado_emp (relación de tipos de empleados)
CREATE TABLE IF NOT EXISTS Tipo_empleado_emp (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_empleado INT,
    id_tipo_empleado INT,
    FOREIGN KEY (id_empleado) REFERENCES Empleado(id),
    FOREIGN KEY (id_tipo_empleado) REFERENCES Tipo_empleado(id)
);
