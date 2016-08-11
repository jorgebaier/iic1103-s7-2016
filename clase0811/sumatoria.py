







limite_inferior = int(input("cual es el limite inferior?"))
contador = limite_inferior
suma = 0
limite = int(input("cual es el limite superior?"))
while contador <= limite:
    suma =  suma + contador
    contador = contador + 1
print("La suma entre",limite_inferior,"y",limite, "es", suma)

