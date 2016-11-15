def mezcla(L1,L2):
    R = []
    i = 0
    j = 0
    while i < len(L1) and j < len(L2):
        if L1[i] <= L2[j]:
            R.append(L1[i])
            i += 1
        else:
            R.append(L2[j])
            j += 1
    if i >= len(L1):
        R.extend(L2[j:])
    else:
        R.extend(L1[i:])

    return R

def mergesort(L):
    if len(L) <= 1:
        return L
    m = len(L)//2
    L1 = mergesort(L[:m])
    L2 = mergesort(L[m:])
    return mezcla(L1,L2)

nombre = input("Nombre del archivo: ")
f = open(nombre, "r")
L = [int(linea.strip()) for linea in f.readlines()]
f.close()

L=mergesort(L)

for x in L:
    print(x)

