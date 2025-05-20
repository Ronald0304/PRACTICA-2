#1. Sean las siguientes clases: 
#Habitación<nombre, tamaño (en metros cuadrados) 
#Métodos: mostrar_info() (muestra el nombre y tamaño de la habitación) 
#Casa<dirección, habitaciones (lista de objetos de tipo Habitación) 
#Métodos: agregar_habitacion(habitacion), mostrar_casa() (muestra la 
#dirección y la información de todas las habitaciones) 
#a) Implementa las clases con sus constructores, getters y setters. 
#b) Crea una casa y agrega varias habitaciones. 
#c) Muestra la información de la casa y sus habitaciones.
class Habitacion:
    def __init__(self,nombre,tamaño):
        self.__nombre = nombre
        self.__tamaño = tamaño
        
    def __str__(self):
        return f"Nombre de la Habitacion: {self.__nombre}, Tamaño: {self.__tamaño} m^2"
    
    def get_nombre(self):
        return self.nombre
    
    def get_tamaño(self):
        return self.tamaño
    
    def set_nombre(self,nombre):
        self.__nombre = nombre
        
    def set_tamaño(self,tamaño):
        self.__tamaño = tamaño
        
class Casa:
    def __init__(self,direccion):
        self.__direccion = direccion
        self.__nroHabitaciones = 0
        self.__habitaciones = []
        
    def agregar_habitaciones(self,nombre_habitacion,tamaño_habitacion):
        nueva_habitacion = Habitacion(nombre_habitacion,tamaño_habitacion)
        self.__habitaciones.append(nueva_habitacion)
        self.__nroHabitaciones = self.__nroHabitaciones+1
        
    def __str__(self):
        cad = ( f"Direccion de la Casa: {self.__direccion}\n")    
        for i in range(self.__nroHabitaciones):
            cad = cad+ " -" + (self.__habitaciones[i].__str__()) +"\n"
        return (cad)
        
    def get_direccion(self):
        return self.__direccion
    
    def get_habitaciones(self):
        return self.__habitaciones
    
    def set_habitaciones(self,habitaciones):
        self.__habitaciones = habitaciones
    
    def set_direccion(self,direccion):
        self.__direccion = direccion
class main():
    c1 = Casa("Avenida los Alamos 333")
    
    c1.agregar_habitaciones("Sala",25)
    c1.agregar_habitaciones("Cocina",35)
    c1.agregar_habitaciones("Dormitorio1",20)
    c1.agregar_habitaciones("Taller",25)
    c1.agregar_habitaciones("Dormitorio2",35)
    
    print(c1)
