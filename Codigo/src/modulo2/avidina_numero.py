import random

def adivinar_numero():

    numero_aleatorio = random.randint(1,100)
    intentos = 0
    adivinado = False

    while not adivinado:
        try:
            numero_usuario = input("Ingresa un numero o -1 para salir: ")

            if numero_usuario == '-1':
                print(f"Oh que lastima, el numero secreto era {numero_aleatorio}")
                break

            numero_usuario = int(numero_usuario)
            intentos += 1

            if numero_usuario < numero_aleatorio:
                print("El numero introducido es bajo")
            elif numero_usuario > numero_aleatorio:
                print("El numero introducido es alto")
            else:
                adivinado = True
                print(f"Felicidades, el numero es {numero_aleatorio}")
                print(f"Te tomo {intentos} intentos")
        except Exception as e:
            print(f"Ocurrio un error inesperado: {e}")
            break

if __name__ == "__main__":
    adivinar_numero()