import random
def Aleato_list(n):
      lista = [0]  * n
      for i in range(n):
          lista[i] = random.random()
      return lista

print("Cuantos números desea imprimir? ")
n=int(input())

a=Aleato_list(n)
print(a)