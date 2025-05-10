#Proyecto_23270057
#\. C:\Users\lisas\OneDrive\Escritorio\S5A\Administracion de Base de Datos\Proyecto_ABD\Proyecto_23270057.sql
DROP DATABASE IF EXISTS Proyecto_23270057;
CREATE DATABASE Proyecto_23270057;
USE Proyecto_23270057;

CREATE TABLE Clientes (id_cliente INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(100), contrasena VARCHAR(100), correo VARCHAR(100), telefono VARCHAR(15),direccion TEXT,
tipo_cliente ENUM("Fisico", "linea") NOT NULL DEFAULT "linea",fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

CREATE TABLE Productos (id_producto VARCHAR(20) PRIMARY KEY, titulo VARCHAR(255), artista VARCHAR(255), genero VARCHAR(50), precio DECIMAL(10,2),
cantidad INT, fecha_de_lanzamiento INT);

CREATE TABLE Metodos_Pago (id_pago INT AUTO_INCREMENT PRIMARY KEY,
metodo_de_pago ENUM("Efectivo", "Tarjeta de Crédito", "Tarjeta de Débito", "Transferencia Bancaria"));

CREATE TABLE Ordenes (id_orden INT AUTO_INCREMENT PRIMARY KEY, id_cliente INT, fecha_compra TIMESTAMP DEFAULT CURRENT_TIMESTAMP, total DECIMAL(10,2) NOT NULL, 
tipo_compra ENUM("Físico", "linea") NOT NULL, id_pago INT, estado ENUM("Pendiente", "Pagado", "Enviado", "Entregado", "Cancelado") DEFAULT 'Pendiente',
FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
FOREIGN KEY (id_pago) REFERENCES Metodos_Pago(id_pago));

CREATE TABLE Detalles_Orden (id_detalle INT AUTO_INCREMENT PRIMARY KEY, id_orden INT, id_producto VARCHAR(20), cantidad INT, 
precio_unitario DECIMAL(10,2), subtotal DECIMAL(10,2) GENERATED ALWAYS AS (cantidad * precio_unitario) STORED,
FOREIGN KEY (id_orden) REFERENCES Ordenes(id_orden),
FOREIGN KEY (id_producto) REFERENCES Productos(id_producto));

CREATE TABLE Envios (id_envio INT AUTO_INCREMENT PRIMARY KEY, id_orden INT UNIQUE, direccion_envio TEXT NOT NULL, empresa_de_envio VARCHAR(100),
estado_envio ENUM("Preparando", "En tránsito", "Entregado", "Devuelto") DEFAULT "Preparando", fecha_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (id_orden) REFERENCES Ordenes(id_orden));

CREATE TABLE Catalogo_Productos (id_catalogo INT AUTO_INCREMENT PRIMARY KEY, id_producto VARCHAR(20), disponible ENUM("Sí", "No") DEFAULT "Sí", imagen_url VARCHAR(500),
fecha_actualizacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, 
FOREIGN KEY (id_producto) REFERENCES Productos(id_producto));

CREATE TABLE Carrito (id_carrito INT AUTO_INCREMENT PRIMARY KEY, id_cliente INT, id_producto VARCHAR(20), cantidad INT DEFAULT 1,
fecha_agregado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
FOREIGN KEY (id_producto) REFERENCES Productos(id_producto));

CREATE TABLE Empleados (id_empleado INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(100), correo VARCHAR(100),contrasena VARCHAR(100) NOT NULL, 
telefono VARCHAR(15), direccion TEXT, rol ENUM("Vendedor", "Almacenista", "Administrador", "Repartidor") NOT NULL, 
fecha_contratacion DATE DEFAULT (CURRENT_DATE));

INSERT INTO Empleados (nombre, correo, contrasena, telefono, direccion, rol)
VALUES ("Jose Lisandro Lopez L.", "lisandro@hotmail.com", "solriax234", "9616077499", "Col. Herradura, calle la niebla", "Administrador")
       ("Mario Alberto Anzures p.", "mario@hotmail.com", "mari234", "9611781692", "col. limon, calle la rosa", "Vendedor")
       ("Jose Angel Juarez T.", "jose@hotmail.com", "josa234", "9616085348", "col. las aguilas, libramiento sur", "Almacenista")
       ("Rodrigo Antonio Estrada O.", "rodrigo@hotmail.com", "rodri234", "9622798895", "col. el mirador, callejon alebriges", "Repartidor");
