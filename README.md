# Pa1_2025
Producto academico  1

classDiagram
    class Usuario {
        - nombre: String
        - email: String
        - telefono: String
        + Usuario(nombre: String, email: String, telefono: String)
        + mostrar_info(): String
    }

    class Paciente {
        - historia_medica: List<String>
        - citas: List<Cita>
        + Paciente(nombre: String, email: String, telefono: String)
        + mostrar_info(): String
        + agregar_historial(entrada: String)
        + reservar_cita(cita: Cita)
    }

    class Doctor {
        - especialidad: String
        - citas: List<Cita>
        + Doctor(nombre: String, email: String, telefono: String, especialidad: String)
        + mostrar_info(): String
        + agendar_cita(cita: Cita)
        + listar_citas(): List<String>
    }

    class Cita {
        - fecha: String
        - hora: String
        - estado: String
        - doctor: Doctor
        - paciente: Paciente
        - receta: Receta
        + Cita(fecha: String, hora: String, doctor: Doctor, paciente: Paciente)
        + obtener_detalles(): String
        + cancelar_cita()
        + agregar_receta(receta: Receta)
    }

    class Receta {
        - medicamentos: List<String>
        + Receta()
        + agregar_medicamento(medicamento: String)
        + mostrar_receta(): String
    }

    class Clinica {
        - nombre: String
        - doctores: List<Doctor>
        + Clinica(nombre: String)
        + agregar_doctor(doctor: Doctor)
        + listar_doctores(): List<String>
    }

    class SistemaGestorCitas {
        - citas: List<Cita>
        + SistemaGestorCitas()
        + agendar_cita(fecha: String, hora: String, doctor: Doctor, paciente: Paciente): Cita
        + cancelar_cita(cita: Cita)
        + listar_citas(): List<String>
    }

    %% Relaciones

    Usuario <|-- Paciente
    Usuario <|-- Doctor
    Paciente "1" o-- "*" Cita: reserva
    Doctor "1" o-- "*" Cita: atiende
    Cita *-- Receta: 0..1
    Doctor "1" o-- "*" Clinica: trabaja_en
    Clinica "1" o-- "*" Doctor: tiene
    SistemaGestorCitas "1" o-- "*" Cita: gestiona