

directorio =  """id;nombre;email;teléfono;descuento|01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5|71476342J;Macarena Ramírez;macarena@mail.com;692839321;8|63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2S|98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"""

lineas = directorio.strip().split("|")
columnas = lineas[0].split(";")
empleados = {}
#print(lineas[1])

for linea in lineas[1:]:
    #print(linea)
    valores = linea.split(";")
    id_empleado = valores[0]
    datos_empleado = dict(zip(columnas[1:], valores[1:]))
    empleados[id_empleado] = datos_empleado

from pprint import pprint
pprint(empleados)