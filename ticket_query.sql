-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS ticket;
USE ticket;

-- Crear la tabla 'Nivel'
CREATE TABLE Nivel (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nivel VARCHAR(2) NOT NULL
);

-- Crear la tabla 'Municipio'
CREATE TABLE Municipio (
    id INT AUTO_INCREMENT PRIMARY KEY,
    municipio VARCHAR(30) NOT NULL
);

-- Crear la tabla 'Asunto'
CREATE TABLE Asunto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    asunto VARCHAR(50) NOT NULL
);

-- Crear la tabla 'Usuarios'
CREATE TABLE Usuarios (
    no_usuario INT AUTO_INCREMENT PRIMARY KEY,
    usuario VARCHAR(30) NOT NULL,
    contrasena VARCHAR(20) NOT NULL
);

-- Crear la tabla 'Formulario'
CREATE TABLE Formulario (
    no_turno INT AUTO_INCREMENT PRIMARY KEY,
    curp VARCHAR(18) NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    paterno VARCHAR(255) NOT NULL,
    materno VARCHAR(255) NOT NULL,
    telefono VARCHAR(10),
    celular VARCHAR(10),
    correo VARCHAR(100),
    id_nivel INT,
    id_mun INT,
    id_asunto INT,
    estado VARCHAR(255),
    FOREIGN KEY (id_nivel) REFERENCES Nivel(id),
    FOREIGN KEY (id_mun) REFERENCES Municipio(id),
    FOREIGN KEY (id_asunto) REFERENCES Asunto(id)
);

-- Insertar datos en la tabla 'Nivel'
INSERT INTO Nivel (nivel) VALUES 
('1'),
('2'),
('3'),
('4'),
('5'),
('6'),
('7'),
('8'),
('9'),
('10');

-- Insertar datos en la tabla 'Municipio'
INSERT INTO Municipio (municipio) VALUES 
('Saltillo'),
('Arteaga'),
('Ramos Arizpe'),
('Monclova'),
('Torreón'),
('Acuña'),
('Ocampo'),
('Piedras Negras');

-- Insertar datos en la tabla 'Asunto'
INSERT INTO Asunto (asunto) VALUES 
('Ingreso'),
('Egreso'),
('Pago de Inscripción'),
('Selección de Horario'),
('Recoger papelería');

-- Insertar datos de ejemplo en la tabla 'Usuarios'
INSERT INTO Usuarios (usuario, contrasena) VALUES 
('azul', 'azul'),
('admin', 'admin'),
('otroadmin', 'otroadmin');
