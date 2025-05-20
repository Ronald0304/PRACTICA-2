#7. Crea un POO para una universidad y sus estudiantes. La universidad contiene estudiantes, pero los estudiantes pueden existir independientemente de la universidad. 
#Estudiante< nombre, carrera, semestre> Métodos: mostrar_info() (muestra el nombre, carrera y semestre del estudiante) 
#Universidad<nombre, estudiantes (lista de objetos de tipo Estudiante)> Métodos: agregar_estudiante(estudiante), mostrar_universidad() (muestra el 
#nombre de la universidad y la información de todos los estudiantes) 
#a) Implementa las clases con sus constructores, getters y setters. 
#b) Crea una universidad y agrega varios estudiantes. 
#c) Muestra la información de la universidad y sus estudiantes. 
class Estudiante:
    def __init__(self, nombre, carrera, semestre):
        self.__nombre = nombre
        self.__carrera = carrera
        self.__semestre = semestre

    def get_nombre(self):
        return self.__nombre

    def get_carrera(self):
        return self.__carrera

    def get_semestre(self):
        return self.__semestre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_carrera(self, carrera):
        self.__carrera = carrera

    def set_semestre(self, semestre):
        self.__semestre = semestre

    def mostrar_info(self):
        return f"Nombre: {self.__nombre}, Carrera: {self.__carrera}, Semestre: {self.__semestre}"

class Universidad:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__estudiantes = []

    def get_nombre(self):
        return self.__nombre

    def get_estudiantes(self):
        return self.__estudiantes

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def agregar_estudiante(self, estudiante):
        if isinstance(estudiante, Estudiante):
            self.__estudiantes.append(estudiante)
        else:
            print("Error: Solo se pueden agregar objetos de tipo Estudiante.")

    def mostrar_universidad(self):
        print(f"Universidad: {self.__nombre}")
        print("Estudiantes:")
        for est in self.__estudiantes:
            print(" ", est.mostrar_info())

def main():
    e1 = Estudiante("Ana", "Ingeniería", 3)
    e2 = Estudiante("Luis", "Medicina", 5)
    e3 = Estudiante("María", "Derecho", 2)
    e4 = Estudiante("Ronald","Informatica",2)

    u = Universidad("Universidad Mayor de San Andres")

    u.agregar_estudiante(e1)
    u.agregar_estudiante(e2)
    u.agregar_estudiante(e3)
    u.agregar_estudiante(e4)

    u.mostrar_universidad()

main()
