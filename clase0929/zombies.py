

class Zombie:
    def __init__(self,nombre,ropa=0,velocidad=0): # inicializador se usa para construir
                        # un objeto de la clase Zombie
        self.pista = 0 # define que el atributo "pista" es 0
        self.salud = 100
        self.velocidad = velocidad
        self.ropa = ropa
        self.nombre = nombre

    def get_ropa(self):
        return self.ropa
    
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

    def cambiar_nombre(self,nombre):
        self.nombre = nombre

    def obtener_nombre(self):
        return self.nombre

    def atacado_por(self,planta):
        self.salud = self.salud - 3


class Planta:
    def __init__(self,nombre):
        self.salud = 100
        self.nombre = nombre

    def imprimir(self):
        print("Soy una planta y me llamo",self.nombre,". Mi salud es: ",self.salud)

    def atacado_por(self, zombie):
        if zombie.get_ropa() == 0:
            self.salud = self.salud - 10
        else:
            self.salud -= 5


z = Zombie("Camila")
p = Planta("Camelia")

z.imprimir()
p.imprimir()

p.atacado_por(z)
z.atacado_por(p)

print()

z.imprimir()
p.imprimir()



#z.atacado_por(p)  # Camila fue atacada por Camelia
#p.atacado_por(z)  # Camelia fue atacada por Camila



