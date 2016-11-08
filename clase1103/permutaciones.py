# retorna una lista con todos los strings que resultan
# de insertar c en una posición de s

def insertar(c,s):
    return [s[:i]+c+s[i:] for i in range(len(s)+1)]

def perm(s):
    if s  == '':
        return ['']
    else:
        L = []
        for t in perm(s[1:]):
            L += insertar(s[0],t)
        return L

print(perm('012'))
lista=perm('01234')
print(lista)
print(len(lista))
