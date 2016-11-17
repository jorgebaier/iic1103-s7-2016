import os
import time
class Vector:
	def __init__(self,x,y):
		self.x=x
		self.y=y

	def __add__(self,v):
		return Vector(self.x+v.x,self.y+v.y)

	def __eq__(self,v):
		return self.x==v.x and self.y==v.y

	def __str__(self):
		return "(" + str(self.x) + ","+ str(self.y) + ")"

class Laberinto:

	def __init__(self, path):
		self.leer(path)
		self.busca_robot()
		self.visitados=[]


	def imprimir(self):
		for fila in self.lab:
			print(''.join(fila))


	def leer(self, path):
		archivo = open(path,"r")
		self.lab = []
		for linea in archivo:
			lab_linea = []
			for c in linea.rstrip('\n'):
				lab_linea.append(c)
			self.lab.append(lab_linea)
		archivo.close()

	def busca_robot(self):
		for i in range(len(self.lab)):
			for j in range(len(self.lab[i])):
				if self.lab[i][j] == '+':
					self.pos = Vector(i,j)

	def movimientos(self):
		desp=[Vector(-1,0),Vector(1,0),Vector(0,-1),Vector(0,1)]
		movs=[]
		for d in desp:
			nueva_pos=self.pos+d
			if self.lab[nueva_pos.x][nueva_pos.y]!='x' and not nueva_pos in self.visitados:
				movs.append(nueva_pos)
		return movs

	def marcar_ruta(self):
		for v in self.visitados:
			os.system('clear')
			if self.lab[v.x][v.y]!='g':
				self.lab[v.x][v.y]='*'
				self.imprimir()
				time.sleep(0.3)

	def resolver(self):
                if self.lab[self.pos.x][self.pos.y]=='o':
                        self.marcar_ruta()
                        return True
                for m in self.movimientos():
                        if m not in self.visitados:
                                self.visitados.append(m)
                                posicion_original = self.pos
                                self.pos = m
                                if self.resolver():
                                        return True
                        self.visitados.pop()
                        self.pos = posicion_original
                return False

	def resolver_optimo(self,i,limite):
                if self.lab[self.pos.x][self.pos.y]=='o':
                        self.marcar_ruta()
                        return True
                if i > limite:
                        return False
                for m in self.movimientos():
                        if m not in self.visitados:
                                self.visitados.append(m)
                                posicion_original = self.pos
                                self.pos = m
                                if self.resolver_optimo(i+1,limite):
                                        return True
                        self.visitados.pop()
                        self.pos = posicion_original
                return False

# Código principal
lab = Laberinto('maze_3.txt')
lab.imprimir()
#lab.resolver()
for lim in range(10000):
        if lab.resolver_optimo(0,lim):
                break
        

