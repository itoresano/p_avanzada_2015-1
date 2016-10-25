__author__ = 'Ignacio'
import simpy
import random
import cargar_archivos
from collections import deque
from functools import reduce
from collections import OrderedDict

# se cargan los diferentes archivos
client = input("ingrese el nombre del archivo que contiene la info de clientes")
product = input("ingrese el nombre del archivo que contiene la info de productos")
cajas_1 = input("ingrese el nombre del archivo que contiene la info de cajas")
clientes = cargar_archivos.clientes(client, "Parte_II")
productos = cargar_archivos.productos(product)
cajas = cargar_archivos.cajas(cajas_1)

tasa_llegadas = clientes["tasa"]
numero_pasillos = len(productos.keys())
NUM_ESTACIONAMIENTOS = int(input("Ingrese el numero de estacionamientos del supermercado"))

eventos = open("eventos_Parte_II.csv", "w")


class SuperMercado:
    id_cliente = 1
    id_caja = 1

    def __init__(self, env, ncajas, estacionamientos):
        self.abierto = True
        self.parking = simpy.PriorityResource(env, capacity=estacionamientos)  # Estacionamiento es una priorityResource
        self.cajas = []  # Lista de cajas
        self.env = env  # simpy
        for i in range(ncajas):
            self.cajas.append(Cola(env, SuperMercado.id_caja, self))  # Agregamos las cajas
            SuperMercado.id_caja += 1
        self.C = sum([len(i.cola) for i in self.cajas]) # Valor C del enunciado
        self.productos = dict() # diccionario con todos los productos y sus cantidades del super
        for i in productos:
            for j in productos[i]:
                self.productos[j] = productos[i][j]["cantidad"]
        self.tipos = dict() # Diccionario con productos y su cantidad comprada
        self.clientes = [] # Lista de Clientes
        self.ganancias = 0 # Ganancias Totales
        self.llegada_cliente = 0
        self.clientes_id = 0
        self.abre_caja = 1000000000000 # Valor muy grande para no interferir en el programa
        self.gasto = deque() # gasto por cada cliente que pasa por el super
        self.tiempo = deque() # tiempo por cada cliente que pasa por el super
        self.cola = deque() # tiempo que pasa en la cola cada cliente

    # se actualizan las probabilidades de eleccion de cajas en caso que se abran o cierren cajas
    def set_C(self):
        self.C = sum([len(i.cola) for i in self.cajas])
        for i in self.cajas:
            if sum([self.C - len(j.cola) for j in self.cajas]) > 0:
                i.probabilidad = (self.C - len(i.cola)) / sum([self.C - len(j.cola) for j in self.cajas])
            if sum([self.C - len(j.cola) for j in self.cajas]) == 0:
                i.probabilidad = 1
    # Proceso de entrada de un cliente
    def entra_cliente(self):
        while self.abierto:
            yield self.env.timeout(round(random.expovariate(1 / tasa_llegadas) + 0.5))
            self.clientes.append(Cliente(self.env, SuperMercado.id_cliente, super))
            SuperMercado.id_cliente += 1
            self.env.process(self.cerrar())
        self.env.process(self.abrir())

    def agregar_caja(self):
        self.cajas.append(Cola(self.env, SuperMercado.id_caja, self))
        SuperMercado.id_caja += 1

    def cerrar_caja(self):
        caja = min(filter(lambda x: x.abierta, [i for i in self.cajas]), key=lambda y: y.probabilidad)
        caja.abierta = False
    # Se cierra el supermercado (por alguna razon no conocida, a la hora de cerrar el super esta funcion se ejecuta
    # muchas veces
    def cerrar(self):
        # Cerramos
        if self.abierto:
            yield self.env.timeout(43200 - (self.env.now % 43200))
            self.abierto = False
            print("[SUPERMERCADO] Cierra el supermercado, Dia {0}, segundo {1}".format((self.env.now + 86400) // 86400,
                                                                                       self.env.now % 86400))
            eventos.write(
                "[SUPERMERCADO] Cierra el supermercado, Dia {0}, segundo {1}\n".format((self.env.now + 86400) // 86400,
                                                                                       self.env.now % 86400))

            # reponemos
            for i in productos:
                for j in productos[i]:
                    self.productos[j] = productos[i][j]["cantidad"]
    # Se abre el super
    def abrir(self):
        yield self.env.timeout(86400 - (self.env.now % 86400))
        self.abierto = True
        print("[SUPERMERCADO] Abre el supermercado, Dia {0}, segundo {1}".format((self.env.now + 86400) // 86400,
                                                                                 self.env.now % 86400))
        # y se vuelve al proceso de hacer entrar clientes
        env.process(self.entra_cliente())


