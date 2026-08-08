-- ============================================================
-- Datos iniciales — cursos, materias, profesores y horarios 2026
-- ============================================================

INSERT INTO cursos (id, nombre) VALUES (1,'1A'), (2,'1B'), (3,'2A'), (4,'2B'), (5,'3E'), (6,'3I'), (7,'4E'), (8,'4I'), (9,'5E'), (10,'5I'), (11,'6E'), (12,'6I');

INSERT INTO materias (id,nombre) VALUES
(1,'Artes visuales'),
(2,'Historia'),
(3,'Lengua'),
(4,'Ingles'),
(5,'Geografia'),
(6,'Matematica'),
(7,'Cs. Naturales'),
(8,'Fec'),
(9,'TPPI'),
(10,'Ed. Fisica'),
(11,'TPPE'),
(12,'Musica'),
(13,'Co. Social'),
(14,'Dibujo Tecnico'),
(15,'Teatro'),
(16,'Ed. Tecnologica'),
(17,'Fisica'),
(18,'Quimica'),
(19,'Electrotecnia'),
(20,'LPP'),
(21,'Dibujo Tecnico Asistido'),
(22,'Biologia'),
(23,'Programacion I'),
(24,'TIC'),
(25,'Software de app'),
(26,'Ofimatica'),
(27,'Electrotecnia II'),
(28,'Politica y Ciudania'),
(29,'Teoria de circuitos'),
(30,'Tecnologia de los materiales'),
(31,'LPPE II'),
(32,'Mediciones Electricas I'),
(33,'Sistemas de Control'),
(34,'Electronica I'),
(35,'Programacion II'),
(36,'Lab. Hardware I'),
(37,'Analisis Sistemas'),
(38,'Investigacion Operativa'),
(39,'Arq. de las Computadoras'),
(40,'Sistemas Operativos'),
(41,'Teleinformatica'),
(42,'Mantenimiento de Hardware'),
(43,'Prod. y Serv. Elect I'),
(44,'Electronica II'),
(45,'Mediciones Electronicas'),
(46,'Maq. e Instalaciones Electricas'),
(47,'Programacion y sistemas Proc I'),
(48,'Sist. y Equipo de Telecomunicacion'),
(49,'Practica Profecionalizante'),
(50,'Orientacion y Tutoria'),
(51,'Administracion de Recursos'),
(52,'Economia'),
(53,'Prot. y Mant. de Datos'),
(54,'Programacion III'),
(55,'Lab. de redes I'),
(56,'Mant. de Software'),
(57,'Lab. de Hardware II'),
(58,'Sist. Audio-Video'),
(59,'Electronica III'),
(60,'Prod. y Serv. Elect II'),
(61,'Prog. y Sist. de Proce. II'),
(62,'Administracion de Recursos II'),
(63,'Elect. Ind. y de Pot.'),
(64,'Sist. de Instr. y Control'),
(65,'Seg. e Higene en el Trabajo'),
(66,'Economia y Marco Juridico'),
(67,'Sist. de Equi. de Telecom. II'),
(68,'Comunicacion de Datos'),
(69,'Lab. de Software'),
(70,'Lab. de Redes II'),
(71,'Programacion IV'),
(72,'Seguridad Informatica'),
(73,'Etica y Leg. Laboral'),
(74,'Proyecto Integrador'),
(75,'Form. y Eval de Proyectos');

INSERT INTO materias (id, nombre) VALUES (76, 'ORG. Y GESTIÓN'), (77, 'REDES DE AREA LOCAL'), (78, 'Consulta');

INSERT INTO profesores (id,nombre) VALUES
(1, 'Susana Ferreira'),
(2, 'Carla Cañas'),
(3, 'Guadalupe Badino'),
(4, 'Paloma Lafalla'),
(5, 'Francisco Rojas'),
(6, 'Mariana Rivas'),
(7, 'Esteban Dacuña'),
(8, 'Estefania Roca'),
(9, 'Mario Papetti'),
(10, 'Nicolas Bartolomeo'),
(11, 'Dario Paez'),
(12, 'Raquel Romero'),
(13, 'Cintia Garcia'),
(14, 'Mariel Perrone'),
(15, 'Mariela Moron'),
(16, 'Matias Castro'),
(17, 'Renzo Galdeano'),
(18, 'Matias Grima'),
(19, 'Alejandro Marchena'),
(20, 'Patricio Rovelli'),
(21, 'Luis Cuesta'),
(22, 'Omar Arias'),
(23, 'Ariadna Orellano'),
(24, 'Andres Martin'),
(25, 'Johana Sanchez'),
(26, 'Daniel Quinteros'),
(27, 'Noelia Agüero'),
(28, 'Morelli'),
(29, 'Marcos Adrover'),
(30, 'Bagoros'),
(31, 'Lucca Rando'),
(32, 'Nicolas Perez'),
(33, 'Damian Pedraza'),
(34, 'Mariano Egea'),
(35, 'German Gonzales'),
(36, 'Alejandro Hector Correa'),
(37, 'Raul Vargas'),
(38, 'Guillermo Sanchez'),
(39, 'Gema Pont'),
(40, 'Rocio Barbera'),
(41, 'Patricia Furci'),
(42, 'Jazmin Perez'),
(43, 'Viviana Priolo'),
(44, 'Fanyana Gonzales'),
(45, 'Eliana Allegretti'),
(46, 'Gabriel Perez'),
(47, 'Silvia Curadelli'),
(48, 'Natasha Bertaina'),
(49, 'Paula Di Cesare'),
(50, 'Paula Marañon'),
(51, 'Fernando Morales'),
(52, 'Mauricio Pinti'),
(53, 'Leandro Sanchez'),
(54, 'Sergio Barroso'),
(55, 'Matias Albornoz'),
(56, 'Ceferino Mulet'),
(57, 'Gabriela Millares'),
(58, 'Omar Cardenas'),
(59, 'Natalia Perez'),
(60, 'Carolina Robelin'),
(61, 'Bacha'),
(62, 'Arena'),
(63, 'Yanina Defeliche'),
(64, 'Federico Botaro'),
(65, 'Pablo Ontiveros'),
(66, 'Carlos Cernocky'),
(67, 'Santiago Guercio'),
(68, 'Andres Altamira'),
(69, 'Alejandro Cortinez'),
(70, 'Diego Jerez'),
(71, 'Alejandro Gamez'),
(72, 'Martin Herrera'),
(73, 'David Portal'),
(74, 'Carla Fabretti');

