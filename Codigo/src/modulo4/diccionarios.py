
estudiantes = {
    "juan": {
        "edad": 20,
        "cursos": ["python", "javascript"],
        "calificacion": 8
    },
    "maria": {
        "edad": 30,
        "cursos": ["java", "PHP"],
        "calificacion": 10
    },
    "pedro": {
        "edad": 40,
        "cursos": ["angular", "react"],
        "calificacion": 9
    }
}


# 1. Imprimir todos los nombres de los estudiantes
# print(list(estudiantes.keys()))

# 2. Imprimir todas las calificaciones
#for datos in estudiantes.values():
#    print(datos['calificacion'])
calificaciones = [datos['calificacion'] for datos in estudiantes.values()]
# print(calificaciones)

# 3. Imprimir el nombre y edad de cada estudiante
for nombre, datos in estudiantes.items():
    # print(f"Nombre: {nombre}, Edad: {datos['edad']}")
    pass

# 4. Eliminar un estudiante
estudiante_eliminado = estudiantes.pop('pedro')
# print(estudiante_eliminado) 
# print(estudiantes)

# 5. Obtener los cursos de un estudiante
#cursos = estudiantes.get('maria').get('cursos')
cursos = estudiantes["maria"]["cursos"]
print(cursos)