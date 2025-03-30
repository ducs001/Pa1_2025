from models.usuario import Usuario

class Doctor(Usuario):#Doctor hereda de la clase usuario

    def __init__(self, nombre, email, telefono, especialidad):
        super().__init__(nombre, email, telefono)
        self.__especialidad = especialidad  # Encapsulación: Atributo privado
        self.__citas = []  # Lista privada para almacenar citas

    # Getter y Setter para la especialidad
    def get_especialidad(self):
        return self.__especialidad

    def set_especialidad(self, especialidad):
        self.__especialidad = especialidad

    # Método para agendar una nueva cita
    def agendar_cita(self, cita):
        self.__citas.append(cita)

    # Método para listar todas las citas del doctor
    def listar_citas(self):
        return [cita.obtener_detalles() for cita in self.__citas]

    # Polimorfismo: Sobrescribimos el método mostrar_info() de Usuario
    def mostrar_info(self):
        return f"{super().mostrar_info()}, Especialidad: {self.__especialidad}, Citas agendadas: {len(self.__citas)}"