INSERT INTO profesores (id, nombre) VALUES (75, 'Carla Caña'), (76, 'Adrian Prado'), (77, 'Melina Macagno'), (78, 'Práticas Profesionalizantes');

INSERT INTO horarios (id_curso, id_materia, id_profesor, dia, hora_inicio, hora_fin) VALUES
(1, 1, 1, 'Lunes', '07:45', '09:05'),  -- Artes Visuales - Susana
(1, 2, 2, 'Lunes', '09:15', '11:30'),  -- Historia - C. Cañas
(1, 3, 3, 'Lunes', '11:30', '13:00'),  -- Lengua - Guadalupe
(1, 4, 4, 'Lunes', '14:00', '16:10'),  -- Ingles - Paloma Lafalla
(1, 5, 39, 'Martes', '07:45', '09:05'),  -- Geografia - Gema Pont
(1, 6, 40, 'Martes', '09:15', '11:30'),  -- Matematica - Rocio Barbera
(1, 7, 5, 'Martes', '11:30', '13:00'),  -- Cs Naturales - Rojas
(1, 8, 2, 'Martes', '14:00', '16:10'),  -- Fec - Carla Caña
(1, 5, 39, 'Miércoles', '07:45', '09:05'),  -- Geografia - Gema Pont
(1, 3, 3, 'Miércoles', '09:15', '10:35'),  -- Lengua - Guadalupe
(1, 4, 4, 'Miércoles', '10:50', '13:00'),  -- Ingles - Paloma Lafalla
(1, 9, 41, 'Miércoles', '14:00', '16:10'),  -- Taller Pre Prof. Infor. - Furci
(1, 10, 60, 'Jueves', '07:45', '09:55'),  -- Educacion Fisica - Robelin
(1, 5, 39, 'Jueves', '09:55', '11:30'),  -- Geografia - Gema Pont
(1, 7, 5, 'Jueves', '11:30', '13:00'),  -- Ciencias Naturales - Francisco Rojas
(1, 6, 40, 'Jueves', '14:00', '16:10'),  -- Matematicas - Rocio Barbera
(1, 11, 9, 'Viernes', '07:45', '09:55'),  -- TPPE - Papetti
(1, 3, 3, 'Viernes', '09:55', '11:30'),  -- Lengua - Guadalupe
(1, 12, 70, 'Viernes', '11:30', '13:00'),  -- Musica - Diego Jerez
(2, 7, 5, 'Lunes', '07:45', '09:05'),  -- Cs. Naturales - Francisco Rojas
(2, 1, 1, 'Lunes', '09:15', '10:35'),  -- Artes Visuales - Susana
(2, 4, 6, 'Lunes', '10:50', '13:00'),  -- Ingles - Rivas M.Antonella
(2, 3, 3, 'Lunes', '14:00', '16:10'),  -- Lengua - Guadalupe
(2, 6, 40, 'Martes', '07:45', '09:05'),  -- Matematicas - Rocio Barbera
(2, 5, 39, 'Martes', '09:15', '10:35'),  -- Geografia - Gema Pont
(2, 8, 2, 'Martes', '10:50', '13:00'),  -- Fec - Cañas
(2, 9, 41, 'Martes', '14:00', '16:10'),  -- Tppi - Furci
(2, 7, 5, 'Miércoles', '07:45', '09:05'),  -- Cs. Naturales - Francisco Rojas
(2, 5, 39, 'Miércoles', '09:15', '10:35'),  -- Geografia - Gema Pont
(2, 3, 3, 'Miércoles', '10:50', '13:00'),  -- Lengua - Guadalupe
(2, 11, 9, 'Miércoles', '14:00', '16:10'),  -- TPPE - Papetti
(2, 5, 39, 'Jueves', '07:45', '09:05'),  -- Geografia - Gema Pont
(2, 4, 6, 'Jueves', '09:15', '11:30'),  -- Ingles - Rivas M.Antonella
(2, 6, 40, 'Jueves', '11:30', '13:00'),  -- Matematicas - Rocio Barbera
(2, 2, 2, 'Jueves', '14:00', '16:10'),  -- Historia - Cañas
(2, 10, 60, 'Viernes', '07:45', '09:55'),  -- Educacion Fisica - Robelin
(2, 6, 40, 'Viernes', '09:55', '11:30'),  -- Matematicas - Rocio Barbera
(2, 12, 71, 'Viernes', '11:30', '13:00'),  -- Musica - Alejandro Gamez
(3, 13, 7, 'Lunes', '07:45', '09:05'),  -- Co. Social - Esteban P. Dacuña
(3, 3, 8, 'Lunes', '09:15', '10:35'),  -- Lengua - Estefania Roca
(3, 11, 9, 'Lunes', '10:50', '12:10'),  -- Taller Pre Prof. Electrónica - M.Papetti
(3, 9, 10, 'Lunes', '13:50', '14:00'),  -- Taller Pre Prof. Informatica - N.Barrtolomeo
(3, 4, 11, 'Lunes', '14:40', '16:50'),  -- Inglés - Darío Paez
(3, 14, 12, 'Martes', '07:45', '09:05'),  -- Dibujo Técnico - Raquel Romero
(3, 6, 42, 'Martes', '09:15', '11:30'),  -- Matemática - Jazmín Perez
(3, 9, 41, 'Martes', '11:30', '13:00'),  -- Taller Pre Prof. Informatica - Patricia Furci
(3, 11, 9, 'Martes', '14:00', '15:20'),  -- Taller Pre Prof. Electrónica - M.Papetti
(3, 7, 5, 'Martes', '15:30', '16:50'),  -- Cs. Naturales - Francisco Rojas
(3, 3, 8, 'Miércoles', '07:45', '09:05'),  -- Lengua - Estefania Roca
(3, 7, 5, 'Miércoles', '09:15', '11:30'),  -- Cs. Naturales - Francisco Rojas
(3, 2, 58, 'Miércoles', '11:30', '14:00'),  -- Historia - Omar Cárdenas
(3, 4, 11, 'Miércoles', '14:40', '16:50'),  -- Inglés - Darío Paez
(3, 6, 42, 'Jueves', '07:45', '09:05'),  -- Matemática - Jazmín Perez
(3, 15, 64, 'Jueves', '09:15', '10:35'),  -- Teatro - Federico Botaro
(3, 16, 41, 'Jueves', '10:50', '13:00'),  -- Ed. Tecnológica - Patricia Furci
(3, 8, 58, 'Jueves', '14:00', '15:20'),  -- FEC - Omar Cárdenas
(3, 14, 12, 'Jueves', '15:30', '16:50'),  -- Dibujo Técnico - Raquel Romero
(3, 3, 8, 'Viernes', '07:45', '09:55'),  -- Lengua - Estefania Roca
(3, 10, 60, 'Viernes', '09:55', '12:10'),  -- Ed. Física - Carolina Robelin
(3, 6, 42, 'Viernes', '14:00', '14:30'),  -- Matemática - Jazmín Perez
(3, 8, 58, 'Viernes', '14:40', '15:20'),  -- FEC - Omar Cárdenas
(4, 14, 12, 'Lunes', '07:45', '09:05'),  -- Dibujo Técnico - Raquel Romero
(4, 4, 13, 'Lunes', '09:15', '11:30'),  -- Inglés - Cintia García
(4, 3, 14, 'Lunes', '11:30', '13:00'),  -- Lengua - Mariel Perrone
(4, 11, 9, 'Lunes', '14:00', '16:50'),  -- Taller Pre Prof. Electrónica - M.Papetti
(4, 13, 7, 'Martes', '07:45', '09:05'),  -- Co. Social - Esteban P. Dacuña
(4, 3, 14, 'Martes', '09:15', '11:30'),  -- Lengua - Mariel Perrone
(4, 6, 43, 'Martes', '11:30', '13:00'),  -- Matemática - Viviana Priolo
(4, 2, 44, 'Martes', '14:00', '16:10'),  -- Historia - Fanyana Gonzalez
(4, 16, 41, 'Martes', '16:10', '16:50'),  -- Ed. Tecnologìca - Patricia Furci
(4, 7, 59, 'Miércoles', '07:45', '09:55'),  -- Cs. Naturales - Natalia Perez
(4, 10, 60, 'Miércoles', '09:55', '12:10'),  -- Ed. Física - Carolina Robelin
(4, 16, 41, 'Miércoles', '12:20', '13:40'),  -- Ed. Tecnologìca - Patricia Furci
(4, 8, 58, 'Miércoles', '14:40', '16:50'),  -- FEC - Omar Cárdenas
(4, 6, 43, 'Jueves', '07:45', '09:55'),  -- Matemática - Viviana Priolo
(4, 3, 14, 'Jueves', '09:55', '11:30'),  -- Lengua - Mariel Perrone
(4, 15, 64, 'Jueves', '11:30', '13:00'),  -- Teatro - Federico Botaro
(4, 14, 12, 'Jueves', '14:00', '15:20'),  -- Dibujo Técnico - Raquel Romero
(4, 7, 59, 'Jueves', '15:30', '16:50'),  -- Cs. Naturales - Natalia Perez
(4, 9, 10, 'Viernes', '07:45', '09:05'),  -- Taller Pre Prof. Informatica - N.Barrtolomeo
(4, 6, 43, 'Viernes', '09:15', '10:35'),  -- Matemática - Viviana Priolo
(4, 4, 13, 'Viernes', '10:50', '13:00'),  -- Inglés - Cintia García
(4, 9, 41, 'Viernes', '14:00', '14:30'),  -- Taller Pre Prof. Informatica - Patricia Furci
(4, 72, 41, 'Viernes', '14:40', '15:20'),  -- Taller Pre Pfrof. Informàtica - Patricia Furci
(5, 6, 15, 'Lunes', '07:45', '09:05'),  -- Matematica - Mariela Moron
(5, 17, 16, 'Lunes', '09:15', '10:35'),  -- Fisica - Matías Castro
(5, 4, 17, 'Lunes', '10:50', '13:00'),  -- Ingles - Renzo Galdeano
(5, 5, 18, 'Lunes', '14:00', '16:10'),  -- Geografia - Matías Grima
(5, 17, 16, 'Martes', '07:45', '09:05'),  -- Fisica - Matías Castro
(5, 18, 45, 'Martes', '09:15', '10:35'),  -- Quimica - C.Allegretti
(5, 19, 33, 'Martes', '10:50', '12:10'),  -- ELECTROTECNIA - Damián Pedraza
(5, 20, 31, 'Martes', '13:10', '15:20'),  -- LPP - Lucca Rando
(5, 20, 31, 'Miércoles', '07:45', '09:05'),  -- LPP - Lucca Rando
(5, 3, 27, 'Miércoles', '09:15', '10:35'),  -- Lengua - Noelia Aguero
(5, 19, 33, 'Miércoles', '10:50', '12:10'),  -- ELECTROTECNIA - Damián Pedraza
(5, 10, 38, 'Miércoles', '14:00', '16:10'),  -- Ed Fisica - Guille
(5, 18, 45, 'Jueves', '07:45', '09:05'),  -- Quimica - C.Allegretti
(5, 3, 27, 'Jueves', '09:15', '10:35'),  -- Lengua - Noelia Aguero
(5, 2, 75, 'Jueves', '10:50', '13:00'),  -- Historia - Carla Caña
(5, 20, 31, 'Jueves', '14:00', '15:20'),  -- LPP - Lucca Rando
(5, 21, 65, 'Jueves', '15:30', '16:50'),  -- Dib. Tecnico asistido - Pablo Ontiveros
(5, 21, 65, 'Viernes', '07:45', '09:05'),  -- Dib. Tecnico asistido - Pablo Ontiveros
(5, 6, 15, 'Viernes', '09:15', '11:30'),  -- Matematica - Mariela Moron
(5, 22, 5, 'Viernes', '11:30', '14:00'),  -- Biologia - Francisco Rojas
(6, 23, 19, 'Lunes', '07:45', '09:05'),  -- Programacion I - A.Marchena
(6, 24, 20, 'Lunes', '09:15', '10:35'),  -- TIC - Rovelli
(6, 25, 21, 'Lunes', '10:50', '13:00'),  -- Software de app - Luis Cuesta
(6, 4, 17, 'Lunes', '14:00', '16:10'),  -- Ingles - Renzo Galdeano
(6, 6, 46, 'Martes', '07:45', '09:55'),  -- Matematica - Gabriel Perez
(6, 17, 16, 'Martes', '09:55', '11:30'),  -- Fisica - Matias Castro
(6, 18, 47, 'Martes', '11:30', '13:00'),  -- Quimica - Curadelli
(6, 10, 38, 'Martes', '14:00', '16:10'),  -- Ed Fisica - Guille
(6, 6, 46, 'Miércoles', '07:45', '09:05'),  -- Matematica - Gabriel Perez
(6, 17, 16, 'Miércoles', '09:15', '10:35'),  -- Fisica - Matias Castro
(6, 3, 27, 'Miércoles', '10:50', '12:10'),  -- Lengua - Noelia Aguero
(6, 22, 5, 'Miércoles', '12:20', '15:20'),  -- Biologia - Rojas
(6, 25, 21, 'Miércoles', '15:30', '16:50'),  -- Software de app - Luis Cuesta
(6, 23, 19, 'Jueves', '07:45', '09:05'),  -- Programacion I - A.Marchena
(6, 23, 10, 'Jueves', '09:15', '10:35'),  -- Programacion I - N.Bartolomeo
(6, 2, 58, 'Jueves', '10:50', '13:00'),  -- Historia - Cardenas
(6, 5, 18, 'Jueves', '14:00', '16:10'),  -- Geografia - Grima
(6, 18, 47, 'Viernes', '07:45', '09:05'),  -- Quimica - Curadelli
(6, 3, 27, 'Viernes', '09:15', '10:35'),  -- Lengua - Noelia Aguero
(6, 26, 20, 'Viernes', '10:50', '13:00'),  -- Ofimatica - Rovelli
(7, 27, 22, 'Lunes', '07:45', '09:05'),  -- Electrotecnia ll - Arias
(7, 28, 23, 'Lunes', '09:15', '10:35'),  -- Política y Ciudadanía - A.Orellano
(7, 29, 24, 'Lunes', '10:50', '12:30'),  -- Teoria de Circuitos - A.Martín
(7, 30, 25, 'Lunes', '14:00', '16:10'),  -- Tec de los Materiales - Johana Sanchez
(7, 20, 76, 'Martes', '07:45', '10:35'),  -- LPP 2 - Adrian Prado
(7, 23, 49, 'Martes', '10:50', '12:30'),  -- Med Elec l - Paula Di Cesare
(7, 27, 22, 'Martes', '14:00', '15:00'),  -- Electrotecnia ll - Arias
(7, 28, 23, 'Martes', '15:30', '16:10'),  -- Política y Ciudadanía - A.Orellano
(7, 4, 61, 'Miércoles', '07:45', '09:55'),  -- Inglés - Bacha
(7, 64, 22, 'Miércoles', '09:55', '12:10'),  -- Sist de Control - Arias
(7, 17, 16, 'Miércoles', '13:10', '15:00'),  -- Fisica - Castro
(7, 6, 62, 'Miércoles', '15:30', '16:50'),  -- Matemática - F.Arena
(7, 6, 62, 'Jueves', '07:45', '09:55'),  -- Matemática - F.Arena
(7, 17, 16, 'Jueves', '09:55', '11:30'),  -- Fisica - Castro
(7, 3, 27, 'Jueves', '11:30', '14:00'),  -- Lengua - Noelia Aguero
(7, 10, 63, 'Jueves', '14:40', '16:50'),  -- Ed.Fisica - Yanina Defeliche
(7, 20, 76, 'Viernes', '07:45', '10:35'),  -- LPP 2 - Adrian Prado
(7, 34, 72, 'Viernes', '10:50', '13:40'),  -- Electronica l - Martín Herrera
(8, 35, 26, 'Lunes', '07:45', '09:05'),  -- Programación II - D.Quinteros
(8, 3, 27, 'Lunes', '09:15', '10:35'),  -- Lengua - Agüero N
(8, 17, 16, 'Lunes', '10:50', '13:00'),  -- Física - Castro M
(8, 36, 28, 'Lunes', '14:00', '16:50'),  -- Lab. Hardware l - J.Morelli
(8, 37, 50, 'Martes', '07:45', '09:05'),  -- Análisis Sist - Marañon P
(8, 38, 47, 'Martes', '09:15', '11:30'),  -- Inv. Operativa - Curadelli S
(8, 28, 23, 'Martes', '11:30', '14:00'),  -- Política y Ciudadanía - A.Orellano
(8, 39, 51, 'Martes', '14:40', '16:50'),  -- Arq. de las Computadoras - F.Morales
(8, 10, 63, 'Miércoles', '07:45', '09:55'),  -- Ed.Fisica - Yanina Defeliche
(8, 4, 61, 'Miércoles', '09:55', '12:10'),  -- Inglés - Bacha C
(8, 6, 46, 'Miércoles', '13:10', '15:20'),  -- Matemática - Perez G
(8, 17, 16, 'Miércoles', '15:30', '16:50'),  -- Física - Castro M
(8, 40, 66, 'Jueves', '07:45', '09:55'),  -- Sistemas Operativos - Cernocky C
(8, 41, 21, 'Jueves', '09:55', '12:10'),  -- Teleinformática - Cuesta L
(8, 3, 27, 'Jueves', '12:20', '13:00'),  -- Lengua - Aguero N
(8, 42, 54, 'Jueves', '14:00', '16:50'),  -- Mant. Hardware - Barroso S
(8, 35, 26, 'Viernes', '07:45', '10:35'),  -- Programación II - D.Quinteros
(8, 6, 46, 'Viernes', '10:50', '12:10'),  -- Matemática - Perez G
(9, 10, 29, 'Lunes', '07:45', '09:55'),  -- Ed Fisica - M.Adrover
(9, 43, 30, 'Lunes', '09:55', '11:30'),  -- Prod y Serv Elect I - Bagoros
(9, 44, 31, 'Lunes', '11:30', '13:00'),  -- Electrónica ll - Lucca Rando
(9, 45, 32, 'Lunes', '14:00', '16:10'),  -- Med Electron - Nicolas Perez
(9, 46, 30, 'Martes', '07:45', '09:55'),  -- Maq e inst.elect - Bagoros
(9, 47, 35, 'Martes', '09:55', '13:00'),  -- Prog y Sist Proc I - Germán Gonzalez
(9, 48, 24, 'Martes', '14:00', '15:20'),  -- Sist. Y Equipo de telec - Andres Martin
(9, 43, 30, 'Miércoles', '07:45', '09:05'),  -- Prod y Serv Elect I - Bagoros
(9, 44, 31, 'Miércoles', '09:15', '10:35'),  -- Electrónica ll - Lucca Rando
(9, 43, 30, 'Miércoles', '10:50', '14:40'),  -- Prod y Serv Elect I - Bagoros
(9, 48, 24, 'Miércoles', '14:40', '15:30'),  -- Sist. Y Equipo de telec - Andres Martin
(9, 49, 20, 'Jueves', '07:45', '09:55'),  -- Pract prof - P.Rovelli / A. Martin
(9, 4, 67, 'Jueves', '09:55', '12:10'),  -- Inglés - Santi Guercio
(9, 6, 33, 'Jueves', '13:00', '15:20'),  -- Matematicas - Damián Pedraza
(9, 50, 68, 'Jueves', '15:30', '16:50'),  -- Orientación y tutoría - Andres Altamira
(9, 3, 3, 'Viernes', '07:45', '09:55'),  -- Lengua - Guada Badino
(9, 51, 47, 'Viernes', '09:55', '12:10'),  -- Adm de Recursos - Silvia Curadelli
(9, 43, 30, 'Viernes', '12:20', '13:10'),  -- Prod y Serv Elect I - Bagoros
(10, 3, 3, 'Lunes', '07:45', '09:55'),  -- LENGUA - Guada Badino
(10, 10, 29, 'Lunes', '09:55', '12:10'),  -- Ed Fisica - M.Adrover
(10, 6, 33, 'Lunes', '13:10', '15:20'),  -- MATEMÁTICA - D.Pedraza
(10, 52, 77, 'Martes', '07:45', '09:05'),  -- ECONOMÍA - Melina Macagno
(10, 53, 50, 'Martes', '09:15', '10:35'),  -- PROT. Y MANT. DE DATOS - Paula Marañon
(10, 76, 53, 'Martes', '10:50', '13:00'),  -- ORG. Y GESTIÓN - Sanchez Leandro
(10, 77, 54, 'Martes', '14:00', '16:10'),  -- REDES DE AREA LOCAL - Sergio Barroso
(10, 52, 77, 'Miércoles', '07:45', '09:05'),  -- ECONOMÍA - Melina Macagno
(10, 53, 50, 'Miércoles', '09:15', '10:35'),  -- PROT. Y MANT. DE DATOS - Paula Marañon
(10, 54, 26, 'Miércoles', '10:50', '13:00'),  -- PROGRAMACIÓN lll - D.Quinteros
(10, 55, 54, 'Miércoles', '14:00', '16:50'),  -- LAB. DE REDES I - Sergio Barroso
(10, 4, 67, 'Jueves', '07:45', '09:55'),  -- INGLÉS - Santi Guercio
(10, 49, 20, 'Jueves', '09:55', '12:10'),  -- Pract prof - P.Rovelli / A. Martin
(10, 50, 68, 'Jueves', '13:10', '14:30'),  -- ORIENTACIÓN Y TUTORÍA - Andres Altamira
(10, 56, 51, 'Jueves', '14:40', '16:50'),  -- MANT. DE SOFTW. - F.Morales
(10, 57, 73, 'Viernes', '07:45', '10:35'),  -- LAB. HARDWARE II - David Portal
(10, 54, 26, 'Viernes', '10:50', '13:00'),  -- PROGRAMACIÓN lll - D.Quinteros
(11, 58, 34, 'Lunes', '07:45', '09:05'),  -- Sis de Audio-Video - Egea
(11, 59, 22, 'Lunes', '09:15', '11:30'),  -- Electronica lll - Omar Arias
(11, 60, 30, 'Lunes', '11:30', '13:10'),  -- Prod y Srv Elec ll - Bagoros
(11, 61, 35, 'Lunes', '14:40', '16:10'),  -- Prog y SIS de Procesamiento ll - Germán Gonzalez
(11, 62, 55, 'Martes', '07:45', '09:55'),  -- Ad de Rec ll - Albornoz
(11, 49, 22, 'Martes', '09:55', '12:10'),  -- Pract Profesionalizante - Omar Arias
(11, 60, 30, 'Martes', '13:10', '14:00'),  -- Prod y Srv Elec ll - Bagoros
(11, 61, 35, 'Martes', '14:40', '16:10'),  -- Prog y SIS de Procesamiento ll - Germán Gonzalez
(11, 59, 22, 'Miércoles', '07:45', '09:05'),  -- Electronica lll - Omar Arias
(11, 63, 9, 'Miércoles', '09:15', '12:10'),  -- Elec ind y de pot - Mario Papetti
(11, 64, 22, 'Miércoles', '13:10', '15:20'),  -- Sis de Instrumentacion y Cont - Omar Arias
(11, 65, 69, 'Jueves', '07:45', '09:05'),  -- Seg e Higiene en el Trabajo - Ale Cortinez
(11, 60, 30, 'Jueves', '09:15', '10:35'),  -- Prod y Srv Elec ll - Bagoros
(11, 10, 29, 'Jueves', '10:50', '12:10'),  -- Ed Fisica - M.Adrover
(11, 66, 52, 'Jueves', '13:10', '15:20'),  -- Econ y Marco Juridico - Mauricio Pinti
(11, 48, 36, 'Viernes', '07:45', '09:55'),  -- Sist de Equipo de Telecomunicacion ll - Hector Correa
(11, 60, 30, 'Viernes', '09:55', '12:10'),  -- Prod y Srv Elec ll - Bagoros
(11, 50, 74, 'Viernes', '12:20', '13:10'),  -- Orientacion y tutoria - Carla Fabretti
(12, 68, 36, 'Lunes', '07:45', '09:05'),  -- Comunicación de Datos - Correa Hector
(12, 69, 26, 'Lunes', '09:15', '10:35'),  -- Lab Software - D.Quinteros
(12, 70, 37, 'Lunes', '10:50', '13:00'),  -- Lab de Redes ll - Raúl Vargas
(12, 10, 38, 'Lunes', '14:00', '15:20'),  -- Ed. Fisca - Guillermo Sanchez
(12, 71, 19, 'Lunes', '15:30', '16:50'),  -- Programación IV - Alejandro Marchena
(12, 72, 56, 'Martes', '07:45', '09:05'),  -- Seguridad Informatica - Ceferino Mulet
(12, 73, 57, 'Martes', '09:15', '10:35'),  -- Etica y Leg Laboral - Millares Gabriela
(12, 74, 26, 'Martes', '10:50', '12:10'),  -- Proy Integrador - Quinteros Daniel
(12, 69, 26, 'Martes', '13:10', '15:20'),  -- Lab Software - D.Quinteros
(12, 78, 78, 'Martes', '16:10', '17:30'),  -- Consulta - Práticas Profesionalizantes
(12, 68, 36, 'Miércoles', '07:45', '09:05'),  -- Comunicación de Datos - Correa Hector
(12, 73, 57, 'Miércoles', '09:15', '10:35'),  -- Etica y Leg Laboral - Millares Gabriela
(12, 49, 50, 'Miércoles', '10:50', '13:00'),  -- Pract Profesionalizante - Paula Marañon
(12, 75, 55, 'Miércoles', '14:00', '15:20'),  -- Form y Eval De Proyectos - Albornoz
(12, 74, 26, 'Jueves', '07:45', '09:55'),  -- Proy Integrador - Quinteros Daniel
(12, 71, 19, 'Jueves', '09:55', '13:00'),  -- Programación IV - Alejandro Marchena
(12, 75, 55, 'Jueves', '14:00', '15:20'),  -- Form y Eval De Proyectos - Albornoz
(12, 72, 56, 'Viernes', '07:45', '09:05'),  -- Seguridad Informatica - Ceferino Mulet
(12, 70, 37, 'Viernes', '09:15', '10:35'),  -- Lab de Redes ll - Raúl Vargas
(12, 50, 74, 'Viernes', '10:50', '12:10'),  -- Orientacion y tutoria - Carla Fabretti
(12, 74, 26, 'Viernes', '13:10', '14:00');

