def selection_sort(L):
    #ordena la lista L usando ordenacion por seleccion

    i = 0
    while i < len(L):
        minimo = L[i] # contiene el valor mas pequeno en L (desde i en adelante)
        indice_minimo = i # contiene el indice del valor mas pequeno       
        j = i + 1
        while j < len(L):
            if L[j] < minimo:
                minimo = L[j]
                indice_minimo = j
            j += 1
        L[indice_minimo] = L[i]
        L[i] = minimo
        i += 1

nombre = input("nombre del archivo: ")
f= open(nombre,"r")
L = [int(x.strip()) for x in f.readlines()]
f.close()

selection_sort(L)
for x in L:
    print(x)

