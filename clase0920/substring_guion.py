def substring(s1,s2):
    # retorna True si s1 está contenido en s2
    # y False en caso contrario
    i = 0
    while i <= len(s2) - len(s1) :
        if s1 == s2[i:i+len(s1)]:
            return True
        i = i + 1
    return False

def iguales_guion(s1,s2):
    # retorna True si s1 es una palabra con guiones que
    # es "igual" a s2.
    i = 0
    while i < len(s1):
        if s1[i] != s2[i] and s1[i] != "-":
            return False
        if s1[i] == "-" and (s2[i] < 'a' or s2[i] > 'z'):
            return False
        i = i + 1
    return True


def substring_guion(s1,s2):
    # retorna True si s1 está contenido en s2
    # y False en caso contrario
    i = 0
    while i <= len(s2) - len(s1) :
        if iguales_guion(s1,s2[i:i+len(s1)]):
            return True
        i = i + 1
    return False


print(substring("arb","el arbol"))
print(substring_guion("a-b-l","el arbol"))
print(substring_guion("a-bb-l","el arbol"))