-- ------------------------------------------------------------
-- Inventario (catálogo de elementos del taller)
-- categoria queda sin asignar (NULL): se puede completar después
-- ------------------------------------------------------------
INSERT INTO inventario (codigo, nombre, categoria, estado) VALUES
('05''001''007''000003', 'Compresor', NULL, 'disponible'),
('05''001''012''000005', 'DREMEL ROJO', NULL, 'disponible'),
('05''001''011''000003', 'Est. De Sold.', NULL, 'disponible'),
('05''001''011''000004', 'Est. De Sold.', NULL, 'disponible'),
('05''001''005''000009', 'FUENTE', NULL, 'disponible'),
('05''001''005''000010', 'FUENTE', NULL, 'disponible'),
('Fuente Simple', 'FUENTE', NULL, 'disponible'),
('05''001''005''000006', 'fuente lineal', NULL, 'disponible'),
('fuente''01', 'Fuente Partida(1)', NULL, 'disponible'),
('fuente''02', 'Fuente Partida(2)', NULL, 'disponible'),
('fuente''03', 'Fuente(1)', NULL, 'disponible'),
('fuente''04', 'Fuente(2)', NULL, 'disponible'),
('05''001''005''000008', 'Generador de señal', NULL, 'disponible'),
('gen''01', 'Generador De Señal(1)', NULL, 'disponible'),
('gen''02', 'Generador De Señal(2)', NULL, 'disponible'),
('C5', 'Impresora HP', NULL, 'disponible'),
('httpsÑ--me''qr.com-osmcwoYO', 'llave terraza', NULL, 'disponible'),
('Microfono?Vincha', 'Microfono Inalambrico', NULL, 'disponible'),
('LupaElectronica', 'microscopio', NULL, 'disponible'),
('MicSnowBall', 'MicSnowBall', NULL, 'disponible'),
('02''005''003''000326', 'Monitor_Samsung_1', NULL, 'disponible'),
('Multimetros UNI''T', 'Multimetros UNI''T', NULL, 'disponible'),
('02''005''002''000195', 'Notebook', NULL, 'disponible'),
('02''005''002''000048', 'Netbook', NULL, 'disponible'),
('02''005''002''000061', 'Netbook', NULL, 'disponible'),
('02''005''002''000063', 'Netbook', NULL, 'disponible'),
('02''005''002''000064', 'Netbook', NULL, 'disponible'),
('02''005''002''000068', 'Netbook', NULL, 'disponible'),
('02''005''002''000116', 'Netbook', NULL, 'disponible'),
('02''005''002''000117', 'Netbook', NULL, 'disponible'),
('02''005''002''000118', 'Netbook', NULL, 'disponible'),
('02''005''002''000119', 'Netbook', NULL, 'disponible'),
('02''005''002''000120', 'Netbook', NULL, 'disponible'),
('02''005''002''000121', 'Netbook', NULL, 'disponible'),
('02''005''002''000125', 'Netbook', NULL, 'disponible'),
('02''005''002''000126', 'Netbook', NULL, 'disponible'),
('02''005''002''000130', 'Netbook', NULL, 'disponible'),
('02''005''002''000131', 'Netbook', NULL, 'disponible'),
('02''005''002''000132', 'Netbook', NULL, 'disponible'),
('02''005''002''000139', 'Netbook', NULL, 'disponible'),
('02''005''002''000140', 'Netbook', NULL, 'disponible'),
('02''005''002''000141', 'Netbook', NULL, 'disponible'),
('02''005''002''000142', 'Netbook', NULL, 'disponible'),
('02''005''002''000144', 'Netbook', NULL, 'baja'),
('02''005''002''000145', 'Netbook', NULL, 'disponible'),
('02''005''002''000146', 'Netbook', NULL, 'disponible'),
('02''005''002''000153', 'Netbook', NULL, 'disponible'),
('02''005''002''000155', 'Netbook', NULL, 'disponible'),
('02''005''002''000156', 'Netbook', NULL, 'disponible'),
('02''005''002''000157', 'Netbook', NULL, 'disponible'),
('02''005''002''000158', 'Netbook', NULL, 'disponible'),
('02''005''002''000159', 'Netbook', NULL, 'disponible'),
('02''005''002''000003', 'Notebook', NULL, 'disponible'),
('02''005''002''000004', 'Notebook', NULL, 'disponible'),
('02''005''002''000005', 'Notebook', NULL, 'disponible'),
('02''005''002''000006', 'Notebook', NULL, 'disponible'),
('02''005''002''000007', 'Notebook', NULL, 'disponible'),
('02''005''002''000008', 'Notebook', NULL, 'disponible'),
('02''005''002''000009', 'Notebook', NULL, 'disponible'),
('02''005''002''000010', 'Notebook', NULL, 'disponible'),
('02''005''002''000011', 'Notebook', NULL, 'disponible'),
('02''005''002''000012', 'Notebook', NULL, 'disponible'),
('02''005''002''000013', 'Notebook', NULL, 'disponible'),
('02''005''002''000014', 'Notebook', NULL, 'disponible'),
('02''005''002''000015', 'Notebook', NULL, 'disponible'),
('02''005''002''000016', 'Notebook', NULL, 'disponible'),
('02''005''002''000017', 'Notebook', NULL, 'disponible'),
('02''005''002''000018', 'Notebook', NULL, 'disponible'),
('02''005''002''000019', 'Notebook', NULL, 'disponible'),
('02''005''002''000020', 'Notebook', NULL, 'disponible'),
('02''005''002''000072', 'Notebook', NULL, 'disponible'),
('02''005''002''000073', 'Notebook', NULL, 'disponible'),
('02''005''002''000074', 'Notebook', NULL, 'disponible'),
('02''005''002''000075', 'Notebook', NULL, 'disponible'),
('02''005''002''000076', 'Notebook', NULL, 'disponible'),
('02''005''002''000077', 'Notebook', NULL, 'disponible'),
('02''005''002''000078', 'Notebook', NULL, 'disponible'),
('02''005''002''000079', 'Notebook', NULL, 'disponible'),
('02''005''002''000080', 'Notebook', NULL, 'disponible'),
('02''005''002''000081', 'Notebook', NULL, 'disponible'),
('02''005''002''000082', 'Notebook', NULL, 'disponible'),
('02''005''002''000083', 'Notebook', NULL, 'disponible'),
('02''005''002''000084', 'Notebook', NULL, 'disponible'),
('02''005''002''000085', 'Notebook', NULL, 'disponible'),
('02''005''002''000086', 'Notebook', NULL, 'disponible'),
('02''005''002''000087', 'Notebook', NULL, 'disponible'),
('02''005''002''000088', 'Notebook', NULL, 'disponible'),
('02''005''002''000089', 'Notebook', NULL, 'disponible'),
('02''005''002''000090', 'Notebook', NULL, 'disponible'),
('02''005''002''000091', 'Notebook', NULL, 'disponible'),
('02''005''002''000092', 'Notebook', NULL, 'disponible'),
('02''005''002''000093', 'Notebook', NULL, 'disponible'),
('02''005''002''000094', 'Notebook', NULL, 'disponible'),
('02''005''002''000095', 'Notebook', NULL, 'disponible'),
('02''005''002''000096', 'Notebook', NULL, 'disponible'),
('02''005''002''000097', 'Notebook', NULL, 'disponible'),
('02''005''002''000098', 'Notebook', NULL, 'disponible'),
('02''005''002''000099', 'Notebook', NULL, 'disponible'),
('02''005''002''000100', 'Notebook', NULL, 'disponible'),
('02''005''002''000101', 'Notebook', NULL, 'disponible'),
('02''005''002''000102', 'Notebook', NULL, 'disponible'),
('02''005''002''000103', 'Notebook', NULL, 'disponible'),
('02''005''002''000104', 'Notebook', NULL, 'disponible'),
('02''005''002''000105', 'Notebook', NULL, 'disponible'),
('02''005''002''000106', 'Notebook', NULL, 'disponible'),
('02''005''002''000107', 'Notebook', NULL, 'disponible'),
('02''005''002''000108', 'Notebook', NULL, 'disponible'),
('02''005''002''000110', 'Notebook', NULL, 'disponible'),
('02''005''002''000112', 'Notebook', NULL, 'disponible'),
('02''005''002''000176', 'Notebook', NULL, 'disponible'),
('02''005''002''000177', 'Notebook', NULL, 'disponible'),
('02''005''002''000178', 'Notebook', NULL, 'disponible'),
('02''005''002''000179', 'Notebook', NULL, 'disponible'),
('02''005''002''000180', 'Notebook', NULL, 'disponible'),
('02''005''002''000181', 'Notebook', NULL, 'disponible'),
('02''005''002''000182', 'Notebook', NULL, 'disponible'),
('02''005''002''000183', 'Notebook', NULL, 'disponible'),
('02''005''002''000184', 'Notebook', NULL, 'disponible'),
('02''005''002''000185', 'Notebook', NULL, 'disponible'),
('02''005''002''000186', 'Notebook', NULL, 'disponible'),
('02''005''002''000187', 'Notebook', NULL, 'disponible'),
('02''005''002''000188', 'Notebook', NULL, 'disponible'),
('02''005''002''000189', 'Notebook', NULL, 'disponible'),
('02''005''002''000190', 'Notebook', NULL, 'disponible'),
('02''005''002''000191', 'Notebook', NULL, 'disponible'),
('02''005''002''000192', 'Notebook', NULL, 'disponible'),
('02''005''002''000193', 'Notebook', NULL, 'disponible'),
('02''005''002''000194', 'Notebook', NULL, 'disponible'),
('02''005''002''000196', 'Notebook', NULL, 'disponible'),
('02''005''002''000197', 'Notebook', NULL, 'disponible'),
('02''005''002''000198', 'Notebook', NULL, 'disponible'),
('02''005''002''000199', 'Notebook', NULL, 'disponible'),
('02''005''002''000200', 'Notebook', NULL, 'disponible'),
('02''005''002''000201', 'Notebook', NULL, 'disponible'),
('02''005''002''000202', 'Notebook', NULL, 'disponible'),
('02''005''002''000203', 'Notebook Profesor', NULL, 'disponible'),
('02''005''002''000204', 'Notebook', NULL, 'disponible'),
('02''005''002''000205', 'Notebook', NULL, 'disponible'),
('02''005''002''000206', 'Notebook', NULL, 'disponible'),
('02''005''002''000207', 'Notebook', NULL, 'disponible'),
('02''005''002''000208', 'Notebook', NULL, 'disponible'),
('02''005''002''000209', 'Notebook', NULL, 'disponible'),
('02''005''002''000210', 'Notebook', NULL, 'disponible'),
('02''005''002''000211', 'Notebook', NULL, 'disponible'),
('02''005''002''000212', 'Notebook', NULL, 'disponible'),
('02''005''002''000213', 'Notebook', NULL, 'disponible'),
('02''005''002''000214', 'Notebook', NULL, 'disponible'),
('02''005''002''000217', 'Notebook', NULL, 'disponible'),
('02''005''002''000218', 'Notebook', NULL, 'disponible'),
('02''005''002''000219', 'Notebook', NULL, 'disponible'),
('02''005''002''000220', 'Notebook', NULL, 'disponible'),
('02''005''002''000221', 'Notebook', NULL, 'disponible'),
('02''005''002''000222', 'Notebook', NULL, 'disponible'),
('02''005''002''000223', 'Notebook', NULL, 'disponible'),
('02''005''002''000224', 'Notebook', NULL, 'disponible'),
('02''005''002''000225', 'Notebook', NULL, 'disponible'),
('02''005''002''000226', 'Notebook', NULL, 'disponible'),
('02''005''002''000227', 'Notebook', NULL, 'disponible'),
('02''005''002''000228', 'Notebook', NULL, 'disponible'),
('02''005''002''000229', 'Notebook', NULL, 'disponible'),
('02''005''002''000230', 'Notebook', NULL, 'disponible'),
('02''005''002''000231', 'Notebook', NULL, 'disponible'),
('02''005''002''000232', 'Notebook', NULL, 'disponible'),
('02''005''002''000233', 'Notebook', NULL, 'disponible'),
('02''005''002''000234', 'Notebook', NULL, 'disponible'),
('02''005''002''000235', 'Notebook', NULL, 'disponible'),
('02''005''002''000109', 'Notebook Profesor', NULL, 'disponible'),
('02''005''002''000111', 'Notebook Profesor', NULL, 'disponible'),
('02''005''002''000113', 'Notebook Profesor', NULL, 'disponible'),
('02''005''002''000215', 'Notebook Profesor', NULL, 'disponible'),
('02''005''002''000216', 'Notebook Profesor', NULL, 'disponible'),
('05''001''004''000019', 'Osciloscopio', NULL, 'disponible'),
('05''001''004''000020', 'Osciloscopio', NULL, 'disponible'),
('Osciloscopio', 'OSILOSCOPIO', NULL, 'disponible'),
('par_1', 'Par. de escritorio_1', NULL, 'disponible'),
('par_2', 'Par. de escritorio_2', NULL, 'disponible'),
('02''006''016''000037', 'Parlante Chico', NULL, 'disponible'),
('02''006''016''000038', 'Parlante Chico', NULL, 'disponible'),
('ParlanteGTC', 'Parlante chico', NULL, 'disponible'),
('02''006''016''000039', 'Parlante Grande', NULL, 'disponible'),
('ParlanteGrandeSKP', 'Parlante_Grande', NULL, 'disponible'),
('02''005''001''000337', 'PC Lab. 2', NULL, 'disponible'),
('02{006{009{000022', 'Proyector', NULL, 'disponible'),
('02{006{009{000023', 'Proyector', NULL, 'disponible'),
('02{006{009{000024', 'Proyector', NULL, 'disponible'),
('02{006{009{000031', 'Proyector', NULL, 'disponible'),
('02{006{009{000065', 'Proyector', NULL, 'disponible'),
('02{006{017{000021', 'Proyector', NULL, 'disponible'),
('02´006´009´000022', 'Proyector', NULL, 'disponible'),
('02''006''005''000031', 'Proyector', NULL, 'disponible'),
('02''006''005''000065', 'Proyector', NULL, 'disponible'),
('02''006''005''000089', 'Proyector', NULL, 'disponible'),
('02''006''005''000094', 'Proyector', NULL, 'disponible'),
('02''006''005''000095', 'Proyector', NULL, 'disponible'),
('02''006''009''000020', 'Proyector', NULL, 'disponible'),
('02''006''009''000022', 'Proyector', NULL, 'disponible'),
('02''006''017''000021', 'Proyector', NULL, 'disponible'),
('Puntero', 'puntero_1', NULL, 'disponible'),
('router TP''Link', 'Router TP''Link', NULL, 'disponible'),
('02''006''009''000026', 'Proyector', NULL, 'disponible'),
('YQVJ63816', 'Parlante Xiaomi', NULL, 'disponible'),
('xiaomi1', 'Parlante Xiaomi', NULL, 'disponible'),
('xiaomi2', 'Parlante Xiaomi', NULL, 'disponible'),
('xiaomi3', 'Parlante Xiaomi', NULL, 'disponible'),
('05''001''005''000007', 'Generador de señal', NULL, 'disponible'),
('AR020000597089', 'Notebook', NULL, 'disponible'),
('05''001''005''000005', 'Fuente_Doble', NULL, 'disponible');

-- ------------------------------------------------------------
-- Novedades históricas (solo la que referencia un item que sigue en el catálogo)
-- ------------------------------------------------------------
INSERT INTO novedades (fecha_hora, elemento_codigo, clasificacion, comentario) VALUES
('2023-05-09 10:00', '02''005''002''000144', 'retiro', 'netbooks que se llevo el dto de la universidad');