class Cliente:
    def __init__(self, env, ide, super):
        self.super = super # el supermercado al que entra
        self.env = env #simpy
        self.id = ide # id del cliente
        self.llegada = env.now # tiempo de llegada (cuando se inicializa)
        self.tiempo_compra = 0
        self.estacionado = 0 # cuando se estaciona
        self.espera = 0
        self.tiempo_caja = 0
        self.prioridad = random.uniform(0, 3)  # Prioridad para estacionar
        self.tipo = "PREFERENCIAL" # Tipo
        print('[LLEGADA] Cliente {0}: Dia {1}, segundo {2} ha llegado al Estacionamiento'.format(self.id,
                                                                                                 (
                                                                                                 self.llegada + 86400) // 86400,
                                                                                                 self.llegada % 86400))
        eventos.write('[LLEGADA] Cliente {0}: Dia {1}, segundo {2} ha llegado al Estacionamiento\n'.format(self.id,
                                                                                                           (
                                                                                                           self.llegada + 86400) // 86400,
                                                                                                           self.llegada % 86400))
        self.monto_gasto = random.gauss(clientes[self.tipo]["media"], clientes[self.tipo]["desv"])
        self.pasillos = clientes[self.tipo]["pasillos"]
        self.productos_1 = clientes[self.tipo]["productos"]
        self.cantidad_productos = 0
        self.productos = dict()
        self.atasco = random.gauss(600, 180)
        self.env.process(self.estaciona_cliente(self.super.parking))

    # proceso para estacionarse
    def estaciona_cliente(self, res):
        entra_auto = res.request(priority=self.prioridad)
        yield entra_auto
        a = round(random.expovariate(1 / 5) + 0.5)
        yield self.env.timeout(a)
        print("[ESTACIONAMIENTO] El cliente {0} se estaciona en DIA {1}, segundo {2}".format(self.id,
                                                                                             (
                                                                                             self.env.now + 86400) // 86400,
                                                                                             self.env.now % 86400))
        self.estacionado = env.now
        self.generar_carro()
        self.env.process(self.elegir_cola())
        res.release(entra_auto)

    # generador del carro de compras, mismo metodo que en la parte_I
    def generar_carro(self):
        self.tiempo_compra = 0
        for i in self.pasillos:
            if self.monto_gasto == 0:
                break
            if round(random.random(), 1) <= self.pasillos[i]:
                self.tiempo_compra += random.randint(20, 30)
                for n in productos[i]:
                    if n in self.productos_1:
                        if round(random.random(), 1) <= self.productos_1[n]:
                            a = random.randint(1, productos[i][n]["R"])
                            if self.super.productos[n] >= a and self.monto_gasto >= a * productos[i][n]["precio"]:
                                self.productos[n] = [a, i]
                                self.cantidad_productos += a
                                self.monto_gasto -= a * productos[i][n]["precio"]
                                self.super.productos[n] -= a
                                if self.super.productos[n] == 0:
                                    print("El producto {0} se agoto".format(n))
                                    eventos.write("El producto {0} se agoto, Dia {1}, segundo {2}\n".format(n, (
                                    self.env.now + 86400) // 86400,
                                                                                                            self.env.now % 86400))
                                self.tiempo_compra += a * random.randint(5, 10)
                    else:
                        if round(random.random(), 1) <= productos[i][n]["prob"]:
                            a = random.randint(1, productos[i][n]["R"])
                            if self.super.productos[n] >= a and self.monto_gasto >= a * productos[i][n]["precio"]:
                                self.productos[n] = [a, i]
                                self.cantidad_productos += a
                                self.monto_gasto -= a * productos[i][n]["precio"]
                                self.super.productos[n] -= a
                                if self.super.productos[n] == 0:
                                    print("El producto {0} se agoto".format(n))
                                    eventos.write("El producto {0} se agoto, Dia {1}, segundo {2}\n".format(n, (
                                    self.env.now + 86400) // 86400,
                                                                                                            self.env.now % 86400))
                                self.tiempo_compra += a * random.randint(5, 10)
    # se elige la cola con mayor probabilidad, se verifica si se deben abrir o cerrar colas
    def elegir_cola(self):
        if min([len(i.cola) for i in self.super.cajas]) >= 3:
            self.super.agregar_caja()
            self.super.set_C()
            self.super.abre_caja = env.now
        if env.now - self.super.abre_caja >= 30 * 60 and min([len(i.cola) for i in self.super.cajas if i.abierta]) > 3:
            self.super.cerrar_caja()
        cola = max(filter(lambda x: x.abierta, [i for i in self.super.cajas]), key=lambda y: y.probabilidad)
        yield self.env.timeout(self.tiempo_compra)
        print("[CAJA] El Cliente {0}: entra a la cola de la caja {1} en DIA {2}, {3} s, con {4}".format(self.id,
                                                                                                        cola.ncola,
                                                                                                        (
                                                                                                        self.env.now + 86400) // 86400,
                                                                                                        self.env.now % 86400,
                                                                                                        self.productos))
        eventos.write(
            "[CAJA] El Cliente {0}: entra a la cola de la caja {1} en DIA {2}, {3} s, con {4}\n".format(self.id,
                                                                                                        cola.ncola,
                                                                                                        (
                                                                                                        self.env.now + 86400) // 86400,
                                                                                                        self.env.now % 86400,
                                                                                                        self.productos))
        self.env.process(cola.Agregar(self))


