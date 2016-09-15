### Inicio código de jugador perfecto

def jugar_maquina(ficha,tablero):
    valor,jugada = mejor_jugada(ficha,tablero,ficha)
    return jugada

def valor_tablero(mificha,tablero,ficha):
    quien_gana = ganador(tablero)
    if quien_gana != 0:
        return quien_gana*mificha
    valor,jugada = mejor_jugada(mificha,tablero,ficha)
    return valor

def mejor_jugada(mificha,tablero,ficha):
    jugadas_legales=legales(tablero,ficha)
    if len(jugadas_legales)==0:
        return 0,[-1,-1,0]
    elif len(jugadas_legales)==9: # tablero está vacio
        return 0,[1,1,mificha]
    valores=[valor_tablero(mificha,realiza_jugada(tablero,j),-ficha) for j in jugadas_legales]
    if ficha==mificha:
        indice=valores.index(max(valores))
    else:
        indice=valores.index(min(valores))
    return valores[indice],jugadas_legales[indice]



### Fin código de jugador perfecto



def ficha2str(valor):
    if valor==0:
        return ' '
    elif valor==1:
        return 'X'
    else:
        return 'O'

def tablero2str(tablero):
    tab = "|".join([ficha2str(x) for x in tablero[0]])+"\n"
    tab = tab+"-"*5+"\n"
    tab = tab+"|".join([ficha2str(x) for x in tablero[1]])+"\n"
    tab = tab+"-"*5+"\n"
    tab = tab+"|".join([ficha2str(x) for x in tablero[2]])+"\n"
    
    return tab

def ganador(tablero):
## retorna la ficha del ganador del tablero, de haber un ganador, o 0 de no haber ganador
    # revisamos las filas
    i = 0
    while i < 3:
        if tablero[i][0]==tablero[i][1]==tablero[i][2]!=0:
            return tablero[i][0]
        i = i + 1

    # revisamos las columnas
    i = 0
    while i < 3:
        if tablero[0][i]==tablero[1][i]==tablero[2][i]!=0:
            return tablero[0][i]
        i = i + 1
    # revisamos las diagonales

    if tablero[0][0]==tablero[1][1]==tablero[2][2]!=0 or \
       tablero[2][0]==tablero[1][1]==tablero[0][2]!=0:

        return tablero[1][1]

    return 0

def jugar_humano(ficha,tablero):
    while True:
        linea=input("Jugador" + ficha2str(ficha) + ", ingresa tu jugada [x] [y] (ejemplo 1 2): ")
        coords=linea.split()
        if len(coords)==2 and coords[0].isnumeric() and coords[1].isnumeric():
            intcoords = [int(c) for c in coords]
            if 0 <= intcoords[0] <= 2 and 0 <= intcoords[1] <= 2:
                jugada=[intcoords[0],intcoords[1],ficha]
                if posible(tablero,jugada):
                    return jugada
        print("Ingresa una jugada válida!")


def realiza_jugada(tablero,jugada):
    ## jugada es una lista [i,j,ficha]
    ## retorna el tablero que resulta de aplicar la jugada en el tablero
    newtab=[list(tablero[0]),list(tablero[1]),list(tablero[2])] # newtab contiene una copia del tablero antiguo
    newtab[jugada[0]][jugada[1]]=jugada[2]
    return newtab

def posible(tablero,jugada):
    ## retorna verdadero si es posible aplicar la jugada en este tablero
    return tablero[jugada[0]][jugada[1]] == 0



def legales(tablero,ficha):
    ## retorna una lista con las jugadas legales
    lista_legales=[]
    i=0
    while i<3:
        j=0
        while j<3:
            if tablero[i][j]==0:
                lista_legales.append([i,j,ficha])
            j = j + 1
        i = i+1
    return lista_legales


tablero = [[0,0,0],[0,0,0],[0,0,0]]

while True:
    print(tablero2str(tablero))
    jugada=jugar_maquina(-1,tablero)
    print(jugada)
    tablero=realiza_jugada(tablero,jugada)
    print(tablero2str(tablero))
    if ganador(tablero)!=0:
        print("Ha ganado O")
        break
    if legales(tablero,1)==[]:
        print("Empate!")
        break
#    jugada=jugar_maquina(1,tablero)
    jugada=jugar_maquina(1,tablero)
    print(jugada)
    tablero=realiza_jugada(tablero,jugada)
    print(tablero2str(tablero))
    if ganador(tablero)!=0:
        print("Ha ganado X")
        break
    if legales(tablero,-1)==[]:
        print("Empate!")
        break
