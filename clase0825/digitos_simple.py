
numero = int(input("dame un numero: "))

cifras = 0

while numero // 10**cifras != 0:
    cifras = cifras + 1

i = 1
suma = 0
while i <= cifras:
    suma = suma + (numero//10**(i-1))%10
    i = i + 1

print("metodo 1 da ",suma)

suma = 0
cifras = 0
while numero != 0:
    suma = suma + numero % 10
    numero = numero // 10
    cifras = cifras + 1

print("metodo 2 da ",suma)
