

class Contacto:
    def __init__(self, nombre, primer_apellido, segundo_apellido, email):
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.email = email
        
    def __str__(self):
        return f"{self.nombre}|{self.apellido}|{self.email}"
    
    @staticmethod
    def to_object(linea):
        nombre, apellido, email = linea.strip().split("|")
        return Contacto(nombre, apellido, email)
    