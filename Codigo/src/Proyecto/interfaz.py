from contacto import Contacto
from dao_contacto import DaoContacto
from tabulate import tabulate
from exportador import exportar_a_json, exportar_a_csv, exportar_a_pdf
from vlidadores import ContactoValidator
from pydantic import ValidationError

import constantes
import os
import platform

def menu():
    # Muestra el menu principal de opciones al usuario
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
    # Solicita al usuario la informacion de un contacto y valida los datos
    try:
        nombre = input("Nombre: ")
        primer_apellido = input("Prime apelldo: ")
        segundo_apellido = input("Segundo apellido: ")
        email = input("Correo electronico: ")
        
        datos_contacto = {
            "nombre": nombre,
            "primer_apellido": primer_apellido,
            "segundo_apellido": segundo_apellido,
            "email": email
        }
        
        # Valida los datos usando un modelo de validacion
        contacto_validator = ContactoValidator(**datos_contacto)

        # Crea y devuelve el objeto Contacto
        contacto = Contacto(nombre, primer_apellido, segundo_apellido, email)
        return contacto
    
    except ValidationError as e:
        # Muestra los errores de validacion campo por campo
        for error in e.errors():
            print(f"-- {error['loc'][0]}: {error['msg']}")

def main():
    # Funcion principal de la aplicacion que muestra el menu e interactua con el usuario
    bd = DaoContacto()
    
    while True:
        menu()
        opcion = input("Seleccione una opcion: ")
         
        match opcion:
            case "1":
                # Alta de contacto
                try:
                    contacto = pedir_informacion_contacto()
                    resultado = bd.alta_contacto(contacto)
                    mensaje = f"Contacto guardado con el id: {resultado}" if resultado else "No se pudo guardar."                
                    print(mensaje)
                except Exception as e:
                    print(e)
                    
            case "2":
                # Baja de contacto
                id_contacto = input("Id de contacto: ")
                eliminado = bd.baja_contacto(id_contacto)
                mensaje = "Contacto eliminado" if eliminado else "No se pudo eliminar. Verifique."                
                print(mensaje)

            case "3":
                # Actualizacion de contacto
                id_contacto = input("id de contacto: ")
                campo = input("campo a actualizar (nombre, primer_apellido, segundo_apellido, mail): ")
                nuevo_valor = input(f"nuevo valor para el {campo}: ")
                bd.actualiza_contacto(id_contacto, campo, nuevo_valor)

            case "4":
                # Buscar contacto por nombre
                nombre = input("Nombre a buscar: ")
                contacto = bd.buscar_por_nombre(nombre)
                if contacto:
                    print(contacto) 

            case "5":
                # Exportar contactos a CSV
                contactos = bd.mostrar_todos()
                exportar_a_csv(contactos, "reporte")

            case "6":
                # Exportar contactos a JSON
                contactos = bd.mostrar_todos()
                dict_datos = [dict(zip(constantes.ENCABEZADOS, tupla)) for tupla in contactos]
                exportar_a_json(dict_datos, "reporte")

            case "7":
                # Exportar contactos a PDF
                contactos = bd.mostrar_todos()
                exportar_a_pdf(contactos)

            case "8":
                # Mostrar todos los contactos en formato de tabla
                contactos = bd.mostrar_todos()
                if contactos:
                    print(tabulate(contactos, constantes.ENCABEZADOS, tablefmt="grid"))
                else:
                    print("No hay contactos en la base de datos")
                
            case "9":
                # Salida del programa
                bd.cerrar_conexion()
                print("bye bye...")
                break

            case _:
                # Opcion invalida
                print("Opcion invalida")
        
        input("Presione enter para continuar.. ")
        limpiar_pantalla()

def limpiar_pantalla():
    # Limpia la pantalla segun el sistema operativo
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
