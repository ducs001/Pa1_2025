from models.doctor import Doctor

class Clinica:
    def __init__(self, nombre):
        #Constructor de la clase Clinica. Representa una clínica con una lista de doctores
        self.__nombre = nombre
        self.__doctores = []  # Relación de agregación: la clínica tiene múltiples doctores

    def get_nombre(self):
        return self.__nombre

    def agregar_doctor(self, doctor):
        if isinstance(doctor, Doctor):
            self.__doctores.append(doctor)

    def listar_doctores(self):
        return [doctor.get_nombre() for doctor in self.__doctores]