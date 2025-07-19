from datetime import datetime

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors

import constantes
import json
import csv
import os

# Define la ruta donde se guardaran los archivos exportados
PATH_FILE = os.path.join("src", "Proyecto", "files")

def exportar_a_json(lista_contactos, nombre_archivo="contacto"):
    # Exporta una lista de contactos a un archivo JSON con nombre y fecha actual
    fecha_hora = datetime.now().strftime("%d%m%Y_%H%M%S")
    archivo = os.path.join(PATH_FILE, f"{nombre_archivo}_{fecha_hora}.json")
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(lista_contactos, f, indent=4)

def exportar_a_csv(lista_contactos, nombre_archivo="contacto"):
    # Exporta una lista de contactos a un archivo CSV con encabezados
    fecha_hora = datetime.now().strftime("%d%m%Y_%H%M%S")
    archivo = os.path.join(PATH_FILE, f"{nombre_archivo}_{fecha_hora}.csv")
    
    with open(archivo, "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        # Escribe la fila de encabezados
        writer.writerow(constantes.ENCABEZADOS)
        # Escribe cada contacto como una fila
        for linea in lista_contactos:
            writer.writerow(linea)

def exportar_a_pdf(lista_contactos, nombre_archivo="contacto"):
    # Exporta una lista de contactos a un archivo PDF en forma de tabla
    datos = [constantes.ENCABEZADOS]
    fecha_hora = datetime.now().strftime("%d%m%Y_%H%M%S")
    archivo = os.path.join(PATH_FILE, f"{nombre_archivo}_{fecha_hora}.pdf")
    
    # Agrega los contactos a los datos de la tabla
    for contacto in lista_contactos:
        datos.append(contacto)
    
    # Crea el lienzo para dibujar el PDF
    lienzo = canvas.Canvas(archivo, pagesize=letter)
    anchura, altura = letter

    # Crea la tabla con estilo
    tabla = Table(datos)
    tabla.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),  # Fondo gris para encabezado
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),  # Texto blanco en encabezado
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),  # Centrado para todas las celdas
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),  # Fuente en negrita para encabezado
        ("FONTSIZE", (0, 0), (-1, -1), 8),  # Tamano de fuente uniforme
        ("BOTTOMPADDING", (0, 0), (-1, 0), 6),  # Espacio inferior en encabezado
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),  # Rejilla negra para todas las celdas
    ]))
    
    # Ajusta y dibuja la tabla en el lienzo
    tabla.wrapOn(lienzo, anchura, altura)
    tabla.drawOn(lienzo, 10, 600)
    lienzo.save()
