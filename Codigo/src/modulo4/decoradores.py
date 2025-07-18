# Decorador 1 que recibe solo una funcion

def decorador_1(funcion_original):
    def funcion_interna():
        print("En el decorador 1")
        funcion_original()
    return funcion_interna

def decorador_2(funcion_original):
    def funcion_interna():
        print("En el decorador 2")
        funcion_original()
    return funcion_interna

@decorador_1
@decorador_2
def saludar():
    print("INSERT INTO tabla()")
  
saludar()
mi_funcion =  decorador_1(decorador_2(saludar))
mi_funcion()