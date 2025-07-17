
# Counter

from collections import Counter
from collections import defaultdict
from pprint import pprint
palabra = Counter([1,2,2,3,3,3,3,"Cadena", False])

print(palabra.most_common(2))

# defaultdict
diccionario = defaultdict(list)
palabras = [True, False, True, [0, 1], [4,5]]

for palabra in palabras:
    tipo = type(palabra).__name__
    diccionario[tipo].append(palabra)

pprint(diccionario)