from models.doctor import Doctor
from models.paciente import Paciente
from models.receta import Receta

class Cita:
    def __init__(self, fecha, hora, doctor, paciente):
        #Constructor de la clase Cita. Define la relación entre un Doctor y un Paciente en una fecha y hora específicas. 
        self.__fecha = fecha
        self.__hora = hora
        self.__estado = "Agendada"  # Estado inicial
        self.__doctor = doctor #Asociacion con la clase doctor
        self.__paciente = paciente#Asociacion con la clase paciente 
        self.__receta = None  # Relación de composición, inicialmente sin receta

    def obtener_detalles(self):
        detalles = f"Cita: {self.__fecha} {self.__hora}, Estado: {self.__estado}, "
        detalles += f"Doctor: {self.__doctor.get_nombre()}, Paciente: {self.__paciente.get_nombre()}"
        return detalles

    def cancelar_cita(self):
        self.__estado = "Cancelada"

    def agregar_receta(self, receta):
        if isinstance(receta, Receta):
            self.__receta = receta

