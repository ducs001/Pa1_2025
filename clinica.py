class Clinica:
    def __init__(self,nombre):
        self.nombre=nombre
        self.doctores=[]

    def agregarDoctor(self, doctor):
        self.doctores.append(doctor)

    def listarDoctores(self):
        return [doctor.mostrarInfo() for doctor in self.doctores]