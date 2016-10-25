__author__ = 'Ignacio'
from Carga import Carga
from Pasajeros import Pasajero
from Terminales import Terminal
from Rutas import Ruta
from Vehiculos import Vehiculo, Transporte_carga, Transporte_pasajeros, Avion, Barco, Crucero, Bus, Camion
from Viajes import Viaje
from Itinerarios import Itinerario

lista_cargas = []
cargas = dict()

lista_psjs = []
psjs = dict()

lista_trmnl = []
terminal = dict()

lista_rutas = []
rutas = dict()

lista_veh = []
lista_fleet = []
vehiculos = dict()

lista_viajes = []
viajes = dict()

lista_it = []
it = dict()

# Estas funciones cargan los datos entregados en los archivos de texto y los guardan en diccionarios, los cuales estan
# asociados a cada clase.
def cargar_iti(archivo):
    for line in open(archivo).read().splitlines():
        date_1 = line.split("\t")
        lista_it.append(date_1)
    for i in range(1, len(lista_it)):
        it[lista_it[i][0]] = Itinerario(id_objeto=lista_it[i][0], id_viaje=lista_it[i][1])


def cargar_viajes(archivo):
    for line in open(archivo).read().splitlines():
        date_1 = line.split("\t")
        lista_viajes.append(date_1)
    for i in range(1, len(lista_viajes)):
        viajes[lista_viajes[i][0]] = Viaje(id=lista_viajes[i][0], origen=lista_viajes[i][1], destino=lista_viajes[i][2],
                                           ruta=lista_viajes[i][3], hora_partida=lista_viajes[i][4],
                                           vehiculo=lista_viajes[i][5])


def cargar_vehiculos(archivo_fleet, archivo_models):
    for line in open(archivo_fleet).read().splitlines():
        date_1 = line.split("\t")
        lista_fleet.append(date_1)

    for line in open(archivo_models).read().splitlines():
        date_1 = line.split("\t")
        lista_veh.append(date_1)

    for line in lista_fleet:
        for linea in lista_veh:
            if line[0] == linea[0]:
                for i in range(1, len(linea)):
                    line.append(linea[i])
                if 0 < lista_veh.index(linea) < 6:
                    line.append("Avion")
                if 6 < lista_veh.index(linea) < 11:
                    line.append("CargoShip")
                if 11 < lista_veh.index(linea) < 15:
                    line.append("CruiseShip")
                if 15 < lista_veh.index(linea) < 19:
                    line.append("Bus")
                if 19 < lista_veh.index(linea):
                    line.append("Truck")

    for i in range(1, len(lista_fleet)):
        if "Avion" in lista_fleet[i]:
            vehiculos[lista_fleet[i][1]] = Avion(modelo=lista_fleet[i][0], nombre=lista_fleet[i][1],
                                                 tamaño=lista_fleet[i][2], velocidad=lista_fleet[i][3],
                                                 alcance=lista_fleet[i][4], asientos=lista_fleet[i][5],
                                                 vol_max=lista_fleet[i][6], peso_max=lista_fleet[i][7],
                                                 tipo_carga=lista_fleet[i][8], tipo="Aereo",
                                                 costo=lista_fleet[i][9])
        if "CargoShip" in lista_fleet[i]:
            vehiculos[lista_fleet[i][1]] = Barco(modelo=lista_fleet[i][0], nombre=lista_fleet[i][1],
                                                 tamaño=lista_fleet[i][2], velocidad=lista_fleet[i][3],
                                                 vol_max=lista_fleet[i][4], peso_max=lista_fleet[i][5],
                                                 tipo_carga=lista_fleet[i][6],
                                                 tipo="Acuatico", costo=lista_fleet[i][7])
        if "CruiseShip" in lista_fleet[i]:
            vehiculos[lista_fleet[i][1]] = Crucero(modelo=lista_fleet[i][0], nombre=lista_fleet[i][1],
                                                   tamaño=lista_fleet[i][2], velocidad=lista_fleet[i][3],
                                                   asientos=lista_fleet[i][4], tipo="Acuatico",
                                                   costo=float(lista_fleet[i][5]))
        if "Bus" in lista_fleet[i]:
            vehiculos[lista_fleet[i][1]] = Bus(modelo=lista_fleet[i][0], nombre=lista_fleet[i][1],
                                               tamaño=lista_fleet[i][2], velocidad=lista_fleet[i][3],
                                               asientos=lista_fleet[i][4], tipo="Terrestre",
                                               costo=lista_fleet[i][5])
        if "Truck" in lista_fleet[i]:
            vehiculos[lista_fleet[i][1]] = Camion(modelo=lista_fleet[i][0], nombre=lista_fleet[i][1],
                                                  tamaño=lista_fleet[i][2], velocidad=lista_fleet[i][3],
                                                  vol_max=lista_fleet[i][4], peso_max=lista_fleet[i][5],
                                                  tipo_carga=lista_fleet[i][6], tipo="Terrestre",
                                                  costo=lista_fleet[i][7])


def cargar_rutas(archivo):
    for line in open(archivo).read().splitlines():
        date_1 = line.split("\t")
        lista_rutas.append(date_1)
    for i in range(1, len(lista_rutas)):
        rutas[lista_rutas[i][0]] = Ruta(id=lista_rutas[i][0], ciudad1=lista_rutas[i][1], ciudad2=lista_rutas[i][2],
                                        tipo=lista_rutas[i][3], largo=lista_rutas[i][4], tamaño=lista_rutas[i][5],
                                        costo=lista_rutas[i][6])



def cargar_terminales(archivo):
    for line in open(archivo).read().splitlines():
        date_1 = line.split("\t")
        lista_trmnl.append(date_1)
    for i in range(1, len(lista_trmnl)):
        if len(lista_trmnl[i]) > 1:
            terminal[lista_trmnl[i][0]] = Terminal(code=lista_trmnl[i][0], ciudad=lista_trmnl[i][1],
                                                   tipo=lista_trmnl[i][2], tamaño=lista_trmnl[i][3])


def cargar_pasajeros(archivo):
    for line in open(archivo).read().splitlines():
        date_1 = line.split("\t")
        lista_psjs.append(date_1)
    for i in range(1, len(lista_psjs)):
        psjs[lista_psjs[i][2]] = Pasajero(nombre=lista_psjs[i][0], apellido=lista_psjs[i][1],
                                          rut=lista_psjs[i][2])


def cargar_carga(archivo):
    for line in open(archivo).read().splitlines():
        date_1 = line.split("\t")
        lista_cargas.append(date_1)
    for i in range(2, len(lista_cargas)):
        cargas[lista_cargas[i][0]] = Carga(id=lista_cargas[i][0], nombre=lista_cargas[i][1],
                                           peso=lista_cargas[i][2], volumen=lista_cargas[i][3],
                                           tipo=lista_cargas[i][4])






