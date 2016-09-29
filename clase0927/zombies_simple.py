

class Zombie:
    def __init__(self,nombre): # inicializador se usa para construir
                        # un objeto de la clase Zombie
        self.pista = 0 # define que el atributo "pista" es 0
        self.salud = 100
        self.velocidad = 0
        self.ropa = 0
        self.nombre = nombre
        
    def cambiar_ropa(self, nueva_ropa):
        self.ropa = nueva_ropa

    def imprimir(self):
        if self.ropa == 0:
            str_ropa = "abrigo"
        elif self.ropa == 1:
            str_ropa = "traje"
        else:
            str_ropa = "traje de baño"
        print("Hola, soy zombie", self.nombre,". Estoy usando", str_ropa, "Tengo salud", self.salud)
        


z1 = Zombie("Jorge") # construye ("crea") un objeto de tipo zombie
             # y lo almacena en z

z2 = Zombie("Camila")

z1.imprimir()
z2.imprimir()
z1.cambiar_ropa(1)
z1.imprimir()
z2.imprimir()
