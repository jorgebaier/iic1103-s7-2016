def leer_archivo():
    nombre = input("Nombre del archivo donde está el mapa: ")
    f = open(nombre,"r")
    lineas = f.readlines()
    f.close()
    mapa = []
    for linea in lineas:
        mapa.append([c for c in linea.rstrip()])
    return mapa

def vecinos(mapa,i,j):
    # entrega la lista de vecinos libres de la posición i,j en mapa
    ancho = len(mapa[0])
    alto = len(mapa)
    V = [[-1,0],[1,0],[0,-1],[0,1]]
    return [[i+x,j+y] for [x,y] in V if 0<=i+x<alto and 0<=j+y<ancho and mapa[i+x][j+y]==' ']

def pintar_desde(mapa,i,j,letra,limite):
    # retorna un mapa en donde una region interior
    # ha sido completamente pintada con letra
    # y donde no se han usado más que limite letras para pintar
    # de no tener exito, retorna una lista vacía

    if mapa[i][j] != ' ':
        return []
    m = [list(linea) for linea in mapa]
    cola = [[i,j]]
    pintados  = 0
    while cola != []:
        vecinos_sin_pintar = []
        primero = cola.pop(0)
        i = primero[0]
        j = primero[1]
        if m[i][j] != letra:
            m[i][j] = letra
            pintados += 1
        if pintados > limite:
            return []
        for v in vecinos(m,i,j):
            x = v[0]  # x,y son las coordenadas del vecino
            y = v[1]
            if m[x][y] != letra:
                cola.append([x,y])
    if pintados <= limite:
        return m
    else:
        return []

def pretty_print(mapa):
    for linea in mapa:
        print("".join(linea))

mapa=leer_archivo()
color = input("Con qué letra pinto? ")
limite = int(input("Cuantas letras tengo? "))
total=0
listo = False

i=0
while i < len(mapa) and not listo:
    j=0
    while j < len(mapa[0]) and not listo:
        coloreado = pintar_desde(mapa,i,j,color,limite)
        if coloreado != []:
            pretty_print(coloreado)
            listo = True
        j+=1
    i+=1

if not listo:
    print("Es imposible pintar el mapa con el limite que me das :(")
