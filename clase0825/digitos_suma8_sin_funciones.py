









def sumacifras(numero):
    suma = 0
    while numero != 0:
        suma = suma + numero % 10
        numero = numero // 10
    return suma

N = int(input("cuanto vale N: "))

contador = 0
numero = 0
while contador < N:
    if sumacifras(numero) == 8:
        print(numero)
        contador = contador + 1
    numero = numero + 1





