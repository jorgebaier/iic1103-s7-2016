def leer_archivo():
    nombre = input("Nombre del archivo donde está el mapa: ")
    f = open(nombre,"r")
    lineas = f.readlines()
    f.close()
    mapa = []
    ## completar

def vecinos(mapa,i,j):
    # entrega la lista de vecinos libres de la posición i,j en mapa
    ancho = len(mapa[0])
    alto = len(mapa)
    V = [[-1,0],[1,0],[0,-1],[0,1]]
    ## completar 


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
