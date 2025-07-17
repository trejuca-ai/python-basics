usuarios = {
    '1': {
        'nombre': 'Juan',
        'edad': 23,
        'curso': 'Curso de Python',
        'skills': {
            'programacion': True,
            'base_de_datos': False
        },
        'medallas': ['básico', 'intermedio']
    },
    '2': {
        'nombre': 'Carlos',
        'edad': 30,
        'curso': 'Curso de Java',
        'skills': {
            'programacion': True,
            'base_de_datos': True
        },
        'medallas': ['básico']
    }
}

# a) Obtener la edad promedio de los usuarios.
edad = sum(datos['edad'] for datos in usuarios.values())
# print(edad / len(usuarios))

# b)  Verificar cuántos usuarios tienen la habilidad "base_de_datos" activada.
usuarios_bd_suma = sum(1 for usuario in usuarios.values() if usuario['skills']['base_de_datos']) 
#print(usuarios_bd_suma)

# c) Crear una lista con los nombres de los usuarios que 
# tienen el curso de "Curso de Python" y la habilidad 
# "programacion" activada.
cursos_python = [
    usuario['nombre']
    for usuario in usuarios.values() 
    if usuario['skills']['programacion'] and usuario['curso'] == 'Curso de Python'
    ]
print(cursos_python)

# d) Agregar una nueva medalla "avanzado" para cada 
# usuario que tenga la habilidad "base_de_datos" 
# activada.
from pprint import pprint

for usuario in usuarios.values():
    if usuario['skills']['base_de_datos']:
        usuario['medallas'].append('avanzado')

#pprint(usuarios)

# Mostrar el nombre de los usuarios y la cantidad de 
# medallas que tienen.
for usuario in usuarios.values():
    nombre = usuario['nombre']
    medallas = len(usuario['medallas'])
    print(f"{nombre} tiene {medallas} medallas")

