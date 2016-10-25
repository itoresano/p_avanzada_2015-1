__author__ = 'Ignacio'
# Modulo para cargar todos los archivos de texto

def itineraries(archivo):
    lista_it = list()
    it = dict()
    for line in open(archivo).read().splitlines():
        date_1 = line.split("\t")
        lista_it.append(date_1)
    for i in range(1, len(lista_it)):
        lista_it[i][1] = lista_it[i][1].split(" ")
        it[lista_it[i][0]] = {"id": lista_it[i][0], "trips": lista_it[i][1]}
    return it


def trips(archivo):
    lista_viajes = list()
    viajes = dict()
    for line in open(archivo).read().splitlines():
        date_1 = line.split("\t")
        lista_viajes.append(date_1)
    for i in range(1, len(lista_viajes)):
        viajes[lista_viajes[i][0]] = {"id": lista_viajes[i][0], "origen": lista_viajes[i][1],
                                      "destino": lista_viajes[i][2],
                                      "ruta": lista_viajes[i][3], "vehiculo": lista_viajes[i][5]}
    return viajes


def hubs(archivo):
    lista_trmnl = list()
    terminal = dict()
    for line in open(archivo).read().splitlines():
        date_1 = line.split("\t")
        lista_trmnl.append(date_1)
    for i in range(1, len(lista_trmnl)):
        if len(lista_trmnl[i]) > 1:
            terminal[lista_trmnl[i][0]] = {"id": lista_trmnl[i][0], "ciudad": lista_trmnl[i][1],
                                           "tipo": lista_trmnl[i][2], "tamaño": lista_trmnl[i][3]}
    return terminal


def cities(archivo):
    lista_city = list()
    ciudades = dict()
    for line in open(archivo).read().splitlines():
        date_1 = line.split("\t")
        lista_city.append(date_1)
    for i in range(1, len(lista_city)):
        ciudades[lista_city[i][0]] = {"ciudad": lista_city[i][0], "pais": lista_city[i][1]}
    return ciudades


def routes(archivo):
    lista_rutas = list()
    rutas = dict()
    for line in open(archivo).read().splitlines():
        date_1 = line.split("\t")
        lista_rutas.append(date_1)
    for i in range(1, len(lista_rutas)):
        rutas[lista_rutas[i][0]] = {"id": lista_rutas[i][0], "ciudad1": lista_rutas[i][1], "ciudad2": lista_rutas[i][2],
                                    "tipo": lista_rutas[i][3]}
    return rutas


def colores():
    lista_colores = ["0xFFCC00", "0x99FF00", "0xFF6699", "0x99FFFF", "0xFF6600", "0x990000", "0x00FF00", "0x33CCFF",
                     "0x33CC66", "0x009900", "0x336600", "0x003399", "0x336666", "0x0033FF", "0x999966"]
    a = set()
    aa = dict()
    b = cities("datos\\cities.txt")
    for i in b:
        a.add(b[i]["pais"])
    c = list(a)
    for j in range(len(c)):
        aa[c[j]] = lista_colores[j]
    return aa


def passengers(archivo):
    lista_psjs = list()
    for line in open(archivo).read().splitlines():
        date_1 = line.split("\t")
        lista_psjs.append(date_1[2])
    return lista_psjs


def cargo(archivo):
    lista_psjs = list()
    for line in open(archivo).read().splitlines():
        date_1 = line.split("\t")
        lista_psjs.append(date_1[0])
    return lista_psjs






