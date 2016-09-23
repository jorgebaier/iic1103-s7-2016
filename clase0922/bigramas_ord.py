import sys
import random

class Bigramas:
    def __init__(self):
        self.bigramas=[]  # lista de bigramas
        self.nbigramas=0  # numero de bigramas

    def buscar(self,palabra):
        i = 0
        j = len(self.bigramas)-1

        while i <= j:
            mid = (i+j)//2
            if self.bigramas[mid][0] == palabra:
                return self.bigramas[mid][1]
            elif self.bigramas[mid][0] < palabra:
                i = mid + 1
            else:
                j = mid - 1
        self.bigramas.insert(i,[palabra,[]])
        return self.bigramas[i][1]


    def incrementar(self,lista,palabra):
        i=0
        while i < len(lista):
            if lista[i][0]==palabra:
                lista[i][1] = lista[i][1] + 1
                return
            i+=1
        lista.append([palabra,1])
        self.nbigramas=self.nbigramas+1
        if self.nbigramas%1000==0:
            print(".",end="")
            sys.stdout.flush()

    def agregar(self,pal1,pal2):
        lista=self.buscar(pal1)
        self.incrementar(lista,pal2)

    def caminata(self,palabra,limite):
        def sumalista(lista):
            suma=0
            for elem in lista:
                suma+=elem[1]
            return suma

        contador=0
        lista_palabras=[]
        while contador < limite:
            lista_palabras.append(palabra)
            lista=self.buscar(palabra)
            if len(lista)>0:
                total=sumalista(lista)
                rand=random.randint(0,total)
                acc=0
                i=0
                while acc + lista[i][1] < rand and i < len(lista):
                    acc = acc + lista[i][1]
                    i = i + 1
                palabra=lista[i][0]
            else:
                palabra=palabras[random.randint(0,len(self.palabras)-1)]
            contador = contador + 1
        return lista_palabras


def limpiar(palabra):
    puntuacion=".,!:;?»«-¿¡"
    respuesta=""
    for c in palabra:
        if not c in puntuacion:
            respuesta += c
    return respuesta


def cargar_archivo():
    global b;
    filename = input("Archivo con datos: ")
    f = open(filename,'r')
    print("Leyendo los datos")
    entrada=''
    for linea in f:
        linea.rstrip()
        entrada += linea

    import time
    tic1=time.time()
    print("Datos leidos. Procesando.",end="")

    f.close()
    palabras = [limpiar(x.lower()) for x in entrada.split() if x!=""]
    b=Bigramas()
    i=0
    while i < len(palabras)-1:
        b.agregar(palabras[i],palabras[i+1])
        i+=1

    tic2=time.time()
    print("\nDatos procesados en ",round(tic2-tic1,2),"seg.")
    print("Base de datos tiene",len(b.bigramas),"palabras y",b.nbigramas,"bigramas.")

#print(b.bigramas)


def palabra_comun_seguida(palabra):
    return b.caminata(palabra,2)[1]
