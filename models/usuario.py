class Usuario:
    # Clase base Usuario que representa a una persona dentro del sistema.
    def __init__(self, nombre, email, telefono):
        self.__nombre = nombre          # Encapsulación: Atributo privado
        self.__email = email            # Encapsulación: Atributo privado
        self.__telefono = telefono      # Encapsulación: Atributo privado

    # Métodos Getters y Setters
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_email(self) :
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_telefono(self):
        return self.__telefono

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def mostrar_info(self) :
        return f"Nombre: {self.__nombre}, Email: {self.__email}, Teléfono: {self.__telefono}"