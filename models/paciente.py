from models.usuario import Usuario

class Paciente(Usuario):
    # Paciente hereda de Usuario y tiene su propio historial médico y citas
    def __init__(self, nombre, email, telefono):
        super().__init__(nombre, email, telefono)
        self.__historia_medica = []  # Lista privada para el historial médico
        self.__citas = []  # Lista privada para almacenar citas

    def get_historia_medica(self):
        return self.__historia_medica

    def agregar_historial(self, entrada):
        self.__historia_medica.append(entrada)

    def reservar_cita(self, cita):
        self.__citas.append(cita)

    def mostrar_info(self): #Polimorfismo
        return f"{super().mostrar_info()}, Historial Médico: {len(self.__historia_medica)} registros, Citas: {len(self.__citas)}"
