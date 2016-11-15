N=6

def pretty_print(tablero):
    for fila in tablero:
        print(" ".join([str(x) for x in fila]))
        
def caballo(i,j,tablero,cuenta):
    # i,j es la posicion del caballo
    # tablero tiene la solucion hasta el momento
    # cuenta almacena cuantas decisiones hemos tomado
    if cuenta == N**2:
        pretty_print(tablero)
        return True
    delta = [[1,2],[-1,2],[1,-2],[-1,-2],[2,1],[-2,1],[2,-1],[-2,-1]]
    for d in delta:
        nuevo_i = i + d[0]
        nuevo_j = j + d[1]
        if 0 <= nuevo_i < N and 0 <= nuevo_j < N and tablero[nuevo_i][nuevo_j] == 0:
            tablero[nuevo_i][nuevo_j] = cuenta + 1
            if caballo(nuevo_i,nuevo_j,tablero,cuenta+1):
                return True
            tablero[nuevo_i][nuevo_j] = 0
    return False

tab = []
for i in range(N):
    tab.append([0]*N)

tab[0][0] = 1
caballo(0,0,tab,1)
