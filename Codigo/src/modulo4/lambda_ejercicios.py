#  2. Dada una lista de palabras, filtrar y conserva solo las que tienen 4 letras o menos usando filter

palabras = ["este", "es", "el", "curso", "de", "python"]
lista_menor_4_palabras = list(filter(lambda letra: len(letra) <= 4, palabras))

# print(lista_menor_4_palabras)

# 3. Dada una lista de números, crear una nueva lista con el cuadrado de los que son pares, usando 
# filter y map

numeros = [1,2,3,4,5]
cuadrados = list(map(lambda numero: numero ** 2, 
                     filter(lambda numero_filtrado: numero_filtrado % 2 == 0, numeros)))
# print(cuadrados)

# 4. Dada una lista de palabras, contar cuántas empiezan con vocal
vocales = list(filter(lambda palabra: palabra[0] in "aeiou", palabras))
# print(len(vocales))

# 5. Dada una lista de números enteros, sumar todos los dígitos de los números que son impares. 
from functools import reduce
numeros_impares = [5,55,44,11,2,4]
suma_impares = reduce(
    lambda acumulado, valor: acumulado + sum(map(int, str(valor))),
    filter(lambda numero: numero % 2 != 0, numeros_impares),
    0
)
print(suma_impares)