from models.cita import Cita

class SistemaGestorCitas:

    def __init__(self):
        self.__citas = []# Asociacion con la clase cita

    def agendar_cita(self, fecha, hora, doctor, paciente):
        nueva_cita = Cita(fecha, hora, doctor, paciente)
        self.__citas.append(nueva_cita)
        paciente.reservar_cita(nueva_cita)
        doctor.agendar_cita(nueva_cita)
        return nueva_cita

    def cancelar_cita(self, cita):
        cita.cancelar_cita()

    def listar_citas(self):
        return [cita.obtener_detalles() for cita in self.__citas]
