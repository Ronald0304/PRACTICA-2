//1. Modelar diferentes tipos de vehículos. Las clases deben tener las siguientes características: Vehículo<marca, modelo, año, precio_base> 
//Métodos: mostrar_info() muestra la información básica del vehículo Coche (hereda de Vehículo)< num_puertas, tipo_combustible> Métodos: mostrar_info() debe mostrar la información básica más los 
//atributos adicionales Moto (hereda de Vehículo)< cilindrada, tipo_motor> Métodos: mostrar_info() debe mostrar la información básica más los 
//atributos adicionales 
//a) Implementa las clases con sus constructores, getters y setters.  
//b) Crea instancias de Coche y Moto y muestra su información usando el método mostrar_info(). 
//c) Muestra todos los coches que tienen más de 4 puertas. 
//d) Mostrar los coches y motos actuales (gestión 2025)
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        Coche a1 = new Coche("Toyota", "4x4", 2020, 35000, 4, "Gasolina");
        Coche a2 = new Coche("Toyota", "Caldina", 2021, 29000, 4, "Gasolina");
        Coche a3 = new Coche("BMW", "GTX-205", 2025, 57000, 2, "Gas");
        Coche a4 = new Coche("Suzuki", "J-569K", 2024, 3000, 6, "Gasolina");

        Moto m1 = new Moto("Yamaha", "Tracer 7 / GT", 2025, 15000, "689 cc", "2 cil. en línea");
        Moto m2 = new Moto("Harley", "Davidson Fat Boy", 2025, 70000, "1.923 cc", "2 cil. en V");
        Moto m3 = new Moto("Rieju", "Xplora 557", 2024, 15000, "554 cc", "2 cil. en línea");

        System.out.println("---------Autos: --------");
        System.out.println(a1);
        System.out.println(a2);
        System.out.println(a3);
        System.out.println(a4);

        System.out.println("---------Motos: ---------");
        System.out.println(m1);
        System.out.println(m2);
        System.out.println(m3);

        System.out.println("------Coches con más de 4 puertas------");
        ArrayList<Coche> coches = new ArrayList<>();
        coches.add(a1);
        coches.add(a2);
        coches.add(a3);
        coches.add(a4);
        for (Coche c : coches) {
            if (c.getNroPuertas() > 4) {
                System.out.println(c);
            }
        }

        System.out.println("----Motos y Coches del 2025----");
        ArrayList<Vehiculo> vehiculos = new ArrayList<>();
        vehiculos.add(a1);
        vehiculos.add(a2);
        vehiculos.add(a3);
        vehiculos.add(a4);
        vehiculos.add(m1);
        vehiculos.add(m2);
        vehiculos.add(m3);
        for (Vehiculo v : vehiculos) {
            if (v.getAnio() == 2025) {
                System.out.println(v);
            }
        }
    }
}

class Vehiculo {
    private String marca;
    private String modelo;
    private int anio;
    private double precioBase;

    public Vehiculo(String marca, String modelo, int anio, double precioBase) {
        this.marca = marca;
        this.modelo = modelo;
        this.anio = anio;
        this.precioBase = precioBase;
    }

    public String getMarca() {
        return marca;
    }
    public void setMarca(String marca) {
        this.marca = marca;
    }
    public String getModelo() {
        return modelo;
    }
    public void setModelo(String modelo) {
        this.modelo = modelo;
    }
    public int getAnio() {
        return anio;
    }
    public void setAnio(int anio) {
        this.anio = anio;
    }
    public double getPrecioBase() {
        return precioBase;
    }
    public void setPrecioBase(double precioBase) {
        this.precioBase = precioBase;
    }

    @Override
    public String toString() {
        return "Marca: " + marca + " | Modelo: " + modelo + " | Año: " + anio + " | Precio Base: " + precioBase + " Bs";
    }
}

class Coche extends Vehiculo {
    private int nroPuertas;
    private String tipoCombustible;

    public Coche(String marca, String modelo, int anio, double precioBase, int nroPuertas, String tipoCombustible) {
        super(marca, modelo, anio, precioBase);
        this.nroPuertas = nroPuertas;
        this.tipoCombustible = tipoCombustible;
    }

    public int getNroPuertas() {
        return nroPuertas;
    }

    public void setNroPuertas(int nroPuertas) {
        this.nroPuertas = nroPuertas;
    }

    public String getTipoCombustible() {
        return tipoCombustible;
    }

    public void setTipoCombustible(String tipoCombustible) {
        this.tipoCombustible = tipoCombustible;
    }

    @Override
    public String toString() {
        return super.toString() + " | Nº Puertas: " + nroPuertas + " | Tipo de Combustible: " + tipoCombustible;
    }
}

class Moto extends Vehiculo {
    private String cilindrada;
    private String tipoMotor;

    public Moto(String marca, String modelo, int anio, double precioBase, String cilindrada, String tipoMotor) {
        super(marca, modelo, anio, precioBase);
        this.cilindrada = cilindrada;
        this.tipoMotor = tipoMotor;
    }

    public String getCilindrada() {
        return cilindrada;
    }

    public void setCilindrada(String cilindrada) {
        this.cilindrada = cilindrada;
    }

    public String getTipoMotor() {
        return tipoMotor;
    }

    public void setTipoMotor(String tipoMotor) {
        this.tipoMotor = tipoMotor;
    }

    @Override
    public String toString() {
        return super.toString() + " | Cilindrada: " + cilindrada + " | Tipo de Motor: " + tipoMotor;
    }
}
