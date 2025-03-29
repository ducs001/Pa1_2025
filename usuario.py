class Usuario:
    def __init__(self,nombre,email,telefono):
        self.nombre=nombre
        self.email=email
        self.telefono
    def mostrarInfo(self):
        return f"Nombre:{self.nombre},Email:{self.email}, Telefono:{self.telefono}"
    