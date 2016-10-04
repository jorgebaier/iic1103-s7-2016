import random

class Universo:
    def __init__(self):
        self.plantas = []
        self.zombies = []

    def agregar_planta(self,planta):
        self.plantas.append(planta)

    def agregar_zombie(self,zombie):
        self.zombies.append(zombie)

    def cantidad_plantas(self):
        return len(self.plantas)

    def cantidad_zombies(self):
        return len(self.zombies)

    def print_stats(self):
        vidas_zombies = 0
        vidas_plantas = 0
        for z in self.zombies:
            vidas_zombies += z.get_salud()
        for p in self.plantas:
            vidas_plantas += p.get_salud()
        print("Plantas (",self.cantidad_plantas(),\
              ") = ",vidas_plantas,"Zombies (",\
              self.cantidad_zombies(),") = ",vidas_zombies)
    
    def round_aleatorio(self):
        indice_planta = random.randint(0,self.cantidad_plantas()-1)
        indice_zombie = random.randint(0,self.cantidad_zombies()-1)

        p = self.plantas[indice_planta]
        z = self.zombies[indice_zombie]

        moneda = random.randint(0,1)

        if moneda == 0: ## planta ataca al zombie
            z.atacado_por(p)
            print(p.get_nombre(),"ataca a",z.get_nombre())
            if z.get_salud() <= 0:
                self.zombies.pop(indice_zombie)
        else:
            p.atacado_por(z)
            print(z.get_nombre(),"ataca a",p.get_nombre())
            if p.get_salud() <= 0:
                self.plantas.pop(indice_planta)


class Zombie:
    def __init__(self,nombre,ropa=0,velocidad=0): # inicializador se usa para construir
                        # un objeto de la clase Zombie
        self.pista = 0 # define que el atributo "pista" es 0
        self.salud = 100
        self.velocidad = velocidad
        self.ropa = ropa
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre
    
    def get_salud(self):
        return self.salud
    
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
        self.salud = self.salud - 10


class Planta:
    def __init__(self,nombre):
        self.salud = 100
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def get_salud(self):
        return self.salud

    def imprimir(self):
        print("Soy una planta y me llamo",self.nombre,". Mi salud es: ",self.salud)

    def atacado_por(self, zombie):
        if zombie.get_ropa() == 0:
            self.salud = self.salud - 10
        else:
            self.salud -= 5

u = Universo()

i = 0

while i < 15:
    p = Planta("rosita "+str(i))
    u.agregar_planta(p)
    i = i + 1

i = 0
while i < 15:
    z = Zombie("zorge "+str(i))
    u.agregar_zombie(z)
    i = i + 1


u.print_stats()
while u.cantidad_plantas() > 0 and u.cantidad_zombies() > 0:
    u.round_aleatorio()
    u.print_stats()

    







