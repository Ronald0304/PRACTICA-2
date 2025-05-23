#5. Definir las siguientes clases: Empleado<nombre, apellido, salario_base, años_antigüedad Métodos: calcular_salario() (retorna el salario base más un bono 
#del 5% por cada año de antigüedad) Gerente (hereda de Empleado)< departamento, bono_gerencial> Métodos: calcular_salario() (debe sumar el bono gerencial al 
#salario calculado en la clase base) Desarrollador (hereda de Empleado) <lenguaje_programación, horas_extras> Métodos: calcular_salario() (debe sumar un monto adicional por horas extras al salario calculado en la clase base) 
#a) Implementa las clases con sus constructores, getters y setters. 
#b) Crea instancias de Gerente y Desarrollador y muestra su salario calculado. 
#c) Muestra todos los gerentes que tienen un bono gerencial mayor a 1000. 
#d) Muestra todos los desarrolladores que trabajan más de 10 horas extras.
class Empleado:
    def __init__(self, nombre, apellido, salario_base, años_antiguedad):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__salario_base = salario_base
        self.__años_antiguedad = años_antiguedad

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_salario_base(self):
        return self.__salario_base

    def get_años_antiguedad(self):
        return self.__años_antiguedad

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def set_salario_base(self, salario):
        self.__salario_base = salario

    def set_años_antiguedad(self, años):
        self.__años_antiguedad = años

    def calcular_salario(self):
        bono = 0.05 * self.__salario_base * self.__años_antiguedad
        return self.__salario_base + bono

    def mostrar(self):
        print(f"{self.__nombre} {self.__apellido} - Salario Base: {self.__salario_base} - Años Antigüedad: {self.__años_antiguedad}")

class Gerente(Empleado):
    def __init__(self, nombre, apellido, salario_base, años_antiguedad, departamento, bono_gerencial):
        super().__init__(nombre, apellido, salario_base, años_antiguedad)
        self.__departamento = departamento
        self.__bono_gerencial = bono_gerencial

    def get_departamento(self):
        return self.__departamento

    def get_bono_gerencial(self):
        return self.__bono_gerencial

    def set_departamento(self, departamento):
        self.__departamento = departamento

    def set_bono_gerencial(self, bono):
        self.__bono_gerencial = bono

    def calcular_salario(self):
        return super().calcular_salario() + self.__bono_gerencial

    def mostrar(self):
        super().mostrar()
        print(f"Departamento: {self.__departamento} - Bono Gerencial: {self.__bono_gerencial} - Salario Total: {self.calcular_salario()}")

class Desarrollador(Empleado):
    def __init__(self, nombre, apellido, salario_base, años_antiguedad, lenguaje_programacion, horas_extras):
        super().__init__(nombre, apellido, salario_base, años_antiguedad)
        self.__lenguaje_programacion = lenguaje_programacion
        self.__horas_extras = horas_extras

    def get_lenguaje_programacion(self):
        return self.__lenguaje_programacion

    def get_horas_extras(self):
        return self.__horas_extras

    def set_lenguaje_programacion(self, lenguaje):
        self.__lenguaje_programacion = lenguaje

    def set_horas_extras(self, horas):
        self.__horas_extras = horas

    def calcular_salario(self):
        pago_extra = 50 * self.__horas_extras
        return super().calcular_salario() + pago_extra

    def mostrar(self):
        super().mostrar()
        print(f"Lenguaje: {self.__lenguaje_programacion} - Horas Extras: {self.__horas_extras} - Salario Total: {self.calcular_salario()}")

gerentes = [
    Gerente("Laura", "Fernandez", 5000, 10, "Marketing", 1500),
    Gerente("Carlos", "Ramirez", 4500, 5, "Finanzas", 800),
    Gerente("Maria", "Lopez", 6000, 15, "TI", 1200)
]

desarrolladores = [
    Desarrollador("Ana", "Gomez", 4000, 3, "Python", 12),
    Desarrollador("Luis", "Mendoza", 4200, 4, "Java", 8),
    Desarrollador("Diego", "Martinez", 3900, 6, "JavaScript", 14)
]

# (b) Mostrar salario calculado
print("----- Salario Calculado de Gerentes -----")
for g in gerentes:
    g.mostrar()
    print()

print("----- Salario Calculado de Desarrolladores -----")
for d in desarrolladores:
    d.mostrar()
    print()

# (c) Gerentes con bono > 1000
print("------Gerentes con bono gerencial > 1000 ------")
for g in gerentes:
    if g.get_bono_gerencial() > 1000:
        g.mostrar()
        print()

# (d) Desarrolladores con más de 10 horas extras
print("------ Desarrolladores con más de 10 horas extras ------")
for d in desarrolladores:
    if d.get_horas_extras() > 10:
        d.mostrar()
        print()
