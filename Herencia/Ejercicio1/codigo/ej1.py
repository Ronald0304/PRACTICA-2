#1. Modelar diferentes tipos de vehículos. Las clases deben tener las siguientes características: 
#Vehículo<marca, modelo, año, precio_base> Métodos: mostrar_info() muestra la información básica del vehículo Coche (hereda de Vehículo)< num_puertas, tipo_combustible> 
#Métodos: mostrar_info() debe mostrar la información básica más los atributos adicionales Moto (hereda de Vehículo)< cilindrada, tipo_motor> 
#Métodos: mostrar_info() debe mostrar la información básica más los atributos adicionales 
#a) Implementa las clases con sus constructores, getters y setters.  
#b) Crea instancias de Coche y Moto y muestra su información usando el método mostrar_info(). 
#c) Muestra todos los coches que tienen más de 4 puertas. 
#d) Mostrar los coches y motos actuales (gestión 2025) 
class Vehiculo:
    def __init__(self,marca,modelo,año,precioBase):
        self.__marca = marca 
        self.__modelo = modelo
        self.__año = año
        self.__precioBase = precioBase
        
    def __str__(self):
        return f"Marca: {self.__marca}| Modelo: {self.__modelo}| Año :{self.__año} | Precio Base : {self.__precioBase} Bs "
    
    def getMarca(self):
        return self.__marca
    
    def setMarca(self,marca):
        self.__marca = marca
        
    def getModelo(self):
        return self.__modelo
    
    def setModelo(self,modelo):
        self.__modelo = modelo
        
    def getAño(self):
        return self.__año
    
    def setAño(self,año):
        self.__año = año
        
    def getPrecioBase(self):
        return self.__precioBase
    
    def setPrecioBase(self,precioBase):
        self.__precioBase = precioBase
        
class Coche(Vehiculo):
    def __init__(self,marca,modelo,año,precioBase,nroPuertas,tipoCombustible):
        super().__init__(marca,modelo,año,precioBase)
        self.__nroPuertas = nroPuertas
        self.__tipoCombustible = tipoCombustible
        
    def __str__(self):
        cad = super().__str__()
        cad = cad + f"| Nº Puertas: {self.__nroPuertas}| Tipo de Combustible : {self.__tipoCombustible}"
        return (cad)
    
    def getNroPuertas(self):
        return self.__nroPuertas
    
    def setNroPuertas(self,nroPuertas):
        self.__nroPuertas = nroPuertas
        
    def getTipoCombustible(self):
        return self.__tipoCombustible
    
    def setTipoCombustible(self,tipoCombustible):
        self.__tipoCombustible = tipoCombustible
        
        
class Moto(Vehiculo):
    def __init__(self,marca,modelo,año,precioBase,cilindrada,tipoMotor):
        super().__init__(marca,modelo,año,precioBase)
        self.__cilindrada = cilindrada
        self.tipoMotor = tipoMotor
        
    def __str__(self):
        cad =super().__str__()
        cad = cad + f"| Cilindrada: {self.__cilindrada} | Tipo de Motor: {self.tipoMotor}"
        return (cad)
    
    def getCilindrada (self):
        return self.__cilindrada
    
    def setCilindrada(self,cilindrada):
        self.__cilindrada = cilindrada
        
    def getTipoMotor(self):
        return self.__tipoMotor
    
    def setTipoMotor(self,tipoMotor):
        self.__tipoMotor = tipoMotor
        
    
class main():
    a1 = Coche("Toyota","4x4",2020,35000,4,"Gasolina")
    a2 = Coche("Toyota","Caldina",2021,29000,4,"gasolina")
    a3 = Coche("BMW","GTX-205",2025,57000,2,"Gas")
    a4 = Coche("Suzuki","J-569K",2024,3000,6,"Gasolina")
    m1 = Moto("Yamaha","Tracer 7 / GT",2025, 15000,"689 cc","2 cil.en linea")
    m2 = Moto("Harley","Davidson Fat Boy",2025,70000,"1.923 cc","2 cil, en V")
    m3 = Moto("Rieju","Xplora 557",2024,15000,"554 cc","2.cil en linea")
    print("---------Autos: --------")
    print(a1)
    print(a2)
    print(a3)
    print(a4)
    print("---------Motos: ---------")
    print(m1)
    print(m2)
    print(m3)
    #Mostrar todos los coches con mas de 4 puertas
    print("------Coches con mas de 4 puertas------")
    coches = [a1,a2,a3,a4]
    for coche in coches:
        if coche.getNroPuertas() > 4:
            print(coche) 
    #mostrar coches y motos actuales 2025
    print("----Motos y Coches del 2025----")
    vehiculos = [a1,a2,a3,a4,m1,m2,m3]
    for i in vehiculos:
        if i.getAño() == 2025:
            print(i)
            
