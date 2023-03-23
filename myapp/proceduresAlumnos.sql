#----------------------------------- AGREGAR A UN alumno ------------------------------------

DELIMITER //

CREATE PROCEDURE Agregar_alumno
(
   IN nombre VARCHAR(50),
   IN apellidos VARCHAR(50),
   IN email VARCHAR(50)
)
BEGIN
   INSERT INTO alumnos (nombre, apellidos, email)
   VALUES (nombre, apellidos, email);
END //

DELIMITER ;

DELIMITER //

#----------------------------------- CONSULTA DE UN alumnoS ------------------------------------

CREATE PROCEDURE Consulta_alumnos()
BEGIN
   SELECT nombre, apellidos, email
   FROM alumnos;
END //

DELIMITER ;

DELIMITER //

#----------------------------------- CONSULTA DE UN alumno ------------------------------------


CREATE PROCEDURE Consulta_alumno
(
   IN nombre_a_buscar VARCHAR(50),
   IN apellidos_a_buscar VARCHAR(50)
)
BEGIN
   SELECT nombre, apellidos, email
   FROM alumnos
   WHERE 
      (nombre LIKE CONCAT('%', nombre_a_buscar, '%') OR nombre_a_buscar IS NULL) AND 
      (apellidos LIKE CONCAT('%', apellidos_a_buscar, '%') OR apellidos_a_buscar IS NULL);
END //

DELIMITER ;

#----------------------------------- ELIMINAR ------------------------------------

DELIMITER //

CREATE PROCEDURE Eliminar_alumno
(
   IN id_alumno_a_eliminar INT
)
BEGIN
   DELETE FROM alumnos
   WHERE id = id_alumno_a_eliminar;
END //

DELIMITER ;

DELIMITER //

#----------------------------------- MODIFICAR ------------------------------------

CREATE PROCEDURE Modificar_alumno
(
   IN id_alumno_alumnosa_buscar INT,
   IN nuevo_nombre VARCHAR(50),
   IN nuevos_apellidos VARCHAR(50),
   IN nuevo_email VARCHAR(50)
)
BEGIN
   UPDATE alumnos
   SET nombre = nuevo_nombre, apellidos = nuevos_apellidos, email = nuevo_email
   WHERE id = id_alumno_a_buscar;
END //

DELIMITER ;

