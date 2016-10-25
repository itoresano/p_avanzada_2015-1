__author__ = 'Ignacio'

from functools import reduce

leer = list(tuple(map(lambda l : l.strip().split(";"),[line for line in open("jugadores.txt")])))
print(leer)

def se_llama_como_yo():
    mismo_nombre = list(tuple((filter(lambda x: "Ignacio José" in x or "Toresano" in x,
                                      [line for line in leer]))))
    return mismo_nombre

def chilenos_zurdos():
    chileno_zurdo = list(tuple(filter(lambda x: "Chileno" in x and "Izuquierda" in x,
                                      [line for line in leer])))
    return chileno_zurdo

def edades():
    edad = list(tuple((map(lambda x: (x[0], x[1], 2015 - int(x[-4])), [line for line in leer]))))
    return edad


def sub_17():
    sub17_1 = list(tuple(filter(lambda x: x[2] < 18,[line for line in edades()])))
    sub17 = list(tuple(map(lambda x: (x[0],x[1]),[line for line in sub17_1])))
    return sub17

def goleador():
    goleador = list(tuple(reduce(lambda x, y: min(x[8],y[9] ), [line for line in leer])))
    return goleador


if __name__ == "__main__":
    print(se_llama_como_yo())
    #print(chilenos_zurdos())
    #print(sub_17())
    #print(edades())
    #print(goleador())




