
# ------ Opcion1. Importar un modulo especifico del paquete
import paquetes.paquete_clase
import paquetes.paquete_funciones

print(paquetes.paquete_funciones.funcion_uno(200))

objeto_clase1 = paquetes.paquete_clase.Saludar("Andrea")
print(objeto_clase1.saludar())
print("-" * 50)

# ------ Opcion 2. Importar una funcion o clase especifica de un paquete
from paquetes.paquete_funciones import funcion_dos
from paquetes.paquete_clase import Saludar

print(funcion_dos("texto paquete"))

objeto_clase2 = Saludar("Lorena")
print(objeto_clase2.saludar())
print("-" * 50)

# ------ Opcion 3. Importar una funcion o clase especifica de un paquete con un alias
from paquetes.paquete_funciones import funcion_dos as primera
from paquetes.paquete_clase import Saludar as CLASE

print(primera("texto paquete con alias"))

objeto_clase3 = CLASE("Lorena")
print(objeto_clase3.saludar())
print("-" * 50)