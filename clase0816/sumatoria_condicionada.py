







limite_inferior = int(input("cual es el limite inferior?"))
contador = limite_inferior
suma = 0
limite_superior = int(input("cual es el limite superior?"))

if limite_superior < limite_inferior:
    print("El limite superior no debe ser menor que el inferior")
else:
    while contador <= limite_superior:
        unidades = contador%10
        centenas = (contador//100)%10
        if (unidades + centenas) % 2 == 0:
            suma =  suma + contador
        contador = contador + 1
    print("La suma entre",limite_inferior,"y",limite_superior, "es", suma)




