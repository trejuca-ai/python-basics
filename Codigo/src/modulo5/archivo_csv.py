"""
 2. De acuerdo al siguiente diccionario, 
transformar los datos para que puedan 
ser guardados en un archivo csv
"""

data = {
  'country1': {
    'name': 'Albania',
    'area': 28748,
    'country_code': 'AL'
  },
  'country2': {
    'name': 'USA',
    'area': 9846,
    'country_code': 'US'
  },
  "country3": {
    'name': 'Mexico',
    'area': 52,
    'country_code': 'MX'
  },
}

import csv

ARCHIVO = "./src/modulo5/paises.csv"

with open(ARCHIVO, mode="w", newline='', encoding="utf-8") as f:
    
    # Definir los encabezados
    encabezados = ["name", "area", "country_code", "otro", "y otro mas"]
    writer = csv.DictWriter(f, fieldnames=encabezados)
    writer.writeheader()
    
    for country in data.values():
        writer.writerow(country)
        
print(f"Datos guardados en  {ARCHIVO}")