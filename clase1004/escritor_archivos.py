
nombre = input("Nombre del archivo a escribir: ")

f = open(nombre,"w")

f.write("hola"+"\n")
f.write("chao"+"\n")

f.close()
