#3. Crea un POO de clases para modelar un avión y sus partes. El avión está compuesto por partes como el motor, las alas y el tren de aterrizaje. Si el avión 
#se destruye, las partes también se destruyen.  
#Parte<nombre, peso (en kg) Métodos: mostrar_info() (muestra el nombre y el peso de la parte) 
#Avión<modelo, fabricante, partes (lista de objetos de tipo Parte) Métodos: agregar_parte(parte), mostrar_avión() (muestra el modelo, fabricante 
#y la información de todas las partes) 
#a) Implementa las clases con sus constructores, getters y setters. 
#b) Crea un avión y agrega varias partes. 
#c) Muestra la información del avión y sus partes.
class Parte:
    def __init__(self, nombre, peso):
        self.__nombre = nombre
        self.__peso = peso

    def get_nombre(self):
        return self.__nombre

    def get_peso(self):
        return self.__peso

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_peso(self, peso):
        self.__peso = peso

    def mostrar_info(self):
        return f"Parte: {self.__nombre}, Peso: {self.__peso} kg"

class Avion:
    def __init__(self, modelo, fabricante):
        self.__modelo = modelo
        self.__fabricante = fabricante
        self.__partes = []  

    def get_modelo(self):
        return self.__modelo

    def get_fabricante(self):
        return self.__fabricante

    def get_partes(self):
        return self.__partes

    def set_modelo(self, modelo):
        self.__modelo = modelo

    def set_fabricante(self, fabricante):
        self.__fabricante = fabricante

    def agregar_parte(self, nombre_parte, peso_parte):
        nueva_parte = Parte(nombre_parte, peso_parte)
        self.__partes.append(nueva_parte)

    def mostrar_avion(self):
        print(f"Modelo: {self.__modelo}")
        print(f"Fabricante: {self.__fabricante}")
        print("Partes del avión:")
        for parte in self.__partes:
            print(" -", parte.mostrar_info())


avion1 = Avion("Boeing 747", "Boeing")

avion1.agregar_parte("Motor izquierdo", 2500)
avion1.agregar_parte("Motor derecho", 2500)
avion1.agregar_parte("Ala izquierda", 1800)
avion1.agregar_parte("Ala derecha", 1800)
avion1.agregar_parte("Tren de aterrizaje", 900)

avion1.mostrar_avion()
