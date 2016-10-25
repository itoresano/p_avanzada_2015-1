__author__ = 'Ignacio'
import cargar_archivos
import random
from collections import deque
from functools import reduce
from collections import OrderedDict


client = input("ingrese el nombre del archivo que contiene la info de clientes")
product = input("ingrese el nombre del archivo que contiene la info de productos")
cajas_1 = input("ingrese el nombre del archivo que contiene la info de cajas")
clientes = cargar_archivos.clientes(client, "Parte_I")
productos = cargar_archivos.productos(product)
cajas = cargar_archivos.cajas(cajas_1)

tasa_llegadas = clientes["tasa"]
numero_pasillos = len(productos.keys())

# valor muy alto que nos permite "omitir" los valores de los eventos pasados o que estan mas adelante en la linea de
# eventos
e = 1000000000000000


class Cliente:
    def __init__(self, id, tiempo_llegada):
        self.tiempo_llegada = tiempo_llegada
        self.id = id
        self.tipos = []
        contador = 0
        for i in clientes:
            if i != "tasa":
                self.tipos.append([i])
        for i in self.tipos:
            i.append(clientes[i[0]]["peso"])
        self.numero = round(
            random.randint(0, reduce(max, list(map(lambda x: x[1], [line for line in self.tipos]))) - 1))
        self.tipos = sorted(self.tipos, key=lambda x: x[1])
        for n in self.tipos:
            if contador <= self.numero < n[1]:
                self.tipo = n[0]
                break
            else:
                contador = n[1]
        self.monto_gasto = random.gauss(clientes[self.tipo]["media"],
                                        clientes[self.tipo]["desv"])
        self.pasillos = clientes[self.tipo]["pasillos"]
        self.productos_1 = clientes[self.tipo]["productos"]
        self.tiempo_compra = e
        self.tiempo_cola = 0
        self.tiempo_compra_2 = 0
        self.tiempo_caja = e + 2
        self.tiempo_salida = e + 3
        self.cantidad_productos = 0
        self.caja = 0
        self.productos = dict()
        self.pagando = []
        self.productos_comprados = []
        self.listo = False
        self.atendido = False

    def __repr__(self):
        return "Cliente {0}, tipo: {1}".format(self.id, self.tipo)

    def set_caja(self, numero):
        self.caja = numero


class Caja:
    def __init__(self, id):
        self.tiempo_atencion = e + 12
        self.cola = deque()
        self.cliente_actual = None
        self.id = id
        self.llegada_cliente = 0
        self.atiende_cliente = 0
        self.salida_cliente = 0
        self.probabilidad = 0


    def ocupada(self):
        return self.cliente_actual is not None

    def llega_cliente(self, cliente):
        self.cola.append(cliente)
        cliente.set_caja(self.id)
        cliente.tiempo_cola = cliente.tiempo_compra
        cliente.tiempo_compra_2 = cliente.tiempo_compra
        cliente.tiempo_compra = e + 1

    def entra_cliente(self):
        self.cliente_actual = self.cola.popleft()
        self.cliente_actual.tiempo_caja = self.cliente_actual.tiempo_cola


    def calcular_tiempo_siguiente_compra(self):
        self.tiempo_atencion = self.cliente_actual.tiempo_caja
        if len(self.cliente_actual.productos) == 0:
            self.cliente_actual.atendido = True
        if len(self.cliente_actual.productos) > 0:
            if self.cliente_actual.atendido is False:
                self.tiempo_atencion += random.randint(0, 90)
                self.cliente_actual.tiempo_caja = self.tiempo_atencion
                self.cliente_actual.atendido = True
            for i in self.cliente_actual.productos:
                self.tiempo_atencion += self.cliente_actual.productos[i] * 3
                self.cliente_actual.tiempo_caja = self.tiempo_atencion
                self.cliente_actual.pagando = i
                self.cliente_actual.productos_comprados.append([i, self.cliente_actual.productos[i]])
                del self.cliente_actual.productos[i]
                break
        for i in self.cola:
            i.tiempo_cola = self.cliente_actual.tiempo_caja

    def se_va_cliente(self):
        self.cliente_actual.tiempo_salida = self.cliente_actual.tiempo_caja
        self.cliente_actual = None
        self.tiempo_atencion = e + 33

    def set_probabilidad(self, superm):
        if sum([superm.C - len(j.cola) for j in superm.cajas]) > 0:
            self.probabilidad = (superm.C - len(self.cola)) / sum([superm.C - len(j.cola) for j in superm.cajas])
        if sum([superm.C - len(j.cola) for j in superm.cajas]) == 0:
            self.probabilidad = 1


