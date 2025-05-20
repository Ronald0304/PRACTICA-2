#9. Crea un POO para un carrito de compras y sus productos. El carrito contiene productos, pero los productos pueden existir independientemente del carrito. 
#Además, el carrito no puede contener más de 10 productos. Producto<nombre, precio> 
#Métodos: mostrar_info() (muestra el nombre y el precio del producto) CarritoCompras<productos (lista de objetos de tipo Producto)> 
#Métodos: agregar_producto(producto), mostrar_carrito() (muestra la información de todos los productos en el carrito) 
#a) Implementa las clases con sus constructores, getters y setters. 
#b) Crea un carrito de compras y agrega varios productos, validando que no se exceda el límite de 10 productos. 
#c) Muestra la información del carrito y sus productos. 
class Producto:
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def set_precio(self, nuevo_precio):
        self.__precio = nuevo_precio

    def mostrar_info(self):
        return f"Producto: {self.__nombre}, Precio: Bs {self.__precio:.2f}"

class CarritoCompras:
    def __init__(self):
        self.__productos = []

    def agregar_producto(self, producto):
        if len(self.__productos) < 10:
            self.__productos.append(producto)
            print(f" Producto '{producto.get_nombre()}' agregado.")
        else:
            print(" Límite de 10 productos alcanzado.")

    def agregar_varios_productos(self, lista_productos):
        for producto in lista_productos:
            self.agregar_producto(producto)

    def mostrar_carrito(self):
        if not self.__productos:
            print(" El carrito está vacío.")
        else:
            print("\n Productos en el carrito:")
            for i, producto in enumerate(self.__productos, start=1):
                print(f"{i}. {producto.mostrar_info()}")
            total = sum(p.get_precio() for p in self.__productos)
            print(f"\n Total: Bs {total:.2f}")

def main():
    productos = [
        Producto("Laptop", 12000.99),
        Producto("Mouse", 75.50),
        Producto("Teclado", 150.75),
        Producto("Monitor", 1000.40),
        Producto("USB", 15.00),
        Producto("Audífonos", 65.00),
        Producto("Mochila", 40.00),
        Producto("Tablet", 2500.00),
        Producto("Cargador", 50.00),
        Producto("Celular", 1200.00),
        Producto("Silla", 150.00),  # número 11 (no se agregará)
    ]

    carrito = CarritoCompras()
    carrito.agregar_varios_productos(productos)

    carrito.mostrar_carrito()

main()
