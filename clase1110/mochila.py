def verificar_suma(lista,valor):
    if lista == []:
        if valor == 0:  # return valor == 0
            return True
        else:
            return False
    if verificar_suma(lista[1:],valor-lista[0]): # se incluye lista[0]
        return True
    if verificar_suma(lista[1:],valor): # no se incluye lista[0]
        return True
    return False


def mostrar_suma(lista,valor,solucion=[]):
    if lista == []:
        if valor == 0:  # return valor == 0
            print(solucion)
            return False
        else:
            return False
    if mostrar_suma(lista[1:],valor-lista[0],solucion+[lista[0]]): # se incluye lista[0]
        return True
    if mostrar_suma(lista[1:],valor,solucion): # no se incluye lista[0]
        return True
    return False


#print(verificar_suma([4,10,9,3,11],22))
#print(verificar_suma([4,10,9,3,11],24))
#print(verificar_suma([4,10,9,3,11],7))
#print(verificar_suma([4,10,9,3,11],100))
#print(verificar_suma([4,10,9,3,11],8))
#print(verificar_suma([4,10,9,3,11],-1))

print(mostrar_suma([4,10,9,3,11],22))
print(mostrar_suma([4,10,9,3,11],24))
print(mostrar_suma([4,10,9,3,11],7))
print(mostrar_suma([4,10,9,3,11],100))
print(mostrar_suma([4,10,9,3,11],8))
print(mostrar_suma([4,10,9,3,11],-1))