class Cola:
    def __init__(self, env, num, super):
        self.super = super
        self.probabilidad = 0
        self.ncola = num
        self.env = env
        self.cola = deque()
        self.counter = simpy.Resource(env, capacity=1) #caja de la cola
        self.tiempo = random.randint(0, 90)
        self.abierta = True
    # se agrega un cliente a la cola
    def Agregar(self, cliente):
        self.cola.append(cliente)
        with self.counter.request() as req:
            yield req
            cliente.espera = self.env.now - (cliente.tiempo_compra + cliente.estacionado)
            print(self.env.now, cliente.tiempo_compra + cliente.estacionado)
            self.super.cola.append(cliente.espera)
            yield env.timeout(self.tiempo)
            for i in cliente.productos:
                demora = cliente.productos[i][0] * 3
                yield env.timeout(demora)

                print("El cliente {0}, compra {1}, en la caja {2}. DIA {3}, {4} segundos".format(cliente.id, i,
                                                                                                 self.ncola, (
                    self.env.now + 86400) // 86400,
                                                                                                 self.env.now % 86400))
                eventos.write(
                    "El cliente {0}, compra {1}, en la caja {2}. DIA {3}, {4} segundos\n".format(cliente.id, i,
                                                                                                 self.ncola, (
                        self.env.now + 86400) // 86400,
                                                                                                 self.env.now % 86400))

            print("[SALIDA] El Cliente {0}, abandona la Caja {1}, habiendo pagado {2}. ".format(cliente.id, self.ncola,
                                                                                                sum([productos[
                                                                                                         cliente.productos[
                                                                                                             n][1]][n][
                                                                                                         "precio"] *
                                                                                                     cliente.productos[
                                                                                                         n][0] for n in
                                                                                                     cliente.productos])))
            eventos.write(
                "[SALIDA] El Cliente {0}, abandona la Caja {1}, habiendo pagado {2}\n".format(cliente.id, self.ncola,
                                                                                              sum([productos[
                                                                                                       cliente.productos[
                                                                                                           n][1]][n][
                                                                                                       "precio"] *
                                                                                                   cliente.productos[n][
                                                                                                       0] for n in
                                                                                                   cliente.productos])))
            self.super.ganancias += sum(
                [productos[cliente.productos[n][1]][n]["precio"] * cliente.productos[n][0] for n in cliente.productos])
            self.super.gasto.append(sum(
                [productos[cliente.productos[n][1]][n]["precio"] * cliente.productos[n][0] for n in cliente.productos]))
            for u in cliente.productos:
                if u not in self.super.tipos.keys():
                    self.super.tipos[u] = cliente.productos[u][0]
                if u in self.super.tipos.keys():
                    self.super.tipos[u] += cliente.productos[u][0]

            self.counter.release(req)
        self.cola.popleft()
        self.super.tiempo.append(env.now - cliente.llegada)
        self.super.clientes.remove(cliente)


