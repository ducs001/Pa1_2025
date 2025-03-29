from sistema_gestor_citas import SistemaGestorCitas
from paciente import Paciente
from doctor import Doctor

def main():
    # Crear el sistema
    sistema = SistemaGestorCitas()

    # Crear un paciente y un doctor
    paciente = Paciente("María López", "maria@mail.com", "987654321")
    doctor = Doctor("Dr. Juan Pérez", "juan@mail.com", "123456789", "Cardiología")

    # Agendar una cita
    cita = sistema.agendar_cita("2025-04-10", "10:30 AM", doctor, paciente)

    # Mostrar información de la cita
    print(cita.obtener_detalles())

    # Cancelar la cita
    sistema.cancelar_cita(cita)
    print(cita.obtener_detalles())  # Debe mostrar "Cancelada"

if __name__ == "__main__":
    main()