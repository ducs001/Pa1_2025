from doctor import Doctor
from paciente import Paciente

class Cita:
    def __init__(self,fecha,hora,doctor,paciente):
        self.fecha=fecha
        self.hora=hora
        self.doctor=doctor
        self.paciente=paciente
        self.estado="Pendiente"
        self.receta=None #Relacion de composicion

    def obtenerDetalles(self):
        return f"Cita el {self.fecha} a las {self.hora} con {self.doctor.nombre},Estado:{self.estado}"
    def cancelarCita(self):
        self.estado = "Cancelada"
    
    def agregarRecetas(self, receta):
        self.receta=receta