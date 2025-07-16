
# ----- Opcion 1: Importar modulos completos
import modulo_clase
import modulo_funciones

print(modulo_funciones.funcion_uno(20))
print(modulo_funciones.funcion_dos("texto"))

objeto_saludar = modulo_clase.Saludar("Juan")
print(objeto_saludar.saludar())
print("-" * 50)

# ----- Opcion 2: Importar funciones especificas o clases
from modulo_funciones import funcion_uno
from modulo_clase import Saludar

print(funcion_uno(50))

objeto_saludar2 = Saludar("Paco")
print(objeto_saludar2.saludar())
print("-" * 50)

# ----- Opcion 3: Importar funciones o clases con un alias
import modulo_funciones as funciones
from modulo_clase import Saludar as HOLA

print(funciones.funcion_dos("nuevo texto"))

objeto_saludar3 = HOLA("Raul")
print(objeto_saludar3.saludar())