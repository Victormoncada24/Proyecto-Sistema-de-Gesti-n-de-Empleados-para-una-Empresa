-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 01-11-2024 a las 07:59:02
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `empresa`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamento`
--

CREATE TABLE `departamento` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `id_empleado` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `departamento`
--

INSERT INTO `departamento` (`id`, `nombre`, `id_empleado`) VALUES
(1, 'Recursos Humanos', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleado`
--

CREATE TABLE `empleado` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `fecha_contrato` date DEFAULT NULL,
  `salario` decimal(10,2) DEFAULT NULL,
  `correo` varchar(255) DEFAULT NULL,
  `telefono` varchar(50) DEFAULT NULL,
  `direccion` varchar(255) DEFAULT NULL,
  `id_tipo_empleado` int(11) DEFAULT NULL,
  `id_rol` int(11) DEFAULT NULL,
  `fecha_nac` date DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `rut` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `empleado`
--

INSERT INTO `empleado` (`id`, `nombre`, `fecha_contrato`, `salario`, `correo`, `telefono`, `direccion`, `id_tipo_empleado`, `id_rol`, `fecha_nac`, `password`, `rut`) VALUES
(1, 'Victor Moncada', '2024-10-31', 900000.00, 'victor@gmail.com', '943432233', 'Los Pinos Km8', 1, 1, '1999-12-12', '123456789', '20353664-K'),
(2, 'Manuel Pérez', '2024-10-31', 900000.00, 'Manuel@gmail.com', '962424313', 'Santa Calorina Km10', 2, 2, '1999-12-24', '0987654321', '20664353-K'),
(4, 'Pepe Martinez', '2024-11-01', 900000.00, 'pepe@gmail.com', '755243232', 'Manuel Montt 4313', 2, 2, '1999-01-01', '352231556', '21535446-K');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `informe`
--

