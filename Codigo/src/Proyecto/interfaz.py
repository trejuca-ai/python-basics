from contacto import Contacto
from dao_contacto import DaoContacto

def menu():
    print("\n ------- Menu de opciones --------")
    print("1. Dar de alta ")
    print("2. Dar de baja ")
    print("3. Actualizar un contacto ")
    print("4. Buscar por nombre de contacto ")
    print("5. Exportar a CSV ")
    print("6. Exportar a JSON ")
    print("7. Exportar a PDF ")
    print("8. Listar todos ")
    print("9. Salir ")
    
def pedir_informacion_contacto():
            
    nombre = input("Nombre:")
    primer_apellido = input("Prime apelldo:")
    segundo_apellido = input("Segundo apellido:")
    email = input("Correo electronico:")
    
    contacto = Contacto(nombre, primer_apellido, segundo_apellido, email)
    return contacto

def main():
    
    bd = DaoContacto()
    
    while True:
        menu()
        opcion = input("Seleccione una opcion: ")
        
        match opcion:
            case "1":
                contacto = pedir_informacion_contacto()
                bd.alta_contacto(contacto)
                print("Contacto guardado exitosamente")
            case "2":
                pass
            case "3":
                pass
            case "9":
                print("bye bye...")
                break
            case _:
                print("Opcion invalida")
        
if __name__ == "__main__":
    main()