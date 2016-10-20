import random


def busqueda_binaria(N,L):
    inicio = 0
    fin = len(L) - 1
    while inicio <= fin:
        mitad = (inicio+fin)//2
        if L[mitad] == N:
            return True
        elif L[mitad] < N:
            inicio = mitad + 1
        else:
            fin = mitad - 1
    return False

def busqueda_lineal(N,L):
    # return x in L
    encontrado = False
    for x in L:
        if x==N:
            return True
    return False 

n = 0
print("Generando...")
L = []
for x in range(0,10000000):
    L.append(n)
    n = n+random.randint(0,500)

print("Buscando lineal...")
N = -10
if busqueda_lineal(N,L):
    print("encontrado")
else:
    print("no encontrado: ")
          
print("Buscando binaria...")
if busqueda_binaria(N,L):
    print("encontrado")
else:
    print("no encontrado")
