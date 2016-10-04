class Contacto:
    def __init__(self,nombre,email,direccion):
        self.nombre = nombre
        self.email = email
        self.direccion = direccion

    def get_nombre(self):
        return self.nombre

    def get_direccion(self):
        return self.direccion

    def get_email(self):
        return self.email

    def print_contacto(self):
        print("Nombre: ",self.nombre)
        print("Direccion: ",self.direccion)
        print("Email: ",self.email)

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self,c):
        self.contactos.append(c)

    def print_contactos(self):
        for c in self.contactos:
            c.print_contacto()
            print()

    def buscar_contacto(self):
        clave = input('Qué quieres buscar? ')
        for c in self.contactos:
            if clave in c.get_nombre() or clave in c.get_email() or clave in c.get_direccion():
                c.print_contacto()

def input_contacto():
    nombre = input("Nombre del contacto:")
    email = input("Email del contacto:")
    direccion = input("Direccion del contacto:")
    return Contacto(nombre,email,direccion)

def print_menu():
    print("1. Crear Contacto")
    print("2. Buscar Contacto")
    print("3. Listar Contactos")
    print("4. Salir")

a = Agenda()
while True:
    print_menu()
    opcion = input("Ingrese su opcion:")
    print("opcion",opcion,end='')
    if opcion == "1":
        c = input_contacto()
        a.agregar_contacto(c)
    elif opcion == "2":
        print("Buscar Contacto:")
        a.buscar_contacto()
    elif opcion == "3":
        print("Lista de Contactos:")
        a.print_contactos()
    elif opcion == "4":
        break
    else:
        print("Opción inválida")

