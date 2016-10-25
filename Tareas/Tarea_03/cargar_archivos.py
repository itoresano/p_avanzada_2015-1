__author__ = 'Ignacio'


def clientes(archivo, parte):
    clientes = dict()
    lista_2 = open(archivo, "r").read().split("$")
    for i in range(len(lista_2)):
        lista_2[i] = lista_2[i].split("-")
    for i in lista_2:
        for j in range(len(i)):
            i[j] = i[j].split("\n")
    a = int(lista_2[0][0].pop(0))
    for k in lista_2:
        for l in k:
            for m in l:
                if m == "":
                    lista_2[lista_2.index(k)][k.index(l)].pop(l.index(m))
    for k in lista_2:
        for l in k:
            for i in range(len(l)):
                l[i] = l[i].split(" # ")
    b = 0
    if parte == "Parte_I":
        for i in lista_2:
            if i[0][0][0] != "PREFERENCIAL":
                clientes[i[0][0][0]] = {"peso": b + int(i[0][0][1]), "media": int(i[0][0][2]), "desv": int(i[0][0][3]),
                                        "pasillos": {}, "productos": {}}
                b += int(i[0][0][1])
                for j in range(int(i[0][0][4])):
                    clientes[i[0][0][0]]["pasillos"][i[0][j + 1][0]] = float(i[0][j + 1][1])
                for k in range(int(i[0][0][5])):
                    clientes[i[0][0][0]]["productos"][i[1][k][0]] = float(i[1][k][1])
    if parte == "Parte_II":
        for i in lista_2:
            if i[0][0][0] == "PREFERENCIAL":
                clientes[i[0][0][0]] = {"peso": b + int(i[0][0][1]), "media": int(i[0][0][2]), "desv": int(i[0][0][3]),
                                        "pasillos": {}, "productos": {}}
                b += int(i[0][0][1])
                for j in range(int(i[0][0][4])):
                    clientes[i[0][0][0]]["pasillos"][i[0][j + 1][0]] = float(i[0][j + 1][1])
                for k in range(int(i[0][0][5])):
                    clientes[i[0][0][0]]["productos"][i[1][k][0]] = float(i[1][k][1])

    clientes["tasa"] = a
    return clientes


def productos(archivo):
    productos = dict()
    lista_2 = open(archivo, "r").read().split("$")
    for i in range(len(lista_2)):
        lista_2[i] = lista_2[i].split("\n")
    for k in lista_2:
        for m in k:
            if m == "":
                lista_2[lista_2.index(k)].pop(k.index(m))
    for i in lista_2:
        for j in range(len(i)):
            i[j] = i[j].split(" # ")
    for i in lista_2:
        productos[i[0][0]] = dict()
        for j in range(int(i[0][1])):
            productos[i[0][0]][i[j + 1][0]] = {"cantidad": int(i[j + 1][1]), "precio": int(i[j + 1][2]),
                                               "R": int(i[j + 1][3]),
                                               "prob": float(i[j + 1][4])}
    return productos


def cajas(archivo):
    cajas = dict()
    lista_2 = open(archivo, "r").read().split("\n")
    for i in range(len(lista_2)):
        lista_2[i] = lista_2[i].split(" # ")
    cajas["cantidad"] = int(lista_2[0][0])
    cajas["cantidad_productos"] = int(lista_2[0][1])
    lista_2.pop(0)
    for i in lista_2:
        cajas[i[0]] = {"cantidad": int(i[1]), "precio": int(i[2]), "R": int(i[3]), "prob": float(i[4])}

    return cajas














