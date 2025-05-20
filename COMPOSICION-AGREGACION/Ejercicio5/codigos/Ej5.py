#5. Desarrolla un POO para un equipo de fútbol y sus jugadores. El equipo está compuesto por jugadores, y si el equipo se destruye, los jugadores también se destruyen. Además, los jugadores pueden ser de diferentes tipos (portero, 
#defensa, mediocampista, delantero). Clase Padre: Jugador<nombre, número, posición> Métodos: mostrar_info() (muestra el nombre, número y posición del jugador) 
#Clases Derivadas: Portero, Defensa, Mediocampista, Delantero (heredan de Jugador) 
#Atributos adicionales: habilidad_especial (ej: "Atajadas", "Marcaje", "Pases", "Goles") 
#Clase: Equipo<nombre, jugadores (lista de objetos de tipo Jugador)> Métodos: agregar_jugador(jugador), mostrar_equipo() (muestra el nombre del equipo y la información de todos los jugadores) 
#a) Implementa las clases con sus constructores, getters y setters. 
#b) Crea un equipo y agrega varios jugadores de diferentes tipos. 
#c) Muestra la información del equipo y sus jugadores.
class Jugador:
    def __init__(self, nombre, numero, posicion, habilidad_especial):
        self.__nombre = nombre
        self.__numero = numero
        self.__posicion = posicion
        self.__habilidad_especial = habilidad_especial

    def get_nombre(self):
        return self.__nombre

    def get_numero(self):
        return self.__numero

    def get_posicion(self):
        return self.__posicion

    def get_habilidad_especial(self):
        return self.__habilidad_especial

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_numero(self, numero):
        self.__numero = numero

    def set_posicion(self, posicion):
        self.__posicion = posicion

    def set_habilidad_especial(self, habilidad):
        self.__habilidad_especial = habilidad

    def mostrar_info(self):
        return f"{self.__posicion}: {self.__nombre} (#{self.__numero}) - Habilidad: {self.__habilidad_especial}"

class Portero(Jugador):
    def __init__(self, nombre, numero):
        super().__init__(nombre, numero, "Portero", "Atajadas")

class Defensa(Jugador):
    def __init__(self, nombre, numero):
        super().__init__(nombre, numero, "Defensa", "Marcaje")

class Mediocampista(Jugador):
    def __init__(self, nombre, numero):
        super().__init__(nombre, numero, "Mediocampista", "Pases")

class Delantero(Jugador):
    def __init__(self, nombre, numero):
        super().__init__(nombre, numero, "Delantero", "Goles")

class Equipo:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__jugadores = []

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_jugadores(self):
        return self.__jugadores

    def agregar_jugador(self, jugador):
        if isinstance(jugador, Jugador):
            self.__jugadores.append(jugador)
        else:
            print("Solo se pueden agregar objetos de tipo Jugador.")

    def mostrar_equipo(self):
        print(f"Equipo: {self.__nombre}")
        print("Jugadores:")
        for jugador in self.__jugadores:
            print("  " + jugador.mostrar_info())

def main():
    equipo = Equipo("Real Madrid")

    equipo.agregar_jugador(Portero("Carlos", 1))
    equipo.agregar_jugador(Defensa("Luis", 3))
    equipo.agregar_jugador(Mediocampista("Andrés", 8))
    equipo.agregar_jugador(Delantero("Mbape", 10))

    equipo.mostrar_equipo()

main()
