from usuario import Usuario
class Doctor(Usuario):
    def __init__(self,nombre,email,telefono,especialidad):
        super().__init__(nombre,email,telefono)
        self.especialidad=especialidad
        self.citas=[]
    
    def mostrarInfo(self):
        return f"Doctor:{self.nombre}, Especialidad: {self.especialidad},Email: {self.email}"
    
    def agedarCita(self, cita):
        self.citas.append(cita)

    def lista_citas(self):
        return [cita.obtenerDetalles() for cita in self.citas]




