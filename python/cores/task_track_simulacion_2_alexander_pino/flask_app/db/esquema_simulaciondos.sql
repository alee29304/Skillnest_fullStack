CREATE DATABASE esquema_simulaciondos;
USE esquema_simulaciondos;

CREATE TABLE usuarios(
id INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(45),
apellido VARCHAR(45),
email VARCHAR(100),
password VARCHAR(255),
created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE categorias (
id INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(45),
usuario_id INT,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
CONSTRAINT fk_categoria_usuario
FOREIGN KEY (usuario_id)
REFERENCES usuarios(id)
);

CREATE TABLE tareas (
id INT AUTO_INCREMENT PRIMARY KEY,
titulo VARCHAR(100),
categoria_id INT,
usuario_id INT,
prioridad VARCHAR(20),
estado VARCHAR(20),
fecha_limite DATE,
descripcion TEXT,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
CONSTRAINT fk_tarea_categoria
FOREIGN KEY (categoria_id)
REFERENCES categorias(id),
CONSTRAINT fk_tarea_usuario
FOREIGN KEY (usuario_id)
REFERENCES usuarios(id)
);