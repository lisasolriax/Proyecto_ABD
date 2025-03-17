#Proyecto_23270057
#\. C:\Users\lisas\OneDrive\Escritorio\S5A\Administracion de Base de Datos\Proyecto_23270057.sql
DROP DATABASE IF EXISTS Proyecto_23270057;
CREATE DATABASE Proyecto_23270057;
USE Proyecto_23270057;

-- Tabla de Clientes
CREATE TABLE Clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) UNIQUE NOT NULL,
    telefono VARCHAR(15),
    direccion TEXT,
    tipo_cliente ENUM('Físico', 'Online') NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de Productos (Vinilos)
CREATE TABLE Productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    artista VARCHAR(255) NOT NULL,
    genero VARCHAR(50),
    precio DECIMAL(10,2) NOT NULL,
    stock INT NOT NULL DEFAULT 0,
    formato ENUM('LP', 'EP', 'Single'),
    ano_lanzamiento INT,  -- Cambio de "año_lanzamiento" a "ano_lanzamiento"
    imagen VARCHAR(255)
);

-- Tabla de Métodos de Pago
CREATE TABLE Metodos_Pago (
    id_pago INT AUTO_INCREMENT PRIMARY KEY,
    metodo ENUM('Efectivo', 'Tarjeta Crédito', 'Tarjeta Débito', 'PayPal', 'Transferencia Bancaria') NOT NULL
);

-- Tabla de Órdenes (Compras)
CREATE TABLE Ordenes (
    id_orden INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    fecha_compra TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL(10,2) NOT NULL,
    tipo_compra ENUM('Físico', 'Online') NOT NULL,
    id_pago INT NULL,  -- Cambiado de NOT NULL a NULL
    estado ENUM('Pendiente', 'Pagado', 'Enviado', 'Entregado', 'Cancelado') DEFAULT 'Pendiente',
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente) ON DELETE CASCADE,
    FOREIGN KEY (id_pago) REFERENCES Metodos_Pago(id_pago) ON DELETE SET NULL
);

-- Tabla de Detalles de la Orden (Productos comprados en cada orden)
CREATE TABLE Detalles_Orden (
    id_detalle INT AUTO_INCREMENT PRIMARY KEY,
    id_orden INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10,2) NOT NULL,
    subtotal DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (id_orden) REFERENCES Ordenes(id_orden) ON DELETE CASCADE,
    FOREIGN KEY (id_producto) REFERENCES Productos(id_producto) ON DELETE CASCADE
);

-- Tabla de Envíos (Solo para compras en línea)
CREATE TABLE Envios (
    id_envio INT AUTO_INCREMENT PRIMARY KEY,
    id_orden INT NOT NULL,
    direccion_envio TEXT NOT NULL,
    empresa_envio VARCHAR(100),
    numero_guia VARCHAR(50),
    estado_envio ENUM('Preparando', 'En tránsito', 'Entregado', 'Devuelto') DEFAULT 'Preparando',
    fecha_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_orden) REFERENCES Ordenes(id_orden) ON DELETE CASCADE
);