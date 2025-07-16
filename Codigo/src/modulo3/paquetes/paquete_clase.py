
class Saludar:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        return f"Hola desde la clase Saludar, soy {self.nombre}"