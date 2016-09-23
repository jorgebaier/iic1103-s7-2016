import bigramas_ord

def leer_prohibidas():
    # retorna un string que contiene a las letras que
    # el usuario ingresa
    print("qué letras quieres omitir?")
    p = ''
    c = ''
    while  c != '0':
        c = input()
        if c != '0':
            p = p + c
    return p


def legal(prohibidas,palabra):
    # retorna True si palabra no contiene letas que
    # están en prohibidas, y False en caso contrario
    for c in prohibidas:
        if c in palabra:
            return False
    return True   


# esta una funcion bigramas_ord.cargar_archivo()
# esta es la otra funcion bigramas_ord.palabra_comun_seguida("cuando"))

bigramas_ord.cargar_archivo()
cuantas_palabras=int(input("cuantas palabras quieres: "))
prohibidas = leer_prohibidas()
inicio = input("palabra inicial: ")

print("Letras prohibidas: ",prohibidas)


cont = 0

palabra = inicio
while cont < cuantas_palabras:
    print(palabra,end=' ')
    palabra = bigramas_ord.palabra_comun_seguida(palabra)
    while not legal(prohibidas,palabra):
        palabra = bigramas_ord.palabra_comun_seguida(palabra)
    cont = cont + 1
