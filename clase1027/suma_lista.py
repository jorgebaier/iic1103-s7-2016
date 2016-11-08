def sumaListaI(L):
    suma=0
    for x in L:
        suma+=x
    return suma

def sumaLista(L):
    if len(L) == 0:
        return 0
    else:
        return L[0] + sumaLista(L[1:])

def en(x,L): # retorna True si x está en L (False en caso contrario)
    if len(L) == 0:
        return False
    if L[0] == x:
        return True
    else:
        return en(x,L[1:])

def en2(x,L): # retorna True si x está en L (False en caso contrario)
    if len(L) == 0:
        return False
    return L[0] == x or en2(x,L[1:])

def superSumaLista(L):
    if len(L)==0:
        return 0
    elif type(L[0])==list:
        return superSumaLista(L[0]) + superSumaLista(L[1:])
    else:
        return L[0]+ superSumaLista(L[1:])
    
print(superSumaLista([1,[2,-1,[1]],[],[[[[[3]]]]]]))   

#print(sumaLista([1,2,3]))
#print(sumaListaI([1,2,3]))
    
#print(en(2,[1,2,3]))
#print(en(4,[1,2,3]))
