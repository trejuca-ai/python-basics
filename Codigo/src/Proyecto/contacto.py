class Contacto:
    def __init__(self, nombre, primer_apellido, segundo_apellido, email):
        # Inicializa un objeto de tipo Contacto con nombre, primer apellido, segundo apellido y correo electronico
        self.nombre = nombre
        self.primer_apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.email = email

    def __str__(self):
        # Devuelve una representacion en cadena del contacto con nombre, apellido y correo electronico
        return f"{self.nombre}|{self.primer_apellido}|{self.email}"

    @staticmethod
    def to_object(linea):
        # Convierte una linea de texto separada por '|' en un objeto de tipo Contacto
        nombre, primer_apellido, email = linea.strip().split("|")
        return Contacto(nombre, primer_apellido, email)
