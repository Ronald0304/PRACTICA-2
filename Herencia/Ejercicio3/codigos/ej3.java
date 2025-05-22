//3. Definir las clases:  Persona <ci, nombre, apellido, celular, fecha_Nac> Estudiante (heredado de persona) <ru, fecha_Ingreso, semestre> 
//Docente (heredado de persona) <nit, profesión, especialidad> 
//a) Diseñar el diagrama UML de las clases anteriores. 
//b) Implementa las clases con sus constructores, datos por defecto y mostrar. 
//c) Mostrar los estudiantes mayores de 25 años. 
//d) Mostrar al docente que tiene la profesión de “Ingeniero”, es del sexo masculino y es el mayor de todos. 
//e) Mostrar a los estudiantes y docentes que tienen el mismo apellido. 
import java.time.LocalDate;
import java.time.Period;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        ArrayList<Estudiante> estudiantes = new ArrayList<>();
        estudiantes.add(new Estudiante("1234567", "Juan", "Perez", "789456123", "2000-05-20", "M", "RU001", "2021-02-10", 6));
        estudiantes.add(new Estudiante("2233445", "Ana", "Gomez", "789456124", "2003-04-12", "F", "RU002", "2022-03-15", 3));
        estudiantes.add(new Estudiante("7891234", "Luis", "Felipez", "789456125", "1995-09-10", "M", "RU003", "2020-01-01", 8));

        ArrayList<Docente> docentes = new ArrayList<>();
        docentes.add(new Docente("9789644", "Carlos", "Lopez", "789456999", "1975-03-01", "M", "NIT001", "Ingeniero", "Sistemas"));
        docentes.add(new Docente("1257895", "Lucia", "Perez", "789456998", "1980-11-11", "F", "NIT002", "Arquitecta", "Diseño"));
        docentes.add(new Docente("9972598", "Marco", "Felipez", "789456997", "1985-06-06", "M", "NIT003", "Ingeniero", "Civil"));
        docentes.add(new Docente("1598753","Jhony","Felipez","68521476","1980-09-05","F","NIT004","Programacion", "Informatica"));

        // c) Estudiantes mayores de 25 años
        System.out.println("\n--- Estudiantes mayores de 25 años ---");
        for (Estudiante e : estudiantes) {
            if (e.calcularEdad() > 25) {
                e.mostrar();
                System.out.println("--------------------");
            }
        }

        // d) Docente Ingeniero, Masculino, más viejo
        System.out.println("\n--- Docente Ingeniero masculino más viejo ---");
        Docente mayor = null;
        for (Docente d : docentes) {
            if (d.getProfesion().equals("Ingeniero") && d.getSexo().equals("M")) {
                if (mayor == null || d.calcularEdad() > mayor.calcularEdad()) {
                    mayor = d;
                }
            }
        }
        if (mayor != null) {
            mayor.mostrar();
        }

        // e) Estudiantes y docentes con el mismo apellido
        System.out.println("\n--- Personas con apellidos comunes ---");
        for (Estudiante e : estudiantes) {
            for (Docente d : docentes) {
                if (e.getApellido().equals(d.getApellido())) {
                    System.out.println("\nApellido en común: " + e.getApellido());
                    System.out.println("Estudiante:");
                    e.mostrar();
                    System.out.println("Docente:");
                    d.mostrar();
                }
            }
        }
    }
}


class Persona {
    private String ci, nombre, apellido, celular, sexo;
    private LocalDate fechaNac;

    public Persona(String ci, String nombre, String apellido, String celular, String fechaNac, String sexo) {
        this.ci = ci;
        this.nombre = nombre;
        this.apellido = apellido;
        this.celular = celular;
        this.fechaNac = LocalDate.parse(fechaNac);
        this.sexo = sexo;
    }

    public int calcularEdad() {
        return Period.between(this.fechaNac, LocalDate.now()).getYears();
    }

    public void mostrar() {
        System.out.println("CI: " + ci + ", Nombre: " + nombre + " " + apellido +
                ", Celular: " + celular + ", Fecha Nac: " + fechaNac + ", Sexo: " + sexo);
    }

    public String getApellido() { return apellido; }
    public String getSexo() { return sexo; }
    public LocalDate getFechaNac() { return fechaNac; }
}

class Estudiante extends Persona {
    private String ru;
    private LocalDate fechaIngreso;
    private int semestre;

    public Estudiante(String ci, String nombre, String apellido, String celular,
                      String fechaNac, String sexo, String ru, String fechaIngreso, int semestre) {
        super(ci, nombre, apellido, celular, fechaNac, sexo);
        this.ru = ru;
        this.fechaIngreso = LocalDate.parse(fechaIngreso);
        this.semestre = semestre;
    }

    @Override
    public void mostrar() {
        super.mostrar();
        System.out.println("RU: " + ru + ", Fecha Ingreso: " + fechaIngreso + ", Semestre: " + semestre);
    }
}

class Docente extends Persona {
    private String nit, profesion, especialidad;

    public Docente(String ci, String nombre, String apellido, String celular,
                   String fechaNac, String sexo, String nit, String profesion, String especialidad) {
        super(ci, nombre, apellido, celular, fechaNac, sexo);
        this.nit = nit;
        this.profesion = profesion;
        this.especialidad = especialidad;
    }

    public String getProfesion() { return profesion; }

    @Override
    public void mostrar() {
        super.mostrar();
        System.out.println("NIT: " + nit + ", Profesión: " + profesion + ", Especialidad: " + especialidad);
    }
}