CREATE TABLE `informe` (
  `id` int(11) NOT NULL,
  `id_empleado` int(11) DEFAULT NULL,
  `fecha_hora` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `modulos`
--

CREATE TABLE `modulos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proyecto`
--

CREATE TABLE `proyecto` (
  `id` int(11) NOT NULL,
  `nombre` varchar(255) NOT NULL,
  `descripcion` text DEFAULT NULL,
  `fecha_inicio` date DEFAULT NULL,
  `fecha_plazo` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `proyecto`
--

INSERT INTO `proyecto` (`id`, `nombre`, `descripcion`, `fecha_inicio`, `fecha_plazo`) VALUES
(1, 'Proyecto de Menú interactivo', 'Es un pequeño proyecto que nos ayudara a crear el menú de esta base de datos', '2024-10-30', '2024-11-01'),
(2, 'Proyecto Ficticio', 'Es un proyecto de relleno', '2024-10-23', '2024-11-01');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proyecto_empleado`
--

CREATE TABLE `proyecto_empleado` (
  `id` int(11) NOT NULL,
  `id_empleado` int(11) DEFAULT NULL,
  `id_proyecto` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registro_tiempo`
--

CREATE TABLE `registro_tiempo` (
  `id` int(11) NOT NULL,
  `id_empleado` int(11) DEFAULT NULL,
  `fecha` date NOT NULL,
  `cantidad_horas` int(11) NOT NULL,
  `descripcion` text DEFAULT NULL,
  `dia_extraordinario` tinyint(1) DEFAULT NULL,
  `comentario` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `id` int(11) NOT NULL,
  `rol` varchar(255) NOT NULL,
  `permisos` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `roles`
--

INSERT INTO `roles` (`id`, `rol`, `permisos`) VALUES
(1, 'GERENTE', 'GER-EMP'),
(2, 'EMPLEADO', 'EMP');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_empleado`
--

CREATE TABLE `tipo_empleado` (
  `id` int(11) NOT NULL,
  `tipo` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tipo_empleado`
--

INSERT INTO `tipo_empleado` (`id`, `tipo`) VALUES
(1, 'Gerente'),
(2, 'Empleado');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_empleado_emp`
--

CREATE TABLE `tipo_empleado_emp` (
  `id` int(11) NOT NULL,
  `id_empleado` int(11) DEFAULT NULL,
  `id_tipo_empleado` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `departamento`
--
ALTER TABLE `departamento`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_empleado` (`id_empleado`);

--
-- Indices de la tabla `empleado`
--
ALTER TABLE `empleado`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_tipo_empleado` (`id_tipo_empleado`),
  ADD KEY `id_rol` (`id_rol`);

--
-- Indices de la tabla `informe`
--
ALTER TABLE `informe`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_empleado` (`id_empleado`);

--
-- Indices de la tabla `modulos`
--
ALTER TABLE `modulos`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `proyecto`
--
ALTER TABLE `proyecto`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `proyecto_empleado`
--
ALTER TABLE `proyecto_empleado`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_empleado` (`id_empleado`),
  ADD KEY `id_proyecto` (`id_proyecto`);

--
-- Indices de la tabla `registro_tiempo`
--
ALTER TABLE `registro_tiempo`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_empleado` (`id_empleado`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tipo_empleado`
--
ALTER TABLE `tipo_empleado`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tipo_empleado_emp`
--
ALTER TABLE `tipo_empleado_emp`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_empleado` (`id_empleado`),
  ADD KEY `id_tipo_empleado` (`id_tipo_empleado`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `departamento`
--
ALTER TABLE `departamento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `empleado`
--
ALTER TABLE `empleado`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `informe`
--
ALTER TABLE `informe`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `modulos`
--
ALTER TABLE `modulos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `proyecto`
--
ALTER TABLE `proyecto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `proyecto_empleado`
--
ALTER TABLE `proyecto_empleado`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `registro_tiempo`
--
ALTER TABLE `registro_tiempo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `tipo_empleado`
--
ALTER TABLE `tipo_empleado`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `tipo_empleado_emp`
--
ALTER TABLE `tipo_empleado_emp`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `departamento`
--
ALTER TABLE `departamento`
  ADD CONSTRAINT `departamento_ibfk_1` FOREIGN KEY (`id_empleado`) REFERENCES `empleado` (`id`);

--
-- Filtros para la tabla `empleado`
--
ALTER TABLE `empleado`
  ADD CONSTRAINT `empleado_ibfk_1` FOREIGN KEY (`id_tipo_empleado`) REFERENCES `tipo_empleado` (`id`),
  ADD CONSTRAINT `empleado_ibfk_2` FOREIGN KEY (`id_rol`) REFERENCES `roles` (`id`);

--
-- Filtros para la tabla `informe`
--
ALTER TABLE `informe`
  ADD CONSTRAINT `informe_ibfk_1` FOREIGN KEY (`id_empleado`) REFERENCES `empleado` (`id`);

--
-- Filtros para la tabla `proyecto_empleado`
--
ALTER TABLE `proyecto_empleado`
  ADD CONSTRAINT `proyecto_empleado_ibfk_1` FOREIGN KEY (`id_empleado`) REFERENCES `empleado` (`id`),
  ADD CONSTRAINT `proyecto_empleado_ibfk_2` FOREIGN KEY (`id_proyecto`) REFERENCES `proyecto` (`id`);

--
-- Filtros para la tabla `registro_tiempo`
--
ALTER TABLE `registro_tiempo`
  ADD CONSTRAINT `registro_tiempo_ibfk_1` FOREIGN KEY (`id_empleado`) REFERENCES `empleado` (`id`);

--
-- Filtros para la tabla `tipo_empleado_emp`
--
ALTER TABLE `tipo_empleado_emp`
  ADD CONSTRAINT `tipo_empleado_emp_ibfk_1` FOREIGN KEY (`id_empleado`) REFERENCES `empleado` (`id`),
  ADD CONSTRAINT `tipo_empleado_emp_ibfk_2` FOREIGN KEY (`id_tipo_empleado`) REFERENCES `tipo_empleado` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
