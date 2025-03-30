# PRODUCTO ACADEMICO 1 
Sistema de Gestión de Citas Médicas
*Descripción
Este proyecto permite la administración de citas médicas en una clínica, gestionando pacientes, doctores, historiales médicos y recetas.

*conceptos aplicados 
- Encapsulamiento: Uso de getters y setters.
- Herencia: Paciente y Doctor heredan de Usuario.
- Polimorfismo: Métodos sobrescritos para mostrar información.
- Relaciones UML:

Composición: Cita contiene Receta.
Agregación: Doctor trabaja en Clínica.
Asociación: Cita vincula Paciente y Doctor.

Tecnologías usadas 
-Python (POO)
-Visual Studio Code
-Diagramas UML (Clases y Casos de Uso)
```mermaid
classDiagram
    %% Clase base Usuario con encapsulamiento y métodos de acceso
    class Usuario {
        - nombre: String
        - email: String
        - telefono: String
        + Usuario(nombre: String, email: String, telefono: String)
        + get_nombre(): String
        + set_nombre(nombre: String)
        + get_email(): String
        + set_email(email: String)
        + get_telefono(): String
        + set_telefono(telefono: String)
        + mostrar_info(): String
    }

    %% Paciente hereda de Usuario y tiene su propio historial y citas
    class Paciente {
        - historia_medica: List<String>
        - citas: List<Cita>
        + Paciente(nombre: String, email: String, telefono: String)
        + get_historia_medica(): List<String>
        + agregar_historial(entrada: String)
        + reservar_cita(cita: Cita)
        + mostrar_info(): String
    }

    %% Doctor hereda de Usuario y gestiona citas
    class Doctor {
        - especialidad: String
        - citas: List<Cita>
        + Doctor(nombre: String, email: String, telefono: String, especialidad: String)
        + get_especialidad(): String
        + set_especialidad(especialidad: String)
        + agendar_cita(cita: Cita)
        + listar_citas(): List<String>
        + mostrar_info(): String
    }

    %% Cita se asocia a Paciente y Doctor (asociación)
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

    %% Receta está fuertemente ligada a la Cita (composición)
    class Receta {
        - medicamentos: List<String>
        + Receta()
        + agregar_medicamento(medicamento: String)
        + mostrar_receta(): String
    }

    %% La clínica administra a los doctores (agregación)
    class Clinica {
        - nombre: String
        - doctores: List<Doctor>
        + Clinica(nombre: String)
        + get_nombre(): String
        + agregar_doctor(doctor: Doctor)
        + listar_doctores(): List<String>
    }

    %% SistemaGestorCitas gestiona las citas de pacientes y doctores (agregación)
    class SistemaGestorCitas {
        - citas: List<Cita>
        + SistemaGestorCitas()
        + agendar_cita(fecha: String, hora: String, doctor: Doctor, paciente: Paciente): Cita
        + cancelar_cita(cita: Cita)
        + listar_citas(): List<String>
    }

    %% Relaciones UML con multiplicidades y tipos de relación
    Usuario <|-- Paciente
    Usuario <|-- Doctor
    Paciente "1" o-- "*" Cita: reserva
    Doctor "1" o-- "*" Cita: atiende
    Cita *-- Receta: 0..1
    Doctor "1" o-- "*" Clinica: trabaja_en
    Clinica "1" o-- "*" Doctor: tiene
    SistemaGestorCitas "1" o-- "*" Cita: gestiona
```
DIAGRAMA DE  CASOS DE  USO  DE NUESTRO SISTEMA 

```mermaid 
graph TD
    %% Definimos los actores principales
    actorPaciente[Paciente] -->|Solicita| UC_ReservarCita["Reservar Cita"]
    actorPaciente -->|Cancela| UC_CancelarCita["Cancelar Cita"]
    actorPaciente -->|Consulta| UC_VerHistorial["Ver Historial Médico"]

    actorDoctor[Doctor] -->|Atiende| UC_AtenderCita["Atender Cita"]
    actorDoctor -->|Registra| UC_RegistrarReceta["Registrar Receta"]

    actorAdmin[Administrador] -->|Gestiona| UC_GestionarClinica["Gestionar Clínica"]
    actorAdmin -->|Configura| UC_AdministrarDoctores["Administrar Doctores"]

    %% Relacionamos casos de uso con el sistema principal
    subgraph SistemaGestorCitas
        UC_ReservarCita --> UC_RegistrarCita["Registrar Cita en el Sistema"]
        UC_CancelarCita --> UC_ModificarCita["Modificar/Cambiar Estado de la Cita"]
        UC_AtenderCita --> UC_FinalizarCita["Finalizar Cita en el Sistema"]
    end

    subgraph Clinica
        UC_GestionarClinica --> UC_AdministrarDoctores
    end

    %% Relación entre casos de uso
    UC_RegistrarReceta --> UC_AtenderCita
