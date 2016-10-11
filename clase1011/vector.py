
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def suma(self, v):
        v = Vector(self.x + v.x, self.y + v.y)
        return v


#    def sum(self, v):
#        self.x = self.x+v.x
#        self.y = self.y+v.y


    def mostrar_vector(self):
        s="("+str(self.x)+","+str(self.y)+")"
        print(s)

    def __mul__(self,c):
        return Vector(self.x*c,self.y*c)

    def __rmul__(self,c):
        return Vector(self.x*c,self.y*c)
    
    def __add__(self, v):
        v = Vector(self.x + v.x, self.y + v.y)
        return v

    def __str__(self):
        s="("+str(self.x)+","+str(self.y)+")"
        return s

    def __eq__(self,v):
        return self.x == v.x and self.y == v.y

v1 = Vector(3,4)
v2 = Vector(5,1)
v3 = Vector(-3,1)

print(v1)
print(v2)
print(v3)
#v1.mostrar_vector()
#v2.mostrar_vector()
#v3.mostrar_vector()
#v = v1.suma(v2).suma(v3)    # v = v1 + v2 + v3
v = v1 + v2 + v3
print(v)
#v = v*-1
v = -1*v
print(v)

v4=Vector(-5,-6)
print(v4)

if v == v4:
    print("son iguales")
else:
    print("son distintos")
    

