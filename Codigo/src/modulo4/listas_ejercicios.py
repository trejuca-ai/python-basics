
#  1. Dada una lista con elementos repetidos, devolver una nueva lista con los elementos únicos, 
# pero manteniendo el orden original.

def eliminar_repetidos(lista: list):
    resultado = []

    for elemento in lista:
        if elemento not in resultado:
            resultado.append(elemento)

    return resultado

# print(eliminar_repetidos([5,1,2,2,3,3,1,4]))

# 2. Dada una lista de números enteros (positivos y negativos), encontrar la sublista contigua con la 
# mayor suma posible.

def sumar_lista(lista):

    suma_total = 0
    suma_actual = 0
    contador = 0
    contador_temp = 0
    salida = ""
    suma_final = 0
    lista_ganadora = []

    while contador < len(lista):

        max_lista = contador_temp + 1
        lista_temp = lista[contador: max_lista]

        for numero in lista_temp:
            salida += f"{numero},"
            suma_total += numero

            if suma_total > suma_actual:
                suma_actual = suma_total
                suma_final = suma_total
                lista_ganadora = lista_temp
                break

        suma_total = 0

        if contador_temp < len(lista):
            contador_temp += 1
        else:
            contador += 1
            contador_temp = contador

    return lista_ganadora

# print(sumar_lista([1,-2,3,6]))

#  3. Dada una lista de números enteros, agrupar los que sean consecutivos en sublistas.

def agrupar_elementos(lista):

    lista.sort()
    resultado = []
    sublista = [lista[0]]

    for i in range(1, len(lista)):
        if lista[i] == lista[i - 1] + 1:
            sublista.append(lista[i])
        else:
            resultado.append(sublista)
            sublista = [lista[i]]
    
    resultado.append(sublista)
    return resultado

# print(agrupar_elementos([1,2,4,5,7,9]))

#  4. Escribir una función que reciba una lista y devuelva todas las permutaciones posibles de sus 
# elementos (ordenaciones distintas).
from itertools import permutations

def generar_permutaciones(lista):
    return list(permutations(lista))

print(generar_permutaciones([1,2,3,9]))