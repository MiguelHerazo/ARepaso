def media_lista(lista):
    suma = 0
    con = 0
    for numero in lista:
        suma += numero
        con = con+1

    return suma/con

lista = [1,3,5,9,2]

print(media_lista(lista))