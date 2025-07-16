datos = (1,2,3,4,5)
nueva_variable = [numero**2 for numero in datos]

print(nueva_variable)

nueva_lista = []
for numero in datos:
    nueva_lista.append(numero**2)

print(nueva_lista)