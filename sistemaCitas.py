class SistemaGestorCitas:
    def __init__(self):
        self.citas = []
    
    def agendarCita(self,fecha,hora,doctor,paciente):
        cita=Cita(fecha,hora,doctor,paciente)
        self.citas.append(cita)
        paciente.reservarCita(cita)
        doctor.agedarCita(cita)
        return cita

    def cancelarCita(self,cita):
        if cita in self.citas:
            cita.cancelarCita()
    def listarCitas(self):
        return [cita.obtenerDetalles() for cita in self.citas]