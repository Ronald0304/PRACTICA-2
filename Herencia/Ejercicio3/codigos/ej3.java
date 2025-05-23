//3. Definir las clases:  Persona <ci, nombre, apellido, celular, fecha_Nac> Estudiante (heredado de persona) <ru, fecha_Ingreso, semestre> 
//Docente (heredado de persona) <nit, profesión, especialidad> 
//a) Diseñar el diagrama UML de las clases anteriores. 
//b) Implementa las clases con sus constructores, datos por defecto y mostrar. 
//c) Mostrar los estudiantes mayores de 25 años. 
//d) Mostrar al docente que tiene la profesión de “Ingeniero”, es del sexo masculino y es el mayor de todos. 
//e) Mostrar a los estudiantes y docentes que tienen el mismo apellido. 
import java.time.LocalDate;
import java.time.Period;
import java.time.format.DateTimeFormatter;
import java.util.*;

class Persona {
    protected String ci;
    protected String nombre;
    protected String apellido;
    protected String celular;
    protected String fechaNac;
    protected String sexo;

    public Persona(String ci, String nombre, String apellido, String celular, String fechaNac, String sexo) {
        this.ci = ci;
        this.nombre = nombre;
        this.apellido = apellido;
        this.celular = celular;
        this.fechaNac = fechaNac;
        this.sexo = sexo;
    }

    public int calcularEdad() {
        LocalDate nacimiento = LocalDate.parse(fechaNac);
        LocalDate hoy = LocalDate.now();
        return Period.between(nacimiento, hoy).getYears();
    }

    public void mostrar() {
        System.out.println("CI: " + ci + ", Nombre: " + nombre + " " + apellido +
                ", Celular: " + celular + ", Fecha Nac: " + fechaNac + ", Sexo: " + sexo);
    }

    public String getApellido() {
        return apellido;
    }

    public String getSexo() {
        return sexo;
    }
}

class Estudiante extends Persona {
    private String ru;
    private String fechaIngreso;
    private int semestre;

    public Estudiante(String ci, String nombre, String apellido, String celular, String fechaNac, String sexo,
                      String ru, String fechaIngreso, int semestre) {
        super(ci, nombre, apellido, celular, fechaNac, sexo);
        this.ru = ru;
        this.fechaIngreso = fechaIngreso;
        this.semestre = semestre;
    }

    @Override
    public void mostrar() {
        super.mostrar();
        System.out.println("RU: " + ru + ", Fecha Ingreso: " + fechaIngreso + ", Semestre: " + semestre);
    }

    public static void estudiantesMayoresDe(List<Estudiante> estudiantes, int edadLimite) {
        System.out.println("\n-- Estudiantes mayores de " + edadLimite + " años --");
        for (Estudiante e : estudiantes) {
            if (e.calcularEdad() > edadLimite) {
                e.mostrar();
                System.out.println("-----------------------------------");
            }
        }
    }

    public static void personaConElMismoApellido(List<Estudiante> estudiantes, List<Docente> docentes) {
        System.out.println("\n------ Personas con el mismo apellido --------");

        Set<String> apellidosEstudiantes = new HashSet<>();
        Set<String> apellidosDocentes = new HashSet<>();

        for (Estudiante e : estudiantes) {
            apellidosEstudiantes.add(e.getApellido());
        }
        for (Docente d : docentes) {
            apellidosDocentes.add(d.getApellido());
        }

        apellidosEstudiantes.retainAll(apellidosDocentes);

        for (String apellido : apellidosEstudiantes) {
            System.out.println("\nApellido en común: " + apellido);
            System.out.println("Estudiantes:");
            for (Estudiante e : estudiantes) {
                if (e.getApellido().equals(apellido)) {
                    e.mostrar();
                }
            }
            System.out.println("Docentes:");
            for (Docente d : docentes) {
                if (d.getApellido().equals(apellido)) {
                    d.mostrar();
                }
            }
        }
    }
}

class Docente extends Persona {
    private String nit;
    private String profesion;
    private String especialidad;

    public Docente(String ci, String nombre, String apellido, String celular, String fechaNac, String sexo,
                   String nit, String profesion, String especialidad) {
        super(ci, nombre, apellido, celular, fechaNac, sexo);
        this.nit = nit;
        this.profesion = profesion;
        this.especialidad = especialidad;
    }

    public String getProfesion() {
        return profesion;
    }

    @Override
    public void mostrar() {
        super.mostrar();
        System.out.println("NIT: " + nit + ", Profesión: " + profesion + ", Especialidad: " + especialidad);
    }

    public static void personaConElMismoApellido(List<Estudiante> estudiantes, List<Docente> docentes) {
        Estudiante.personaConElMismoApellido(estudiantes, docentes);
    }
}

public class Main {
    public static void main(String[] args) {
        List<Estudiante> estudiantes = new ArrayList<>();
        estudiantes.add(new Estudiante("1234567", "Juan", "Perez", "789456123", "2000-05-20", "M", "RU001", "2021-02-10", 6));
        estudiantes.add(new Estudiante("4567891", "Ana", "Gomez", "789456124", "2003-04-12", "F", "RU002", "2022-03-15", 3));
        estudiantes.add(new Estudiante("7891234", "Luis", "Felipez", "789456125", "1995-09-10", "M", "RU003", "2020-01-01", 8));

        List<Docente> docentes = new ArrayList<>();
        docentes.add(new Docente("9789644", "Carlos", "Lopez", "789456999", "1975-03-01", "M", "NIT001", "Ingeniero", "Sistemas"));
        docentes.add(new Docente("1257895", "Lucia", "Perez", "789456998", "1980-11-11", "F", "NIT002", "Arquitecta", "Diseño"));
        docentes.add(new Docente("9972598", "Marco", "Felipez", "789456997", "1985-06-06", "M", "NIT003", "Ingeniero", "Civil"));

        // Mostrar estudiantes mayores de 25 años
        Estudiante.estudiantesMayoresDe(estudiantes, 25);

        // Docente masculino ingeniero más viejo
        System.out.println("\n---- Docente masculino, Ingeniero y más viejo ----");
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
        Docente.personaConElMismoApellido(estudiantes, docentes);
    }
}

