//1. Sean las siguientes clases: Habitación<nombre, tamaño (en metros cuadrados) Métodos: mostrar_info() (muestra el nombre y tamaño de la habitación) 
//Casa<dirección, habitaciones (lista de objetos de tipo Habitación) Métodos: agregar_habitacion(habitacion), mostrar_casa() (muestra la dirección y la información de todas las habitaciones) 
//a) Implementa las clases con sus constructores, getters y setters. 
//b) Crea una casa y agrega varias habitaciones. 
//c) Muestra la información de la casa y sus habitaciones. 
import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        Casa c1 = new Casa("Avenida los Alamos 333");

        c1.agregarHabitacion("Sala", 25);
        c1.agregarHabitacion("Cocina", 35);
        c1.agregarHabitacion("Dormitorio1", 20);
        c1.agregarHabitacion("Taller", 25);
        c1.agregarHabitacion("Dormitorio2", 35);

        System.out.println(c1);
    }

    static class Habitacion {
        private String nombre;
        private double tamaño;

        public Habitacion(String nombre, double tamaño) {
            this.nombre = nombre;
            this.tamaño = tamaño;
        }

        public String getNombre() {
            return nombre;
        }

        public void setNombre(String nombre) {
            this.nombre = nombre;
        }

        public double getTamaño() {
            return tamaño;
        }

        public void setTamaño(double tamaño) {
            this.tamaño = tamaño;
        }

        @Override
        public String toString() {
            return "Nombre de la Habitación: " + nombre + ", Tamaño: " + tamaño + " m^2";
        }
    }

    static class Casa {
        private String direccion;
        private ArrayList<Habitacion> habitaciones;

        public Casa(String direccion) {
            this.direccion = direccion;
            this.habitaciones = new ArrayList<>();
        }

        public String getDireccion() {
            return direccion;
        }

        public void setDireccion(String direccion) {
            this.direccion = direccion;
        }

        public ArrayList<Habitacion> getHabitaciones() {
            return habitaciones;
        }

        public void setHabitaciones(ArrayList<Habitacion> habitaciones) {
            this.habitaciones = habitaciones;
        }

        public void agregarHabitacion(String nombre, double tamaño) {
            Habitacion h = new Habitacion(nombre, tamaño);
            habitaciones.add(h);
        }

        @Override
        public String toString() {
            StringBuilder sb = new StringBuilder();
            sb.append("Dirección de la Casa: ").append(direccion).append("\n");
            for (Habitacion h : habitaciones) {
                sb.append(" - ").append(h.toString()).append("\n");
            }
            return sb.toString();
        }
    }
}
