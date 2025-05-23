#3. Definir las clases:  Persona <ci, nombre, apellido, celular, fecha_Nac> 
#Estudiante (heredado de persona) <ru, fecha_Ingreso, semestre> Docente (heredado de persona) <nit, profesión, especialidad> 
#a) Diseñar el diagrama UML de las clases anteriores. 
#b) Implementa las clases con sus constructores, datos por defecto y mostrar. 
#c) Mostrar los estudiantes mayores de 25 años. 
#d) Mostrar al docente que tiene la profesión de “Ingeniero”, es del sexo masculino y es el mayor de todos. 
#e) Mostrar a los estudiantes y docentes que tienen el mismo apellido. 
from datetime import datetime

class Persona:
    def __init__(self, ci="0000000", nombre="Nombre", apellido="Apellido", celular="0000000000", fecha_Nac="2000-01-01", sexo="N"):
        self.__ci = ci
        self.__nombre = nombre
        self.__apellido = apellido
        self.__celular = celular
        self.__fecha_Nac = fecha_Nac
        self.__sexo = sexo

    def get_ci(self): 
        return self.__ci
    def get_nombre(self): 
        return self.__nombre
    def get_apellido(self): 
        return self.__apellido
    def get_celular(self): 
        return self.__celular
    def get_fecha_Nac(self): 
        return self.__fecha_Nac
    def get_sexo(self): 
        return self.__sexo

    def set_ci(self, ci): 
        self.__ci = ci
    def set_nombre(self, nombre): 
        self.__nombre = nombre
    def set_apellido(self, apellido): 
        self.__apellido = apellido
    def set_celular(self, celular): 
        self.__celular = celular
    def set_fecha_Nac(self, fecha_Nac): 
        self.__fecha_Nac = fecha_Nac
    def set_sexo(self, sexo): 
        self.__sexo = sexo

    def mostrar(self):
        print(f"CI: {self.__ci}, Nombre: {self.__nombre} {self.__apellido}, Celular: {self.__celular}, Fecha Nac: {self.__fecha_Nac}, Sexo: {self.__sexo}")

    def calcular_edad(self):
        nacimiento = datetime.strptime(self.__fecha_Nac, "%Y-%m-%d")
        hoy = datetime.today()
        return hoy.year - nacimiento.year - ((hoy.month, hoy.day) < (nacimiento.month, nacimiento.day))

class Estudiante(Persona):
    def __init__(self, ci="0000000", nombre="Nombre", apellido="Apellido", celular="0000000000", fecha_Nac="2000-01-01", sexo="N", ru="000", fecha_Ingreso="2020-01-01", semestre=1):
        super().__init__(ci, nombre, apellido, celular, fecha_Nac, sexo)
        self.__ru = ru
        self.__fecha_Ingreso = fecha_Ingreso
        self.__semestre = semestre

    def get_ru(self): 
        return self.__ru
    def get_fecha_Ingreso(self): 
        return self.__fecha_Ingreso
    def get_semestre(self): 
        return self.__semestre

    def set_ru(self, ru): 
        self.__ru = ru
    def set_fecha_Ingreso(self, fecha_Ingreso): 
        self.__fecha_Ingreso = fecha_Ingreso
    def set_semestre(self, semestre): 
        self.__semestre = semestre

    def mostrar(self):
        super().mostrar()
        print(f"RU: {self.__ru}, Fecha Ingreso: {self.__fecha_Ingreso}, Semestre: {self.__semestre}")

    @staticmethod
    def estudiantes_mayores_de(lista_estudiantes, edad_limite):
        print(f"\n-- Estudiantes mayores de {edad_limite} años --")
        for est in lista_estudiantes:
            if est.calcular_edad() > edad_limite:
                est.mostrar()
                print("-" * 40)

    @staticmethod
    def persona_con_el_mismo_apellido(lista_estudiantes, lista_docentes):
        print("\n------ Personas con el mismo apellido --------")
        apellidos_estudiantes = set(est.get_apellido() for est in lista_estudiantes)
        apellidos_docentes = set(doc.get_apellido() for doc in lista_docentes)

        comunes = apellidos_estudiantes & apellidos_docentes
        for apellido in comunes:
            print(f"\nApellido en común: {apellido}")
            print("Estudiantes:")
            for est in lista_estudiantes:
                if est.get_apellido() == apellido:
                    est.mostrar()
            print("Docentes:")
            for doc in lista_docentes:
                if doc.get_apellido() == apellido:
                    doc.mostrar()

class Docente(Persona):
    def __init__(self, ci="0000000", nombre="Nombre", apellido="Apellido", celular="0000000000", fecha_Nac="1980-01-01", sexo="N", nit="000", profesion="Docente", especialidad="General"):
        super().__init__(ci, nombre, apellido, celular, fecha_Nac, sexo)
        self.__nit = nit
        self.__profesion = profesion
        self.__especialidad = especialidad

    def get_nit(self):
        return self.__nit
    def get_profesion(self): 
        return self.__profesion
    def get_especialidad(self): 
        return self.__especialidad

    def set_nit(self, nit): 
        self.__nit = nit
    def set_profesion(self, profesion): 
        self.__profesion = profesion
    def set_especialidad(self, especialidad): 
        self.__especialidad = especialidad

    def mostrar(self):
        super().mostrar()
        print(f"NIT: {self.__nit}, Profesión: {self.__profesion}, Especialidad: {self.__especialidad}")

    @staticmethod
    def persona_con_el_mismo_apellido(lista_estudiantes, lista_docentes):
        Estudiante.persona_con_el_mismo_apellido(lista_estudiantes, lista_docentes)

estudiantes = [
    Estudiante("1234567", "Juan", "Perez", "789456123", "2000-05-20", "M", "RU001", "2021-02-10", 6),
    Estudiante("4567891", "Ana", "Gomez", "789456124", "2003-04-12", "F", "RU002", "2022-03-15", 3),
    Estudiante("7891234", "Luis", "Felipez", "789456125", "1995-09-10", "M", "RU003", "2020-01-01", 8),
]

docentes = [
    Docente("9789644", "Carlos", "Lopez", "789456999", "1975-03-01", "M", "NIT001", "Ingeniero", "Sistemas"),
    Docente("1257895", "Lucia", "Perez", "789456998", "1980-11-11", "F", "NIT002", "Arquitecta", "Diseño"),
    Docente("9972598", "Marco", "Felipez", "789456997", "1985-06-06", "M", "NIT003", "Ingeniero", "Civil")
]

Estudiante.estudiantes_mayores_de(estudiantes, 25)

# Mostrar docente más viejo, masculino e ingeniero
print("\n---- Docente masculino, Ingeniero y más viejo ----")
ingenieros_masculinos = [d for d in docentes if d.get_profesion() == "Ingeniero" and d.get_sexo() == "M"]
if ingenieros_masculinos:
    mayor = max(ingenieros_masculinos, key=lambda d: d.calcular_edad())
    mayor.mostrar()

# Mostrar personas con el mismo apellido
Docente.persona_con_el_mismo_apellido(estudiantes, docentes)

