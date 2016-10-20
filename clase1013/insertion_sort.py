def insertion_sort(L):
    i = 1
    while i < len(L):
        j = i - 1
        while j >= 0 and L[j] > L[j+1]:
            L[j],L[j+1] = L[j+1],L[j]
            j -= 1
        i += 1

nombre = input("nombre del archivo: ")
f= open(nombre,"r")
L = [int(x.strip()) for x in f.readlines()]
f.close()

insertion_sort(L)
for x in L:
    print(x)
