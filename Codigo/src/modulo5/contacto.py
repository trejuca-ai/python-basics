"""
Ejercicio
 Archivos
 1. Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, 
primer apellido, el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones:
 • Añadir contacto
 • Listar contactos.
 • Buscar contacto por uno o mas atributos de la clase.
 • Editar contacto.
 • Borrar contacto.
 • Salir
 La información del contacto se deberá guardar en un archivo de texto plano. Cada contacto se 
guardará en una línea y tendrá el formato:
 nombre|primer_apellido|email|telefono
"""
import os

CODIFICACION = "utf-8"
ARCHIVO = "./src/modulo5/agenda.txt"


class Contacto:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        
    def __str__(self):
        return f"{self.nombre}|{self.apellido}|{self.email}"
    
    @staticmethod
    def to_object(linea):
        nombre, apellido, email = linea.strip().split("|")
        return Contacto(nombre, apellido, email)
    
class Agenda:
    def __init__(self, archivo = ARCHIVO):
        self.archivo = archivo
        self.contactos = self.cargar_contactos()
        
    def cargar_contactos(self):
        contactos = []
        if os.path.exists(self.archivo):
            with open(self.archivo, "r", encoding=CODIFICACION) as f:
                for contacto in f:
                    # contactos.append(contacto)
                    contactos.append(Contacto.to_object(contacto))
        
        return contactos
    
    def aniadir_contacto(self):
        nombre = input("Ingresa el nombre: ")
        apellido = input("Ingresa el apellido: ")
        email = input("Ingresa el email: ")
        
        contacto = Contacto(nombre, apellido, email)
        self.contactos.append(contacto)
    
        with open(self.archivo, "a", encoding=CODIFICACION, newline="\n") as f:
            f.write(contacto.__str__())
        
        #with open(self.archivo, "w", encoding=CODIFICACION) as f:
        #    for contacto in self.contactos:
        #        f.write(contacto.__str__() + "\n")

    def listar_contactos(self):
        if not self.contactos:
            print("No hay ningun contacto")
            return
        
        print("-------- Contactos ---------")
        
        for numero, contacto in enumerate(self.contactos, 1):
            print(f"{numero} - {contacto}")    
        
    
    def buscar_contacto(self):
        termino = input("Buscar por nombre, apellido o correo: ")
        encontrados = []
        
        for contacto in self.contactos:
            datos = contacto.split("|")
            
            if termino in datos:
                encontrados.append(contacto)
                
        if encontrados:
            for numero, contacto in enumerate(encontrados, 1):
                print(f"{numero}. {contacto}")
        else:
            print("No se encontro ningun contacto en la agenda con este termino de busqueda")

    def buscar_contacto_objeto(self):
        termino = input("Buscar por nombre, apellido o correo: ")
        encontrados = [
            contacto for contacto in self.contactos if
            termino in contacto.nombre.lower() or 
            termino in contacto.apellido.lower() or 
            termino in contacto.email.lower() 
        ]
                
        if encontrados:
            for numero, contacto in enumerate(encontrados, 1):
                print(f"{numero}. {contacto}")
        else:
            print("No se encontro ningun contacto en la agenda con este termino de busqueda")
    
     
    def mostrar_menu(self):
        
        while True:
            print("\n ------- Menu de opciones --------")
            print("1. Listar contactos ")
            print("2. Guardar contacto ")
            print("3. Buscar contacto ")
            
            opcion = input("Elije una opcion: ")
            
            match opcion:
                case "1":
                    self.listar_contactos()
                case "2":
                    self.aniadir_contacto()
                case "3":
                    self.buscar_contacto_objeto()
                case "9":
                    print("bye bye...")
                    break
                case _:
                    print("Opcion invalida")
        
if __name__ == "__main__":
    agenda = Agenda()
    agenda.mostrar_menu()
