class Vehiculo:
    def __init__(self,marca,modelo,año,precioBase):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__precioBase = precioBase
        
    def __str__(self):
        mostrar = f"Marca: {self.__marca} | Modelo: {self.__modelo} | Año: {self.__año} | Precio: {self.__ precioBase} Bs"
        return mostrar
    
    def getmarca(self):
        return self.marca
    
    def setmarca(self,marca):
        self.marca = marca
        
    def getmodelo(self):
        return self.modelo
    
    def setmodelo(self,modelo):
        self.modelo = modelo

    def getaño(self):
        return self.año
    
    def setaño(self,año):
        self.año = año
        
    def getprecioBase(self):
        return self.precioBase
    
    def setprecioBase(self,precioBase):
        self.precioBase = precioBase
    
class Coche(Vehiculo):
    def __init__(self,marca,modelo,año,precioBase,nroPuertas,tipoCombustible):
        super().__init__(marca,modelo,año,precioBase)
        self.nroPuertas = nroPuertas
        self.tipoCombustible = tipoCombustible
        
    def __str__(self):
        mostrar = super(). __str__()
        return (f"{mostrar}\nNumero de puertas: {self.nroPuertas} | Tipo de Combustible: {self.tipoCombustible}")
    
    def getnroPuertas(self):
        return self.nroPuertas
    
class Moto(Vehiculo):
    def __init__(self,marca,modelo,año,precioBase,cilindrada,tipoMotor):
        super().__init__(marca,modelo,año,precioBase)
        self.cilindrada = cilindrada
        self.tipoMotor = tipoMotor
        
    def __str__(self):
        mostrar = super(). __str__()
        return (f"{mostrar}\nCilindrada: {self.cilindrada} | Tipo de Motor: {self.tipoMotor}")
        

v1 = Coche("Toyota","Hilux",2020,35000,4,"Gasolina")
v2 = Coche("Honda","City",2015,15000,6,"Electrico")
v3 = Coche("Toyota","Hilux",2025,35000,4,"Gas")
v4 = Coche("Honda","City",2015,15000,2,"Gasolina")
m1 = Moto("Honda","LP258",2021,3000 ,25,"gasolina")
m2 = Moto("Honda","SP298",2018,3050 ,25,"gasolina")
print(v1)
print("------------------------------------------")
print(v2)
print("------------------------------------------")
print(v3)
print("------------------------------------------")
print(v4)
print("------------------------------------------")
print(m1)
print("------------------------------------------")
print(m2)

print("\n=== Coches con más de 4 puertas ===")
coches = [v1, v2, v3]
for coche in coches:
    if coche.getnroPuertas() > 4:
        print(coche)
        print("------------")
        
print("\n=== Vehículos de la gestión 2025 ===")
vehiculos = coches + [m1, m2]
for vehiculo in vehiculos:
    if vehiculo.getaño() == 2025:
        print(vehiculo)
        print("------------")
