def palidromo(texto):
    pos_izquierda = 0
    pos_derecha = len(texto)-1
    while pos_derecha >= pos_izquierda:
        if not texto[pos_izquierda] == texto[pos_derecha]:
            return False

        pos_izquierda +=1
        pos_derecha -= 1

    return True

print(palidromo("ana"))
