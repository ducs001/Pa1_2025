from models.sistema_gestor import SistemaGestorCitas

class GestorCitas:
    #control de citas
    def __init__(self):
        self.__sistema = SistemaGestorCitas()

    def agendar_cita(self, fecha, hora, doctor, paciente):
        return self.__sistema.agendar_cita(fecha, hora, doctor, paciente)

    def cancelar_cita(self, cita):
        self.__sistema.cancelar_cita(cita)

    def listar_citas(self):
        return self.__sistema.listar_citas()
