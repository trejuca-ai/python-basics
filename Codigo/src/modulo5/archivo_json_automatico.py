
import csv
import json

# Rutas de archivos a manejar
archivo_csv = "./src/modulo5/info.csv"
archivo_json = "./src/modulo5/info_automatico.json"

# Abrir el csv para extraer informacion
with open(archivo_csv, mode="r", encoding="utf-8") as f:
    lector = csv.DictReader(f)
    datos = list(lector)
    
with open(archivo_json, mode="w", encoding="utf-8") as f:
    json.dump(datos, f, indent=8, ensure_ascii=False)
    