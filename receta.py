class Receta:
    def __init__(self):
        self.medicamentos=[]
    
    def agregarMedicamentos(self,medicamentos):
        self.medicamentos.append(medicamentos)
    
    def mostrarRecetas(self):
        return f"Receta:{', '.join(self.medicamentos) if self.medicamentos else 'No hay medicamentos recetados'}"
