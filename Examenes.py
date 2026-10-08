class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

class Estudiante(Persona):
    def __init__(self, identificador_E, nombre, identificador_G):
        super().__init__(nombre)
        self.identificador_E = identificador_E
        self.identificador_G = identificador_G

contarRegulares = lambda materia: materia > 2.5 or materia < 3.5

class Genero:
    def __init__(self, Identificador_G):
        self.Identificador_G = Identificador_G

Masculino = Genero(0)
Femenino = Genero(1)

class Materia:
    def __init__(self, Nombre_M, identificador_M):
        self.Nombre_M = Nombre_M
        self.identificador_M = identificador_M

Quimica = Materia("Quimica", 1)
Idiomas = Materia("Idiomas", 2)
Historia = Materia("Historia", 3)

list_estudiantes = [Estudiante(1, "Armando", 0, Masculino, 1, "1.1", 2, "1.8", 3, "3.3"),
                    Estudiante(2, "Nicolas", 0, Masculino, 1, "4.3", 2, "1.6", 3, "4.3"),
                    Estudiante(3, "Daniel", 0, Masculino, 1, "3.8", 2, "0.7", 3, "1.8"),
                    Estudiante(4, "Maria", 1, Femenino, 1, "0.6", 2, "2.5", 3, "4.0"),
                    Estudiante(5, "Marcela", 1, Femenino, 1, "0.5", 2, "3.8", 3, "1.2"),
                    Estudiante(6, "Alexandra", 1, Femenino, 1, "2.6", 2, "4.6", 3, "0.1")];

