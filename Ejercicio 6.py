def suma_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero

    return suma

lista = [1,3,5,9,2]

print(suma_lista(lista))