def sumacifras(numero):
    suma = 0
    while numero != 0:
        suma = suma + numero % 10
        numero = numero // 10
    return suma

def esPrimo(n):
    divisores = 0
    i = 1
    while i <= n:
        if n%i==0:
            divisores = divisores + 1
        i = i + 1
    return divisores == 2

def esPrimo2(n):
    i = 2
    if n < 2:
        return False
    while i < n:
        if n%i==0:
            return False
        i = i + 1
    return True

    

N = int(input("cuanto vale N: "))

contador = 0
numero = 0
while contador < N:
    suma = sumacifras(numero)
    if esPrimo2(suma):
        print(numero)
        contador = contador + 1
    numero = numero + 1





