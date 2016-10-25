__author__ = 'Ignacio'

import carga_de_datos as cdd
from Pasajeros import Pasajero
from check_viaje import check
from Viajes import Viaje
from Carga import Carga
from Itinerarios import Itinerario
from Rutas import Ruta
from Terminales import Terminal
from Vehiculos import Vehiculo

# Este archivo maneja las funciones para agregar agendar o cancelar objetos dentro del programa:

# La funcion agregar recibe un tipo (vehiculo, carga, viaje, pasajero) y luego recibe las caracteristicas de cada clase
# revisando si esque son validas o no.
def agregar(tipo):
    def vehiculo(iden):
        nombre = input("Ingrese el nombre del vehiculo:")
        tipo = input("Ingrese el modelo de vehiculo:")
        modelo = False
        for i in cdd.vehiculos:
            if tipo in cdd.vehiculos[i].modelo:
                modelo = True
        if modelo == False:
            print("El modelo del auto no existe. Ingrese sus datos nuevamente")
            vehiculo(None)
        a = open("fleet.txt", "a")
        a.write("{0}\t{1}\n".format(tipo, nombre))
        cdd.cargar_vehiculos("fleet.txt", "vehicle_models.txt")
        print("Vehiculo agregado exitosamente!")


    def pasajero(iden):
        name = input("Ingrese nombre:")
        last_name = input("Ingrese apellido:")
        rut = input("Ingrese Rut:")
        if rut in cdd.psjs:
            print("El rut ingresado ya existe, ingrese nuevamente")
            pasajero(None)
        a = open("passengers.txt", "a")
        a.write("{0}\t{1}\t{2}\n".format(name, last_name, rut))
        cdd.psjs[rut] = Pasajero(nombre=name, apellido=last_name, rut=rut)
        print("Pasajero agregado exitosamente!")

    def carga(iden):
        id = input("Ingrese id:")
        if id in cdd.cargas:
            print("El id ingresado ya exist, ingrese nuevamente")
            carga(None)
        name = input("Ingrese nombre:")
        weight = input("Ingrese Peso:")
        volume = input("Ingrese Volumen:")
        type = input("Ingrese tipo:")
        if type not in ["Normal", "Dangerous", "Delicate"]:
            print("El tipo de carga es incorrecto ingrese nuevamente")
            carga(None)
        a = open("cargo.txt", "a")
        a.write("{0}\t{1}\t{2}\t{3}\t{4}\n".format(id, name, weight, volume, type))
        cdd.cargas[id] = Carga(id=id, nombre=name, peso=weight, volumen=volume, tipo=type)
        print("Carga agregada exitosamente!")

    def viaje(iden):
        id = input("Ingrese id del viaje:")
        if id in cdd.viajes:
            print("El id ingresado ya existe, ingrese nuevamente")
            viaje(None)
        origen = input("Ingrese el Origen:")
        if origen not in cdd.terminal:
            print("el origen no existe. Ingrese nuevamente sus datos.")
            viaje(None)
        destino = input("Ingrese el destino:")
        if destino not in cdd.terminal:
            print("El destino no existe. Ingrese nuevamanete sus datos")
            viaje(None)
        ruta = input("Ingrese la Ruta:")
        if ruta not in cdd.rutas:
            print("La ruta no existe")
            viaje(None)
        hora_partida = input("Ingrese fecha y hora de partida (DD-MM-YY - hh:mm")
        vehiculo = input("Ingrese el vehiculo que utilizara:")
        if vehiculo not in cdd.vehiculos:
            print("El vehiculo no existe, ingrese nuevamente")
            viaje(None)
        a = open("trips.txt", "a")
        a.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\n".format(id, origen, destino, ruta, hora_partida, vehiculo))
        cdd.viajes[id] = Viaje(id=id, origen=origen, destino=destino, ruta=ruta, hora_partida=hora_partida,
                               vehiculo=vehiculo)
        print("Viaje agregado exitosamente!")

    return locals()[tipo]


# La funcion agendar, agenda viajes para cargas y pasajeros, y checkea gracias a la funcion check, si es que el viaje es
# posible de realizar o no.
def agendar(tipo):
    def carga(iden):
        viaje = input("Ingrese el/los viaje/s que desea agendar (separelos por un espacio):")
        viaje = viaje.split(" ")
        for i in viaje:
            if i not in cdd.viajes:
                print("El viaje no existe, ingrese nuevamente")
                carga(None)
        id = input("Ingrese identificador:")
        if id not in cdd.cargas:
            print("La carga no existe")
            carga(None)
        for i in viaje:
            tipo = type(cdd.vehiculos[cdd.viajes[i].vehiculo]).__name__
            if not check(tipo)(i, cdd.cargas[id].volumen, cdd.cargas[id].peso, cdd.cargas[id].tipo):
                print("No se puede trasladar la carga en este viaje")
                carga(None)
            a = open("itineraries.txt", "a")
            a.write("{0}\t{1}\n".format(i, id))
            print("El Itinerario ha sido agendado agendado exitosamente!")
            cdd.it[id] = Itinerario(id, i)

    def pasajero(iden):
        viaje = input("Ingrese el/los viaje/s que desea agendar (separelos por un espacio):")
        viaje = viaje.split(" ")
        for i in viaje:
            if i not in cdd.viajes:
                print("El viaje no existe, ingrese nuevamente")
                pasajero(None)
        id = input("Ingrese rut:")
        if id not in cdd.psjs:
            print("El pasajero no existe")
            pasajero(None)
        for i in viaje:
            tipo = type(cdd.vehiculos[cdd.viajes[i].vehiculo]).__name__
            if not check(tipo)(i, 0, 0):
                print("No se puede trasladar al pasajero en este viaje")
                pasajero(None)
            a = open("itineraries.txt", "a")
            a.write("{0}\t{1}\n".format(viaje, id))
            cdd.it[id] = Itinerario(id, i)
            print("Viaje agendado exitosamente!")

    return locals()[tipo]


# Esta funcion Cancela itinerarios creados: Reagrupa todos los itinerarios existentes en una lista, elimina el viaje ingresado
# y luego reescribe el archivo con los itinerarios restantes
def cancelar(tipo):
    def carga(iden):
        lista_cargas = list()
        id = input("Ingrese id de la carga:")
        if id not in cdd.cargas:
            print("La id ingresada no existe")
            carga(None)
        for line in open("itineraries.txt").read().splitlines():
            date_1 = line
            lista_cargas.append(date_1)
        for i in lista_cargas:
            if id in i:
                del i
        archivo = open("itineraries.txt", "w")
        for linea in lista_cargas:
            archivo.write(linea)
        print("Itinerario eliminado exitosamente")
        cdd.cargar_iti("itineraries.txt")

    def pasajero(iden):
        lista_psjs = list()
        rut = input("Ingrese rut del pasajero:")
        if rut not in cdd.psjs:
            print("El rut ingresado no existe")
            pasajero(None)
        for line in open("itineraries.txt").read().splitlines():
            date_1 = line
            lista_psjs.append(date_1)
        for i in lista_psjs:
            if rut in i:
                del i
                print("{0} sera eliminado".format(cdd.it[i]))
        archivo = open("itineraries.txt", "w")
        for linea in lista_psjs:
            archivo.write(linea)
        print("Itinerario eliminado exitosamente")
        cdd.cargar_iti("itineraries.txt")


    return locals()[tipo]