env = simpy.Environment()
super = SuperMercado(env, 1, NUM_ESTACIONAMIENTOS)
env.process(super.entra_cliente())

# generador de archivos
def archivo_informe():
    informe = open("reporte_Parte_II.csv", "w")
    informe.write("[INFORME]\n")
    informe.write("-----------------------------------------------------------\n")
    informe.write("Total ganado por el supermercado: {0}\n".format(super.ganancias))
    informe.write("---------\n")
    informe.write("TOP 10 de productos comprados por tipo de cliente\n")
    top_10 = list((OrderedDict(sorted(super.tipos.items(), key=lambda x: x[1], reverse=True))))
    informe.write("TIPO: PREFERENCIAL")
    informe.write("{0}\n".format(top_10[0:10]))
    informe.write("---------\n")
    informe.write("Gasto promedio por tipo de cliente\n")
    if len(super.gasto) == 0:
        print("TIPO: PREFERENCIAL: 0\n")
    else:
        promedio_gasto = round(sum(super.gasto) / (len(super.gasto)), 2)
        informe.write("TIPO: PREFERENCIAL - {0}\n".format(promedio_gasto))
    informe.write("---------\n")
    informe.write("Tiempo promedio dentro del super mercado por tipo de cliente\n")
    if len(super.tiempo) == 0:
        informe.write("TIPO: PREFERENCIAL - 0\n)")
    else:
        promedio_dentro = round(sum(super.tiempo) / (len(super.tiempo)), 2)
        informe.write("TIPO: PREFERENCIAL - {0}\n".format(promedio_dentro))
    informe.write("---------\n")
    informe.write("Tiempo promedio en una cola por tipo de cliente\n")
    if len(super.cola) == 0:
        informe.write("TIPO PREFERENCIAL - 0\n")
    else:
        promedio_cola = round(sum(super.cola) / len(super.cola), 2)
        informe.write("TIPO: PREFERENCIAL - {0}\n".format(promedio_cola))


def archivo_clientes():
    lista_tipos = list()
    lista_tipos.append("PREFERENCIAL")
    for i in super.tipos:
        for j in productos:
            for n in productos[j]:
                if n == i:
                    pasillo = j
        lista_tipos.append(",{0}:{1}:{2}".format(i, super.tipos[i], super.tipos[i] * productos[pasillo][i]["precio"]))
    clientes = open("clientes_Parte_II.csv", "w")
    clientes.write("{0}\n".format(reduce(lambda x, y: x + y, [q for q in lista_tipos])))