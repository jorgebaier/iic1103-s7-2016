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
            return True
        else:
            return False
    if mostrar_suma(lista[1:],valor-lista[0],solucion+[lista[0]]): # se incluye lista[0]
        return True
    if mostrar_suma(lista[1:],valor,solucion): # no se incluye lista[0]
        return True
    return False

def retornar_suma(lista,valor,solucion=[]):
    if lista == []:
        if valor == 0:  # return valor == 0
            return solucion
        else:
            return None
    s = retornar_suma(lista[1:],valor-lista[0],solucion+[lista[0]]) # se incluye lista[0]
    if s != None:
        return s
    s = retornar_suma(lista[1:],valor,solucion) # no se incluye lista[0]
    if s != None:
        return s
    return None



def suma_todas(lista,valor,solucion,soluciones):
    if lista == []:
        if valor == 0:  # return valor == 0
            soluciones.append(solucion)
            return False
        else:
            return False
    if suma_todas(lista[1:],valor-lista[0],solucion+[lista[0]],soluciones): # se incluye lista[0]
        return True
    if suma_todas(lista[1:],valor,solucion,soluciones): # no se incluye lista[0]
        return True
    return False


def retornar_todas(lista,valor):
    soluciones = []
    suma_todas(lista,valor,[],soluciones)
    return soluciones    


#print(verificar_suma([4,10,9,3,11],22))
#print(verificar_suma([4,10,9,3,11],24))
#print(verificar_suma([4,10,9,3,11],7))
#print(verificar_suma([4,10,9,3,11],100))
#print(verificar_suma([4,10,9,3,11],8))
#print(verificar_suma([4,10,9,3,11],-1))

#print(mostrar_suma([4,10,9,3,11],22))
#print(mostrar_suma([4,10,9,3,11],24))
#print(mostrar_suma([4,10,9,3,11],7))
#print(mostrar_suma([4,10,9,3,11],100))
#print(mostrar_suma([4,10,9,3,11],8))
#print(mostrar_suma([4,10,9,3,11],-1))

print(retornar_todas([4,10,9,3,11],22))
print(retornar_todas([4,10,9,3,11],24))
print(retornar_todas([4,10,9,3,11],7))
print(retornar_todas([4,10,9,3,11],100))
print(retornar_todas([4,10,9,3,11],8))
print(retornar_todas([4,10,9,3,11],-1))
