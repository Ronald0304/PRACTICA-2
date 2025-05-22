//3. Crea un POO de clases para modelar un avión y sus partes. El avión está compuesto por partes como el motor, las alas y el tren de aterrizaje. Si el avión 
//se destruye, las partes también se destruyen. Parte<nombre, peso (en kg) Métodos: mostrar_info() (muestra el nombre y el peso de la parte) 
//Avión<modelo, fabricante, partes (lista de objetos de tipo Parte) Métodos: agregar_parte(parte), mostrar_avión() (muestra el modelo, fabricante y la información de todas las partes) 
//a) Implementa las clases con sus constructores, getters y setters. 
//b) Crea un avión y agrega varias partes. 
//c) Muestra la información del avión y sus partes. 
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        Avion avion1 = new Avion("Boeing 747", "Boeing");

        avion1.agregarParte("Motor izquierdo", 2500);
        avion1.agregarParte("Motor derecho", 2500);
        avion1.agregarParte("Ala izquierda", 1800);
        avion1.agregarParte("Ala derecha", 1800);
        avion1.agregarParte("Tren de aterrizaje", 900);

        avion1.mostrarAvion();
    }

    static class Parte {
        private String nombre;
        private double peso;

        public Parte(String nombre, double peso) {
            this.nombre = nombre;
            this.peso = peso;
        }

        public String getNombre() {
            return nombre;
        }

        public void setNombre(String nombre) {
            this.nombre = nombre;
        }

        public double getPeso() {
            return peso;
        }

        public void setPeso(double peso) {
            this.peso = peso;
        }

        public String mostrarInfo() {
            return "Parte: " + nombre + ", Peso: " + peso + " kg";
        }
    }

    static class Avion {
        private String modelo;
        private String fabricante;
        private ArrayList<Parte> partes;

        public Avion(String modelo, String fabricante) {
            this.modelo = modelo;
            this.fabricante = fabricante;
            this.partes = new ArrayList<>();
        }

        public String getModelo() {
            return modelo;
        }

        public void setModelo(String modelo) {
            this.modelo = modelo;
        }

        public String getFabricante() {
            return fabricante;
        }

        public void setFabricante(String fabricante) {
            this.fabricante = fabricante;
        }

        public ArrayList<Parte> getPartes() {
            return partes;
        }

        public void setPartes(ArrayList<Parte> partes) {
            this.partes = partes;
        }

        public void agregarParte(String nombreParte, double pesoParte) {
            Parte nuevaParte = new Parte(nombreParte, pesoParte);
            partes.add(nuevaParte);
        }

        public void mostrarAvion() {
            System.out.println("Modelo: " + modelo);
            System.out.println("Fabricante: " + fabricante);
            System.out.println("Partes del avión:");
            for (Parte p : partes) {
                System.out.println(" - " + p.mostrarInfo());
            }
        }
    }
}
