
# 1. Funcion map
numeros = [1,2,3,4,5]
dobles = list(map(lambda numero: numero * 2, numeros))
#print(dobles)

# 2. Funcion filter
pares = list(filter(lambda numero: numero % 2 == 0, numeros))
#print(pares)

# 3 Funcion reduce
from functools import reduce
suma = reduce(lambda acumulado, numero: acumulado + numero, numeros, 2)
#print(suma)

# 4. Funcion zip
nombres = ["Pedro", "Laura", "Oscar"]
edades = [20,30,40]

lista_combinada = dict(zip(nombres, edades))
#print(lista_combinada)

# 5. Funcion enumarate
for i, nombre in enumerate(nombres):
    #print(i, nombre)
    pass

# 6. Funcion any
lista_valores = [True, True, False]
print(any(lista_valores))

# 7. Funcion all
lista_valores = [True, True, False]
print(all(lista_valores))

