from collections import deque
from paquete import Paquete
from botella import Botella

__author__ = 'patricio_lopez'


class Maquina:

    def procesar(self, linea_produccion_entrante):
        print("----------------------")
        print("La maquina {} comienza a trabajar.".format(
            self.__class__.__name__))


class Botellizamodulador(Maquina):

    def __init__(self):
        self.botellas_a_producir = 0

    def procesar(self, linea_produccion_entrante=None):
        super().procesar(linea_produccion_entrante)
        # ----------------
        # Completar método
        # ----------------
        self.linea_produccion_entrante = []
        for i in range(self.botellas_a_producir):
            if (len(self.linea_produccion_entrante) - 1) % 5 == 0:
                capacidad = self.linea_produccion_entrante[i - 1].litros * 2
                self.linea_produccion_entrante.append(Botella(capacidad))
            elif (len(self.linea_produccion_entrante) - 1) % 6 == 0:
                capacidad_2 = (self.linea_produccion_entrante[i - 1].litros / 2) + (botellas[i - 2].litros * 4)
                self.linea_produccion_entrante.append(Botella(capacidad_2))
            else:
                self.linea_produccion_entrante.append(Botellas(1))
        return self.linea_produccion_entrante


class LowFAT32(Maquina):

    def __init__(self):
        self.botellas_desechadas = []

    def desechar_botella(self, botella):
        self.botellas_desechadas.append(botella)

    def imprimir_botellas_desechadas(self):
        print("Se desecharon {} botellas".format(
            len(self.botellas_desechadas)))

    def procesar(self, linea_produccion_entrante):
        super().procesar(linea_produccion_entrante)
        self.linea_de_despacho=deque()
        for botella in linea_produccion_entrante:
            b=linea_produccion_entrante[0]
            linea_produccion_entrante.remove(b)
            if len(self.linea_de_despacho)!=0:
                capacidad_ultima=self.linea_de_despacho[-1].litros
                capacidad_primera=self.linea_de_despacho[0].litros
                if b.litros>=capacidad_ultima:
                    self.linea_de_despacho.append(b)
                elif b.litros<=capacidad_primera:
                    self.linea_de_despacho.appendleft(b)
                else:
                    self.desechar_botella(b)
            else:
                self.linea_de_despacho.append(b)
        self.imprimir_botellas_desechadas()
        return self.linea_de_despacho


class HashSoda9001(Maquina):

    def procesar(self, linea_produccion_entrante):
        super().procesar(linea_produccion_entrante)
        # ----------------
        # Completar método
        # ----------------
        capacidades = []

        for i in range(len(self.linea_produccion_entrante)):
            if self.linea_produccion_entrante[i].litros not in capaciades:
                capacidades.append(self.linea_produccion_entrante[i].litros)
            if self.linea_produccion_entrante[i].litros in capacidades:
                pass
        for i in range(len(capacidades)):
            pilas.append([])
            for i in range (len(self.linea_produccion_entrante)):
                for n in range (len(capacidades)):
                    if self.linea_produccion_entrante[i].litros==capacidades[n]:
                        pilas[n].append(self.linea_produccion_entrante[i])
        #esta función retorna una lista en que cada sublista es una lista con todas las botellas de la misma capacidad
        return pilas


class PackageManager(Maquina):

    def procesar(self, linea_produccion_entrante):
        paquetes = deque()
        for pila in linea_produccion_entrante.values():
            paquete = Paquete()
            paquete.agregar_botellas(pila)
            paquetes.append(paquete)
        return paquetes


class Fabrica:

    def __init__(self):
        self.botellizamodulador = Botellizamodulador()
        self.lowFAT32 = LowFAT32()
        self.hashSoda9001 = HashSoda9001()
        self.packageManager = PackageManager()

    def producir(self, numero_botellas):
        self.botellizamodulador.botellas_a_producir = numero_botellas
        producto = None
        for maquina in [self.botellizamodulador,
                        self.lowFAT32,
                        self.hashSoda9001,
                        self.packageManager]:
            producto = maquina.procesar(producto)
        return producto


if __name__ == "__main__":

    numero_botellas = 423

    fabrica = Fabrica()
    output = fabrica.producir(numero_botellas)
    print("----------------------")
    print("Para {} botellas, se producen {} paquetes".format(
        numero_botellas, len(output)))
    for paquete in output:
        paquete.ver_contenido()
    print("----------------------")

