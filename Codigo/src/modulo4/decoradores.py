# Decorador 1 que recibe solo una funcion

def validar_minusculas(funcion_original):
    def funcion_interna():
        print("En el decorador 1")
        funcion_original()
    return funcion_interna

def verificar_formato(funcion_original):
    def funcion_interna():
        print("En el decorador 2")
        funcion_original()
    return funcion_interna

@decorador_2
@decorador_1
def saludar():
    print("INSERT INTO tabla()")
    
saludar()