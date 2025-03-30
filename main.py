from models.paciente import Paciente
from models.doctor import Doctor
from models.receta import Receta
from models.clinica import Clinica
from controllers.gestor_citas import GestorCitas

def main():
    print("Bienvenido al Sistema de Reserva de Citas Médicas")

    #  Asociación: La clínica tiene doctores (1 Clínica → * Doctores)
    clinica = Clinica("Clínica San Marcos")

    #  Asociación: Se crean doctores y se agregan a la clínica
    doctor1 = Doctor("Dra. Ana López", "ana@gmail.com", "987654321", "Cardiología")
    doctor2 = Doctor("Dr. Juan Pérez", "juan@gmail.com", "987654322", "Dermatología")
    clinica.agregar_doctor(doctor1)
    clinica.agregar_doctor(doctor2)

    #  Creación de pacientes
    paciente1 = Paciente("Carlos Pérez", "carlos@gmail.com", "987654321")
    paciente2 = Paciente("María González", "maria@gmail.com", "987654320")

    #  Agregación: El gestor de citas gestiona múltiples citas (* Citas → 1 Gestor)
    gestor = GestorCitas()

    #  Asociación: Una cita se asocia con un doctor y un paciente (1 Doctor → * Citas, 1 Paciente → * Citas)
    cita1 = gestor.agendar_cita("2025-04-01", "10:00 AM", doctor1, paciente1)
    cita2 = gestor.agendar_cita("2025-04-02", "11:00 AM", doctor2, paciente2)

    #  Mostramos las citas registradas
    print("\n Citas Agendadas:")
    for cita in gestor.listar_citas():
        print(cita)

    #  Asociación: Un paciente tiene un historial médico
    paciente1.agregar_historial("Paciente con presión arterial alta.")
    print("\n Historial Médico de Carlos:")
    print(paciente1.mostrar_info())

    #  Composición: La receta pertenece a una cita (1 Cita → 0..1 Receta)
    receta1 = Receta()
    receta1.agregar_medicamento("Paracetamol 500mg")
    receta1.agregar_medicamento("Aspirina 100mg")
    cita1.agregar_receta(receta1)

    print("\n Receta médica de la primera cita:")
    print(receta1.mostrar_receta())

    # Cancelación de una cita (se elimina de la lista de citas del gestor)
    gestor.cancelar_cita(cita2)
    print("\n Citas después de cancelar una:")
    for cita in gestor.listar_citas():
        print(cita)

if __name__ == "__main__":
    main()
