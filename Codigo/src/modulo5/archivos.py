import os
ARCHIVO = "./src/modulo5/trabajo.txt"

# 1. Verifificar si el archivo existe

def leer_todo_archivo():
    archivo_nombre = ARCHIVO

    print(os.getcwd())
    if os.path.exists(archivo_nombre):
        archivo = open(archivo_nombre, "r")
        print(archivo.read())
    else:
        print(f"El archivo {archivo_nombre} no existe")
    
# 2. Leer un archivo y manejar errores con try/except

def manejar_errores_archivo(nombre):
    try:
        archivo = open(nombre, "r")
        contenido = archivo.read()
        print(contenido)
        archivo.close()
    except FileNotFoundError:
        print("No se encontro el archivo")
    except IOError:
        print("No se pudo abrir el archivo")
        
# manejar_errores_archivo("trabajo.txt")

# 3. Escribir en un archivo solo si no esta vacio
def escribir_archivo_si_no_vacio(nombre):
    archivo = open(nombre, "r")
    contenido = archivo.read()
    archivo.close()
    
    if contenido != "":
        archivo = open(nombre, "a")
        archivo.write("Esta es una nueva linea")
    else:
        print("No se escribio nada en el archivo")    
    archivo.close()
    
# escribir_archivo_si_no_vacio(ARCHIVO)

# 4. Cuente una palabra en un archivo
def contar_palabra(nombre):
    
    archivo = open(nombre, "r")
    contenido = archivo.read()
    
    palabra = "que"
    cantidad = contenido.count(palabra)
    print(f"La palabra {palabra} aparece {cantidad} veces")
    
# 0contar_palabra(ARCHIVO)

# 5. Eliminar un archivo
def eliminar_archivo(nombre):
        
    if os.path.exists(nombre):
        confirmacion = input("Seguro que desea eliminar el archivo S/N: ")
        if confirmacion == "s":
            os.remove(nombre)
        else:
            print("eliminacion cancelada")
    else:
        print("No existe el archivo")
        
eliminar_archivo(ARCHIVO)
