__author__ = 'Ignacio'
from Carga import Carga
from Pasajeros import Pasajero
from Terminales import Terminal
from Rutas import Ruta
from Vehiculos import Vehiculo, Transporte_carga, Transporte_pasajeros, Avion, Barco, Crucero, Bus, Camion
from Viajes import Viaje
from Itinerarios import Itinerario
import carga_de_datos as cdd
import agregar_datos as ad


class Menu:
    def __init__(self):
        self.opciones = {"1": self.display_agregar,
                         "2": self.display_propiedades,
                         "3": self.display_datos,
                         "4": self.display_distancia,
                         "5": self.display_pasajes
        }

    # Menu
    def display_menu(self):
        print("""
              Menu
                1: Agregar Datos:
                2: Imprimir Atributos:
                3: Imprimir Estado de Persona, Carga o Vehiculo dada una fecha y hora:
                4: Calcular distancia recorrida, dada una fecha y hora.
                5: Imprimir pasajes de un objeto.
              """)

    #Run
    def run(self):
        while True:
            self.display_menu()
            eleccion = input("Ingrese Opcion: ")
            accion = self.opciones.get(eleccion)
            if accion:
                accion()
            else:
                print("{0} no es valido como opcion, ingrese nuevamente".format(eleccion))

    # Aca deberia haber una funcion que pregunta por un objeto y dada una fecha y hora, calcula la distancia recorrida
    # por el objeto. Pero no tuve el tiempo suficiente para programar aquella funcion...
    def display_distancia(self):
        pass
    #Aca deberia estar el algoritmo que retorna la ruta mas corta segun el parametro que se le asigna. La funcion
    # crearia un arbol con rutas, y recorreria el arbol hasta encontrar la ruta mas corta.
    def display_ruta_mas_corta(self, parametro):
        pass

    #esta funcion retorna para cada objeto, el metodo __str__  de su clase, menos en el caso del vehiculo
    #que era mas comodo mostrarlo como un diccionario
    def print_propiedades(self, tipo):
        def vehiculo(iden):
            return cdd.vehiculos[iden].__dict__

        def ruta(iden):
            return print(cdd.rutas[iden])

        def pasajero(iden):
            return print(cdd.psjs[iden])

        def carga(iden):
            return print(cdd.cargas[iden])

        def viaje(iden):
            return print(cdd.viajes[iden])

        return locals()[tipo]

    #Esta funcion pregunta los parametros de lo que se quiere encontrar en la consola y ejecuta la funcion
    # encontrar_posicion. Tambien
    def display_datos(self):
        try:
            tipo = input("Ingrese el tipo de objeto del cual desea conocer el estado (persona carga o vehiculo): ")
            objeto = input("Ingrese su identificador")
            fecha = input("Ingrese fecha (DD-MM-YYYY)")
            hora = input("Ingrese Hora (mm:hh)")
            self.encontrar_posicion(tipo, objeto)(fecha, hora)
        except KeyError:
            print("Error en el identificador/tipo: Ingrese su consulta nuevamente")
        except ValueError:
            print("Error en la fecha/hora: Ingrese su consulta nuevamente")
        except TypeError:
            print("Error: Ingrese su consulta nuevamente")
        except IndexError:
            print("Error en la fecha/hora: Ingrese su consulta nuevamente")

    #Esta funcion encuentra la posicion de un objeto dada la fecha y hora, lo que hace es que pasa a horas, todas las
    # fechas de los viajes del objeto y las compara con la fecha y hora preguntada por el usuario, el valor minimo
    #positivo corresponde al viaje, o ruta, en el que se encuentra el objeto dado.
    # Tambien retorna un terminal si esque el objeto ya finalizo su itinerario
    def encontrar_posicion(self, tipo, iden):

        if tipo == "persona" or tipo == "carga":
            viaje = cdd.it[iden].id_viaje
            viaje = viaje.split(" ")
        if tipo == "vehiculo":
            viaje = []
        for i in cdd.viajes:
            if cdd.viajes[i].vehiculo == iden:
                viaje.append(cdd.viajes[i].id)

        def persona_carga_vehiculo(fecha, hora):

            fecha = fecha.split("-")
            hora = hora.split(":")
            f_h_original = [[fecha[0], fecha[1], fecha[2]], [[hora[0], hora[1]]]]
            f_h_trip = []
            dif = []
            for i in viaje:
                a = cdd.viajes[i].hora_partida.split(" - ")
                b = a[0].split("/")
                a[0] = b
                c = a[1].split(":")
                a[1] = c
                f_h_trip.append(a)

            for i in range(len(f_h_trip)):
                dif.append([int(f_h_original[0][0]) - int(f_h_trip[i][0][0]),
                            int(f_h_original[0][1]) - int(f_h_trip[i][0][1]),
                            int(f_h_original[0][2]) - int(f_h_trip[i][0][2]),
                            int(f_h_original[1][0][0]) - int(f_h_trip[i][1][0]),
                            int(f_h_original[1][0][1]) - int(f_h_trip[i][1][1])])

            for i in range(len(dif)):
                dif[i] = int(dif[i][0]) * 24 + int(dif[i][1]) * 24 * 31 + int(dif[i][2]) * 24 * 365 + int(
                    dif[i][3]) + int(
                    dif[i][4]) / 60
                if dif[i] < 0:
                    dif[i] = None
            n = dif.index(min(dif))
            if int(cdd.rutas[cdd.viajes[viaje[n]].ruta].largo) / int(
                    cdd.vehiculos[cdd.viajes[viaje[n]].vehiculo].velocidad) < \
                    dif[n]:
                return cdd.viajes[viaje[n]].destino
            else:
                return cdd.viajes[viaje[n]]

        def vehiculo(fecha, hora):
            viaje = []
            contenido = []
            for i in cdd.viajes:
                if cdd.viajes[i].vehiculo == iden:
                    viaje.append(cdd.viajes[i].id)
            a = persona_carga_vehiculo(fecha, hora)
            if a in cdd.viajes:
                for i in cdd.it:
                    if a.id in cdd.it[i].id_viaje:
                        contenido.append(cdd.it[i].id_objeto)
                return print("El vehiculo se encuentra en la ruta: {0}. Su contenido es: {1}".format(a.id, contenido))
            elif cdd.terminal[a] in cdd.terminal.values():
                return print("El vehiculo ha llegado a su destino: {0} Terminal, de {1}".format(cdd.terminal[a].tipo,
                                                                                                cdd.terminal[a].ciudad))

        def carga(fecha, hora):
            c = persona_carga_vehiculo(fecha, hora)
            if c in cdd.viajes:
                return print("La carga se encuentra en la ruta: {0}".format(c.id))
            if cdd.terminal[c] in cdd.terminal.values():
                return print("La carga ha llegado a su destino: {0} Terminal, de {1}".format(cdd.terminal[c].tipo,
                                                                                             cdd.terminal[c].ciudad))

        def persona(fecha, hora):
            c = persona_carga_vehiculo(fecha, hora)
            if c in cdd.viajes.values():
                return print("La persona se encuentra en la ruta: {0}".format(c.id))
            if cdd.terminal[c] in cdd.terminal.values():
                return print("La persona ha llegado a su destino: {0} Terminal, de {1}".format(cdd.terminal[c].tipo,
                                                                                               cdd.terminal[c].ciudad))

        return locals()[tipo]

    #Esta funcion llama al metodo agregar/agendar/cancelar del archivo agregar_datos y crea objetos, agenda itnerarios
    # y cancela viajes.
    def display_agregar(self):

        tipo = input("""Ingrese:
                     ""crear"" si desea crear nuevos vehiculos, pasajeros, carga y viajes
                     ""agendar"" si desea agendar nuevos viajes a itinerarios.
                     ""cancelar"" si desea cancelar los pasajes agendado a un objeto.
                        :""")
        if tipo == "crear":
            try:
                objeto = input("Ingrese lo que desea crear (vehiculo, pasajero, carga o viajes):")
                iden = None
                ad.agregar(objeto)(iden)
            except KeyError:
                print("KeyError en el identificador/tipo: Ingrese su consulta nuevamente")
            except ValueError:
                print("ValueError en el identificador/tipo: Ingrese su consulta nuevamente")
            except TypeError:
                print("TypeError: Ingrese su consulta nuevamente")
            except IndexError:
                print("IndexError en identificador/tipo: Ingrese su consulta nuevamente")

        if tipo == "agendar":
            try:
                objeto = input("Ingrese a lo que desea agendar su viaje (pasajero o carga):")
                iden = None
                ad.agendar(objeto)(iden)
            except KeyError:
                print("KeyError en el identificador/tipo: Ingrese su consulta nuevamente")
            except ValueError:
                print("ValueError en el identificador/tipo: Ingrese su consulta nuevamente")
            except TypeError:
                print("TypeError: Ingrese su consulta nuevamente")
            except IndexError:
                print("IndexError en identificador/tipo: Ingrese su consulta nuevamente")

        if tipo == "cancelar":
            try:
                carga_pasajero = input("Ingrese si desea cancelar el pasaje de una carga o un pasajero:")
                iden = None
                ad.cancelar(carga_pasajero)(iden)
            except KeyError:
                print("KeyError en el identificador/tipo: Ingrese su consulta nuevamente")
            except ValueError:
                print("ValueError en el identificador/tipo: Ingrese su consulta nuevamente")
            except TypeError:
                print("TypeError: Ingrese su consulta nuevamente")
            except IndexError:
                print("IndexError en identificador/tipo: Ingrese su consulta nuevamente")

    #Esta funcion llama al metodo print_propiedades que imprime los atributos de cada clase.
    def display_propiedades(self):
        try:
            tipo = input("Ingrese el Tipo (vehiculo, ruta, pasajero, carga o viaje): ")
            identificador = input("Ingrese identificador:")
            self.print_propiedades(tipo)(identificador)
        except KeyError:
            print("KeyError en el identificador/tipo: Ingrese su consulta nuevamente")
        except ValueError:
            print("ValueError en el identificador/tipo: Ingrese su consulta nuevamente")
        except TypeError:
            print("TypeError: Ingrese su consulta nuevamente")
        except IndexError:
            print("IndexError en identificador/tipo: Ingrese su consulta nuevamente")

    #Esta funcion llama al metodo print_pasajes que imprime todos los pasajes de un pasajero/carga
    def display_pasajes(self):
        try:
            tipo = input("Ingrese el Tipo (pasajero o carga): ")
            identificador = input("Ingrese identificador:")
            self.print_pasajes(tipo)(identificador)
        except KeyError:
            print("KeyError en el identificador/tipo: Ingrese su consulta nuevamente")
        except ValueError:
            print("ValueError en el identificador/tipo: Ingrese su consulta nuevamente")
        except TypeError:
            print("TypeError: Ingrese su consulta nuevamente")
        except IndexError:
            print("IndexError en identificador/tipo: Ingrese su consulta nuevamente")

    #Esta funcion Imprime los atributos de los viajes de un pasajero o carga y calcula el largo (en horas) del viaje y su costo,
    #el largo lo calcula dividiendo el largo de la ruta por la velocidad del auto, y luego eso se lo suma a la
    # fecha de partida del viaje
    def print_pasajes(self, tipo):

        def pasajero(rut):
            viajes = cdd.it[rut].id_viaje
            viajes = viajes.split(" ")
            for i in viajes:
                duracion = int(cdd.rutas[cdd.viajes[i].ruta].largo) / int(
                    cdd.vehiculos[cdd.viajes[i].vehiculo].velocidad)
                duracion_formato = [duracion // 24, (duracion % 24) // 1,
                                    (
                                    (duracion - 24 * (duracion // 24)) - (duracion - 24 * (duracion // 24)) // 1 ) * 60]
                fecha_hora = cdd.viajes[i].hora_partida.split(" - ")
                fecha_hora[0] = fecha_hora[0].split("/")
                fecha_hora[1] = fecha_hora[1].split(":")
                for n in range(3):
                    fecha_hora[0][n] = float(fecha_hora[0][n])
                for n in range(2):
                    fecha_hora[1][n] = float(fecha_hora[1][n])
                fecha_hora[1][1] += duracion_formato[2]
                if fecha_hora[1][1] >= 60:
                    fecha_hora[1][0] += 1
                    fecha_hora[1][1] -= 60
                if fecha_hora[1][0] >= 24:
                    fecha_hora[0][0] += 1
                    fecha_hora[1][0] -= 24
                if fecha_hora[0][0] > 31:
                    fecha_hora[0][1] += 1
                    fecha_hora[0][0] -= 31
                fecha_hora[1][0] += duracion_formato[1]
                if fecha_hora[1][0] >= 24:
                    fecha_hora[0][0] += 1
                    fecha_hora[1][0] -= 24
                if fecha_hora[0][0] > 31:
                    fecha_hora[0][1] += 1
                    fecha_hora[0][0] -= 31
                fecha_hora[0][0] += duracion_formato[0]
                if fecha_hora[0][0] > 31:
                    fecha_hora[0][1] += 1
                    fecha_hora[0][0] -= 31
                fecha_final = "{0}/{1}/{2} - {3}:{4}".format(fecha_hora[0][0] // 1, fecha_hora[0][1] // 1,
                                                             fecha_hora[0][2] // 1,
                                                             fecha_hora[1][0] // 1, fecha_hora[1][1] // 1)
                costo = (
                    float(cdd.rutas[cdd.viajes[i].ruta].largo) * float(cdd.rutas[cdd.viajes[i].ruta].costo) * float(
                        cdd.vehiculos[cdd.viajes[i].vehiculo].costo))
                print(cdd.viajes[i]), print(" - Hora de llegada: {0} - Costo: {1}".format(fecha_final, costo))

        def carga(rut):
            viajes = cdd.it[rut].id_viaje
            viajes = viajes.split(" ")
            for i in viajes:
                duracion = int(cdd.rutas[cdd.viajes[i].ruta].largo) / int(
                    cdd.vehiculos[cdd.viajes[i].vehiculo].velocidad)
                print(duracion)
                duracion_formato = [duracion // 24, (duracion % 24) // 1,
                                    (
                                    (duracion - 24 * (duracion // 24)) - (duracion - 24 * (duracion // 24)) // 1 ) * 60]
                print(duracion_formato)
                fecha_hora = cdd.viajes[i].hora_partida.split(" - ")
                fecha_hora[0] = fecha_hora[0].split("/")
                fecha_hora[1] = fecha_hora[1].split(":")
                for n in range(3):
                    fecha_hora[0][n] = float(fecha_hora[0][n])
                for n in range(2):
                    fecha_hora[1][n] = float(fecha_hora[1][n])
                fecha_hora[1][1] += duracion_formato[2]
                if fecha_hora[1][1] >= 60:
                    fecha_hora[1][0] += 1
                    fecha_hora[1][1] -= 60
                if fecha_hora[1][0] >= 24:
                    fecha_hora[0][0] += 1
                    fecha_hora[1][0] -= 24
                if fecha_hora[0][0] > 31:
                    fecha_hora[0][1] += 1
                    fecha_hora[0][0] -= 31
                fecha_hora[1][0] += duracion_formato[1]
                if fecha_hora[1][0] >= 24:
                    fecha_hora[0][0] += 1
                    fecha_hora[1][0] -= 24
                if fecha_hora[0][0] > 31:
                    fecha_hora[0][1] += 1
                    fecha_hora[0][0] -= 31
                fecha_hora[0][0] += duracion_formato[0]
                if fecha_hora[0][0] > 31:
                    fecha_hora[0][1] += 1
                    fecha_hora[0][0] -= 31
                fecha_final = "{0}/{1}/{2} - {3}:{4}".format(fecha_hora[0][0] // 1, fecha_hora[0][1] // 1,
                                                             fecha_hora[0][2] // 1,
                                                             fecha_hora[1][0] // 1, fecha_hora[1][1] // 1)
                costo = (
                            float(cdd.rutas[cdd.viajes[i].ruta].largo) * float(
                                cdd.rutas[cdd.viajes[i].ruta].costo) * float(
                                cdd.vehiculos[cdd.viajes[i].vehiculo].costo)) * float(
                    max(float(cdd.cargas[rut].peso) / 100, float(cdd.cargas[rut].volumen)))
                print(cdd.viajes[i]), print(" - Hora de llegada: {0} - Costo: {1}".format(fecha_final, costo))


        return locals()[tipo]

# Consola
if __name__ == "__main__":
    cdd.cargar_carga("cargo.txt")
    cdd.cargar_iti("itineraries.txt")
    cdd.cargar_pasajeros("passengers.txt")
    cdd.cargar_rutas("routes.txt")
    cdd.cargar_terminales("hubs.txt")
    cdd.cargar_vehiculos("fleet.txt", "vehicle_models.txt")
    cdd.cargar_viajes("trips.txt")
    Menu().run()













