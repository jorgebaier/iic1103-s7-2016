def encriptarLetra(letra):
    return chr(ord(letra)+1)

def encriptar(mensaje):
    t = ''
    for c in mensaje:
        t = t + encriptarLetra(c)
    return t

def desencriptarLetra(letra):
    return chr(ord(letra)-1)

def desencriptar(mensaje):
    t = ''
    for c in mensaje:
        t = t + desencriptarLetra(c)
    return t


def rot13c(letra):
    if "A" <= letra <= "Z":
        return chr((ord(letra)-ord('A')+13)%26 + ord('A'))
    elif "a" <= letra <= "z":
        return chr((ord(letra)-ord('a')+13)%26 + ord('a'))
    else:
        return letra

def rot13(mensaje):
    t = ''
    for c in mensaje:
        t = t + rot13c(c)
    return t
    
m="Este es un mensaje muy secreto. No quiero que nadie lo entienda."
m2=rot13(m)
m3=rot13(m2)

print(m)
print(m2)
print(m3)



print(encriptarLetra('h'))
