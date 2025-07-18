import os
from pprint import pprint

"""
    1. Leer el archivo info.csv y convertir los datos en un diccionario
    2. Convertir el diccionario en una cadena que tenga formato JSON
        2a. Leemos los nombres de columnas y los almacenamos en una lista llamada encabezados 
        2b. Formamos una lista de diccionarios. Cada diccionario contiene clave - valor del 
            nombre de columna y su valor del archivo info.csv
    3. Formamos una cadena con los datos que vienen del archivo csv en formato json
    4. Escribimos la cadena formateada en el archivo final con extension .json    
        
"""
# Rutas de archivos a manejar
archivo_csv = "./src/modulo5/info.csv"
archivo_json = "./src/modulo5/info.json"

# Lista para guardar los contactos
contactos = []

# Abrir el csv para extraer informacion
with open(archivo_csv, mode="r", encoding="utf-8") as f:
    lineas = f.readlines()
    
encabezados = lineas[0].split(",")

for linea in lineas[1:]:
    valores = linea.split(",")
    contacto = {encabezados[i].strip(): valores[i].strip() for i in range(len(encabezados))}
    contactos.append(contacto)
    
json_texto = "[\n"

for i, contacto in enumerate(contactos):
    json_texto += "    {\n"
    
    for j, (clave, valor) in enumerate(contacto.items()):
        coma = ',' if j < len(contacto) - 1 else ''
        json_texto += f'        "{clave}": "{valor}"{coma}\n'
        
    coma = ',' if i < len(contactos) - 1 else ''
    json_texto += f'    }}{coma}\n'
    
json_texto += ']'

with open(archivo_json, mode="w", encoding="utf-8") as f:
    f.write(json_texto)
    