class Supermercado:
    id = 1

    def __init__(self, tiempo_max_simulacion):
        self.dia = 1
        self.abierto = True
        self.tiempo_max_simulacion = tiempo_max_simulacion
        self.cajas = []
        for i in range(cajas["cantidad"]):
            self.cajas.append(Caja(Supermercado.id))
            Supermercado.id += 1
        self.C = sum([len(i.cola) for i in self.cajas])
        for i in self.cajas:
            i.set_probabilidad(self)
        self.llegada_cliente = 0
        self.clientes_id = 0
        self.ganancias = 0
        self.clientes = deque()
        self.productos = dict()
        self.tipos = dict()
        for i in productos:
            for j in productos[i]:
                self.productos[j] = productos[i][j]["cantidad"]
        for i in clientes:
            if i != "tasa":
                self.tipos[i] = dict()
                self.tipos[i]["productos"] = dict()
                self.tipos[i]["gasto"] = list()
                self.tipos[i]["tiempo dentro"] = list()
                self.tipos[i]["tiempo colas"] = list()
        global TIEMPO_ACTUAL

    def calcular_llegada_prox_cliente(self):
        self.llegada_cliente = TIEMPO_ACTUAL + round(random.expovariate(1 / clientes["tasa"]) + 0.5)

    def calcular_tiempo_compra(self, cliente):
        cliente.tiempo_compra = cliente.tiempo_llegada
        for i in cliente.pasillos:
            if cliente.monto_gasto == 0:
                break
            if round(random.random(), 1) <= cliente.pasillos[i]:
                cliente.tiempo_compra += random.randint(20, 30)
                for n in productos[i]:
                    if n in cliente.productos_1:
                        if round(random.random(), 1) <= cliente.productos_1[n]:
                            a = random.randint(1, productos[i][n]["R"])
                            if self.productos[n] >= a and cliente.monto_gasto >= a * productos[i][n]["precio"]:
                                cliente.productos[n] = a
                                cliente.cantidad_productos += a
                                cliente.monto_gasto -= a * productos[i][n]["precio"]
                                self.productos[n] -= a
                                if self.productos[n] == 0:
                                    print("El producto {0} se agoto".format(n))
                                cliente.tiempo_compra += a * random.randint(5, 10)
                    else:
                        if round(random.random(), 1) <= productos[i][n]["prob"]:
                            a = random.randint(1, productos[i][n]["R"])
                            if self.productos[n] >= a and cliente.monto_gasto >= a * productos[i][n]["precio"]:
                                cliente.productos[n] = a
                                cliente.cantidad_productos += a
                                cliente.monto_gasto -= a * productos[i][n]["precio"]
                                self.productos[n] -= a
                                if self.productos[n] == 0:
                                    print("El producto {0} se agoto".format(n))
                                cliente.tiempo_compra += a * random.randint(5, 10)
        cliente.listo = True

    def se_va_cliente(self, cliente):
        for i in range(len(self.clientes)):
            if cliente.id == self.clientes[i].id:
                del self.clientes[i]
                break


    def get_clientes_id(self):
        self.clientes_id += 1
        return self.clientes_id

    def set_C(self):
        self.C = sum([len(i.cola) for i in self.cajas])


    def run(self):
        global TIEMPO_ACTUAL
        TIEMPO_ACTUAL = 0

        eventos = open("eventos_Parte_I.csv", "w")
        while True:
            if TIEMPO_ACTUAL % 43200 == 0 and TIEMPO_ACTUAL != 0:
                # Cierra el supermercado y se reponen los productos:
                if self.abierto:
                    self.abierto = False
                    print("[SUPERMERCADO] Se cierra el supermercado:")
                    eventos.write("[SUPERMERCADO] Se cierra el supermercado, Dia {0}, segundo {1}\n".format(self.dia,
                                                                                                            TIEMPO_ACTUAL))
                    # reponemos
                    for i in productos:
                        for j in productos[i]:
                            self.productos[j] = productos[i][j]["cantidad"]
                # Abre el supermercado
                elif not self.abierto:
                    self.abierto = True
                    print("[SUPERMERCADO] Se abre el supermercado:")
                    self.dia += 1
                    TIEMPO_ACTUAL = 0

            # Elegimos el evento mas cercano cuando el supermercado esta abierto y hay clientes dentro
            if len(self.clientes) > 0 and self.abierto:
                primero = min(43200, self.tiempo_max_simulacion, self.llegada_cliente,
                              min([i.tiempo_compra for i in self.clientes]),
                              min([o.tiempo_salida for o in self.clientes]),
                              min([n.tiempo_atencion for n in self.cajas]))
                TIEMPO_ACTUAL = primero
            # Elegimos el evento mas cercano cuando el supermercado esta cerrado y hay clientes dentro
            if len(self.clientes) > 0 and not self.abierto:
                first = min(43200 * 2, self.tiempo_max_simulacion, min([i.tiempo_compra for i in self.clientes]),
                            min([o.tiempo_salida for o in self.clientes]),
                            min([n.tiempo_atencion for n in self.cajas]))
                TIEMPO_ACTUAL = first

            # Si el super esta abierto pero no hay clientes dentro, el evento mas cercano es que llegue
            # un cliente (casi siempre)
            if self.abierto and len(self.clientes) == 0:
                self.calcular_llegada_prox_cliente()
                TIEMPO_ACTUAL = self.llegada_cliente
            if len(self.clientes) == 0 and not self.abierto:
                TIEMPO_ACTUAL = 43200 * 2

            if (self.dia - 1) * 43200 * 2 + TIEMPO_ACTUAL > self.tiempo_max_simulacion: break
            print("[SIMULACION] Tiempo de Simulacion: DIA {0}, TIEMPO {1}".format(self.dia, TIEMPO_ACTUAL))
            # Llega un cliente al super
            if TIEMPO_ACTUAL == self.llegada_cliente:
                self.clientes.append(Cliente(self.get_clientes_id(), TIEMPO_ACTUAL))
                self.calcular_tiempo_compra(self.clientes[-1])
                self.calcular_llegada_prox_cliente()
                print('[LLEGADA]Llega {0}'.format(self.clientes[-1],
                                                  self.dia, TIEMPO_ACTUAL))
                eventos.write("[LLEGADA]Llega {0}, Dia {1}, segund {2}\n".format(self.clientes[-1], self.dia,
                                                                               TIEMPO_ACTUAL))

            for i in self.clientes:
                # Un cliente termina de comprar y llega a una caja
                if TIEMPO_ACTUAL == i.tiempo_compra and i.caja is 0:
                    prob = max(self.cajas, key=lambda x: x.probabilidad)
                    print("[CAJA] El {0}, entra a la cola de la caja {1}. Productos: {2}".format(i, prob.id,
                                                                                                 i.productos))
                    eventos.write("[CAJA] El {0} entra a la cola de la caja {1}. Productos: {2}, Dia {3}, segundo{4}\n".format(i, prob.id,
                                                                                                 i.productos, self.dia, TIEMPO_ACTUAL))
                    prob.llega_cliente(i)
                    self.set_C()
                    # actualizamos las probabilidades de entrada de cada caja
                    for l in self.cajas:
                        l.set_probabilidad(self)
                    # agregamos los productos que compra cada tipo a su lista de productos para poder encontrar
                    # los productos mas vendidos.
                    for u in i.productos:
                        if u not in self.tipos[i.tipo]["productos"].keys():
                            self.tipos[i.tipo]["productos"][u] = i.productos[u]
                        if u in self.tipos[i.tipo]["productos"].keys():
                            self.tipos[i.tipo]["productos"][u] += i.productos[u]
                        break
            for i in self.clientes:
                if TIEMPO_ACTUAL == i.tiempo_salida and i.listo and i.atendido:
                    for j in i.productos_comprados:
                        for x in productos:
                            if j[0] in productos[x].keys():
                                j.append(x)
                    for u in self.cajas:
                        u.set_probabilidad(self)
                    print("[SALIDA] El {0}, abandona la Caja {1}, habiendo pagado {2}".format(i, i.caja,
                                                                                              sum([productos[
                                                                                                       n[2]][
                                                                                                       n[0]][
                                                                                                       "precio"] *
                                                                                                   n[1] for n in
                                                                                                   i.productos_comprados])))
                    eventos.write("[SALIDA] El {0} abandona la Caja {1} habiendo pagado {2}, Dia {3}, segundos {4}\n".format(i, i.caja,
                                                                                              sum([productos[
                                                                                                       n[2]][
                                                                                                       n[0]][
                                                                                                       "precio"] *
                                                                                                   n[1] for n in
                                                                                                   i.productos_comprados]), self.dia, TIEMPO_ACTUAL))
                    self.ganancias += sum([productos[n[2]][n[0]]["precio"] * n[1] for n in i.productos_comprados])
                    self.tipos[i.tipo]["gasto"].append(sum([productos[n[2]][n[0]]["precio"]
                                                            * n[1] for n in i.productos_comprados]))
                    self.tipos[i.tipo]["tiempo dentro"].append(i.tiempo_salida - i.tiempo_llegada)
                    self.tipos[i.tipo]["tiempo colas"].append(i.tiempo_cola - i.tiempo_compra_2)
                    self.se_va_cliente(i)
                    break

            for i in self.cajas:
                # cliente entra a la caja si esque esta primero en la cola y no hay nadie atendiendose
                if len(i.cola) > 0 and i.cliente_actual is None:
                    i.entra_cliente()
                    #se calcula el siguiente tiempo de compra:
                    i.calcular_tiempo_siguiente_compra()
            # un cliente en caja paga un producto
            for i in self.cajas:
                if TIEMPO_ACTUAL == i.tiempo_atencion and i.cliente_actual is not None:
                    print("[CAJA] El {0}, compra {1}, en la caja {2}".format(i.cliente_actual, i.cliente_actual.pagando,
                                                                             i.id))
                    eventos.write("[CAJA] El {0} compra {1} en la caja {2}, Dia {3}, segundo {4}\n".format(i.cliente_actual, i.cliente_actual.pagando,
                                                                             i.id, self.dia, TIEMPO_ACTUAL))
                    i.calcular_tiempo_siguiente_compra()
            for i in self.cajas:
                if TIEMPO_ACTUAL == i.tiempo_atencion and i.cliente_actual is not None:
                    if len(i.cliente_actual.productos) == 0:
                        i.se_va_cliente()

                        #----------------------------------------------------------------------------------------------------------------------

        informe = open("reporte_parte_I.csv", "w")
        informe.write("[INFORME]\n")
        informe.write("-----------------------------------------------------------\n")
        informe.write("Total ganado por el supermercado: {0}\n".format(self.ganancias))
        informe.write("---------\n")
        informe.write("TOP 10 de productos comprados por tipo de cliente\n")
        for i in self.tipos:
            top_10 = list((OrderedDict(sorted(self.tipos[i]["productos"].items(), key=lambda x: x[1], reverse=True))))
            informe.write("TIPO: {0}\n".format(i))
            informe.write("{0}\n".format(top_10[0:10]))
            informe.write("--\n")
        informe.write("---------\n")
        informe.write("Gasto promedio por tipo de cliente\n")
        for j in self.tipos:
            if len(self.tipos[j]["gasto"]) == 0:
                print("TIPO: {0} - 0\n".format(j))
            else:
                promedio_gasto = round(sum(self.tipos[j]["gasto"]) / (len(self.tipos[j]["gasto"])), 2)
                informe.write("TIPO: {0} - {1}\n".format(j, promedio_gasto))
        informe.write("---------\n")
        informe.write("Tiempo promedio dentro del super mercado por tipo de cliente\n")
        for k in self.tipos:
            if len(self.tipos[k]["tiempo dentro"]) == 0:
                informe.write("TIPO: {0} - 0\n".format(k))
            else:
                promedio_dentro = round(sum(self.tipos[k]["tiempo dentro"]) / len(self.tipos[k]["tiempo dentro"]), 2)
                informe.write("TIPO: {0} - {1}\n".format(k, promedio_dentro))
        informe.write("---------\n")
        informe.write("Tiempo promedio en una cola por tipo de cliente\n")
        for l in self.tipos:
            if len(self.tipos[l]["tiempo colas"]) == 0:
                informe.write("TIPO {0} - 0\n".format(l))
            else:
                promedio_cola = round(sum(self.tipos[l]["tiempo colas"]) / len(self.tipos[l]["tiempo colas"]), 2)
                informe.write("TIPO: {0} - {1}\n".format(l, promedio_cola))
        lista_tipos = list()
        contador_tipos = 0
        for m in self.tipos:
            lista_tipos.append([m])
            for n in self.tipos[m]["productos"]:
                for j in productos:
                    if n in productos[j].keys():
                        pasillo = j
                lista_tipos[contador_tipos].append(",{0}:{1}:{2}".format(n, self.tipos[m]["productos"][n],
                                                        self.tipos[m]["productos"][n]*productos[pasillo][n]["precio"]))
            contador_tipos += 1
        clientes = open("clientes_Parte_I.csv", "w")
        for p in lista_tipos:
            clientes.write("{0}\n".format(reduce(lambda x,y:x+y,[q for q in p])))
















