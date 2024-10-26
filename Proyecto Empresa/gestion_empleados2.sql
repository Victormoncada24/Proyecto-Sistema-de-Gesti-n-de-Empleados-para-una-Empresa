-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 26-10-2024 a las 01:22:29
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
-- Base de datos: `gestion_empleados2`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamento`
--

CREATE TABLE `departamento` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `id_empleado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `empleado`
--

CREATE TABLE `empleado` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `fecha_contrato` date NOT NULL,
  `salario` int(11) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `telefono` int(11) NOT NULL,
  `direccion` varchar(50) NOT NULL,
  `id_tipo_empleado` int(11) NOT NULL,
  `rut` varchar(9) NOT NULL,
  `fecha_nac` date NOT NULL,
  `password` varchar(50) NOT NULL,
  `id_rol` int(11) NOT NULL,
  `id_tipo` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `informe`
--

CREATE TABLE `informe` (
  `id` int(11) NOT NULL,
  `id_empleado` int(11) NOT NULL,
  `fecha_hora` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `modulo`
--

CREATE TABLE `modulo` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proyecto`
--

CREATE TABLE `proyecto` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `descripcion` varchar(200) NOT NULL,
  `fecha_inicio` date NOT NULL,
  `fecha_plazo` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registrotiempo`
--

CREATE TABLE `registrotiempo` (
  `id` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `cantidad_horas` int(11) NOT NULL,
  `descripcion` varchar(200) NOT NULL,
  `dia_extraordinario` varchar(8) NOT NULL,
  `comentario` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rol`
--

CREATE TABLE `rol` (
  `id` int(11) NOT NULL,
  `rol` varchar(50) NOT NULL,
  `permisos` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipoempleado`
--

CREATE TABLE `tipoempleado` (
  `id` int(11) NOT NULL,
  `tipo` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `departamento`
--
ALTER TABLE `departamento`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `empleado`
--
ALTER TABLE `empleado`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `informe`
--
ALTER TABLE `informe`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `modulo`
--
ALTER TABLE `modulo`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `proyecto`
--
ALTER TABLE `proyecto`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `registrotiempo`
--
ALTER TABLE `registrotiempo`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `rol`
--
ALTER TABLE `rol`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tipoempleado`
--
ALTER TABLE `tipoempleado`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `departamento`
--
ALTER TABLE `departamento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `empleado`
--
ALTER TABLE `empleado`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `informe`
--
ALTER TABLE `informe`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `modulo`
--
ALTER TABLE `modulo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `proyecto`
--
ALTER TABLE `proyecto`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `registrotiempo`
--
ALTER TABLE `registrotiempo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `rol`
--
ALTER TABLE `rol`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tipoempleado`
--
ALTER TABLE `tipoempleado`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
