#----------------------------------- AGREGAR A UN MAESTRO ------------------------------------

DELIMITER //

CREATE PROCEDURE Agregar_maestro
(
   IN nombre VARCHAR(50),
   IN apellidos VARCHAR(50),
   IN email VARCHAR(50)
)
BEGIN
   INSERT INTO Maestros (nombre, apellidos, email)
   VALUES (nombre, apellidos, email);
END //

DELIMITER ;

DELIMITER //

#----------------------------------- CONSULTA DE UN MAESTROS ------------------------------------

CREATE PROCEDURE Consulta_maestros()
BEGIN
   SELECT nombre, apellidos, email
   FROM Maestros;
END //

DELIMITER ;

DELIMITER //

#----------------------------------- CONSULTA DE UN MAESTRO ------------------------------------


CREATE PROCEDURE Consulta_maestro
(
   IN nombre_a_buscar VARCHAR(50),
   IN apellidos_a_buscar VARCHAR(50)
)
BEGIN
   SELECT nombre, apellidos, email
   FROM Maestros
   WHERE 
      (nombre LIKE CONCAT('%', nombre_a_buscar, '%') OR nombre_a_buscar IS NULL) AND 
      (apellidos LIKE CONCAT('%', apellidos_a_buscar, '%') OR apellidos_a_buscar IS NULL);
END //

DELIMITER ;

#----------------------------------- ELIMINAR ------------------------------------

DELIMITER //

CREATE PROCEDURE Eliminar_maestro
(
   IN id_maestro_a_eliminar INT
)
BEGIN
   DELETE FROM Maestros
   WHERE id = id_maestro_a_eliminar;
END //

DELIMITER ;

DELIMITER //

#----------------------------------- MODIFICAR ------------------------------------

CREATE PROCEDURE Modificar_maestro
(
   IN id_maestro_maestrosa_buscar INT,
   IN nuevo_nombre VARCHAR(50),
   IN nuevos_apellidos VARCHAR(50),
   IN nuevo_email VARCHAR(50)
)
BEGIN
   UPDATE Maestros
   SET nombre = nuevo_nombre, apellidos = nuevos_apellidos, email = nuevo_email
   WHERE id = id_maestro_a_buscar;
END //

DELIMITER ;

