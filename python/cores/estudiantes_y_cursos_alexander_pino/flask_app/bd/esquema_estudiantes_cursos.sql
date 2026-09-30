CREATE DATABASE IF NOT EXISTS esquema_estudiantes_cursos;
USE esquema_estudiantes_cursos;

CREATE TABLE IF NOT EXISTS cursos (
id INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(45) NOT NULL,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS estudiantes (
id INT AUTO_INCREMENT PRIMARY KEY,
nombre VARCHAR(45) NOT NULL,
apellido VARCHAR(45) NOT NULL,
edad INT NOT NULL,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
curso_id INT NOT NULL,
CONSTRAINT fk_estudiantes_curso
FOREIGN KEY (curso_id)
REFERENCES cursos(id)
);

INSERT INTO cursos
(nombre)
VALUES
("MERN"),
("Java"),
("Python"),
("Fundamentos de la Web");

INSERT INTO estudiantes
(nombre, apellido, edad, curso_id)
VALUES
("Valeria", "Romero", 25, 1),
("Cynthia", "Castillo", 26, 1),
("Patricio", "Fuentelba", 27, 1),
("Kevin", "Duque", 27, 1),
("Andrea", "Pérez", 22, 2),
("Matías", "Soto", 24, 3);
