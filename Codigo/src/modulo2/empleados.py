
def registrar_empleado():

    
    while True:
        nombre = input("Ingresa el nombre del empleado: ")

        if len(nombre) > 10:
            print("El nombre sobre pasa la longitud de 10 caracteres")
        else:
            break

    while True:
        try:
            salario = float(input("Ingresa el salario del empleado: "))
            
            if (salario < 0):
                print("El salario del empleado no puede ser negativo")
            else:
                break

        except ValueError:
            print("Salario invalido. Por favor, ingrese un numero valido ")

    print(f"Nombre del empleado: {nombre}, Salario: {salario}")


if __name__ == "__main__":
    while True:
        registrar_empleado()
        salida = input("Presione -1 para terminar el programa o registrar otro empleado: ")

        if salida == "-1":
            break