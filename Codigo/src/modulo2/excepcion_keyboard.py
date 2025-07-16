import time

def ciclo():
    contador = 0
    print("Ciclo infinito. Presione Ctrl + c para terminar")

    try:
        while True:
            print(f"Iteracion {contador}...")
            time.sleep(1)
            contador += 1
    except BaseException as es:
        print(f"Se atrapo BaseException: {type(es)}")

def main():
    print("Iniciando programa principal")
    reintentos = 0

    while reintentos < 3:
        print(f"Numero de reitento: {reintentos + 1}")
        ciclo()
        reintentos += 1

if __name__ == "__main__":
    main()