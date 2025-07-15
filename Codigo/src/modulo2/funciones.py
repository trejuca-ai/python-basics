
# Argumentos por nombre
def sumar(a=1, b=2, c=0):
    return a + b + c

# shift + alt + flecha abajo
#print(sumar(5,5,3))
#print(sumar(5,5))
#print(sumar(5))
#print(sumar())
#print(sumar(b=5, c=5))

# Argumentos de longitud variable (lista y tupla)
# Dependiendo del tipo de argumento que reciba
# lista o *args
def sumar2(numeros):
    total = 0
    print(type(numeros))
    for numero in numeros:
        total += numero
    return total

# print(sumar2([]))

def sumar3(**numeros):
    total = 0
    print(type(numeros))
    for clave, valor in numeros.items():
        print(clave, valor)
        total += valor
    return total

print(sumar3(a=1, z=2, w=6))
