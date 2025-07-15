
# Atrapar excepciones try - except - else
try:
    numero = int(input("Ingresa un numero: "))
    resultado = 10 / numero
    raise ReferenceError("Se lanza este error aunque no estoy manejando archivos")
except ZeroDivisionError as error:
    print("No se puede dividir por cero")
except ValueError as error:
    print("Valor no valido")
except Exception as error:
    print("Se atrapo un error generico")
    print("Mensaje: ", str(error))
else:
    print("El resultado es: ", resultado)
finally:
    print("Linea que siempre se va a ejecutar")