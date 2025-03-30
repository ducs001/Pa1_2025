class Receta:

    def __init__(self):
        self.__medicamentos = []

    def agregar_medicamento(self, medicamento):
        self.__medicamentos.append(medicamento)

    def mostrar_receta(self):
        return f"Medicamentos: {', '.join(self.__medicamentos)}"
