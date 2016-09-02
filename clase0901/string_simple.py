import random

s = "esto es un string muy largo porque estoy haciendo una prueba que no se como va a funcionar, pero al menos será artistico"

#i = 0
#while i < len(s):
#    print(s[i])
#    i = i + 1


#for x in s[::2]:
#    print(x)

t = ''
for c in s:
        if c == ' ' and random.randint(1,4) <= 1:
            t = t + '\n'
        else:
            t = t + c


print(t)
