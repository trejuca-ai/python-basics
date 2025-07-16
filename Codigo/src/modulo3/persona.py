
class Persona:

    def __init__(self, nombre="", apellido="", edad=0, id=""):
        self.__nombre = nombre
        self.apellido = apellido
        self.__edad = edad
        self.__id = id

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_apellido(self):
        return self.apellido

    def set_apellido(self, apellido):
        self.apellido = apellido
    
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, edad):
        self.__edad = edad
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        print("hola desde id setter")
        self.__id = id

    def es_mayor_edad(self):
        return self.__edad > 18

    def __str__(self):
        return f"Persona(nombre={self.__nombre}, apellido={self.apellido})"



# ------- Probar funcionalidad de clase Persona

# cuenta = Cuenta(200)
# print(cuenta.cantidad)

# persona1 = Persona()
# persona1.set_nombre("Pablo")
# persona1.nombre = "LAura"

# Persona__nombre = "Alberto"
# persona1._Persona__nombre="Eduardo"

# print(persona1.get_nombre())
# print(persona1.nombre)
# print(persona1.get_nombre())
# print(Persona__nombre)
# print(persona1.get_nombre())

#persona2 = Persona()

# persona2.edad = 20
# print(persona2.edad)
