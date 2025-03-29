from usuario import Usuario

class Paciente(Usuario):
    def __init__(self,nombre,email,telefono):
        super().__init__(nombre,email,telefono)
        self.historia_medica=[]
        self.citas = []
    def mostrarInfo(self):
        return f"Paciente:{self.nombre},Email: {self.email},tel: {self.email},Citas:{len(self.citas)}"
    def agregarHistorial(self,entrada:str):
        self.historia_medica.append(entrada)
    def reservarCita(self,cita):
        self.citas.append(cita)