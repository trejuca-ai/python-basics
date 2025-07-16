import persona as p

class Cuenta:
    def __init__(self, titular="", cantidad=0.0):
        self.__titular = p.Persona(titular)
        self.__cantidad = cantidad

    def __str__(self):
        return f"Titular: {self.__titular.get_nombre()}, Cantidad: {self.__cantidad}"
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
            return True
        return False
    
    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad
            return True
        return False

# ------- Probar funcionalidad de clase Cuenta

cuenta = Cuenta("Pedro Martinez", 1000.00)

print(cuenta)
print(cuenta.depositar(500.0))
print(cuenta)
print(cuenta.retirar(1000.0))
print(cuenta)