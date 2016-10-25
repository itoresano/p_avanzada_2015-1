__author__ = "Ignacio"

from interfaz import Interfaz
from Subgrilla import Subgrilla
from Ubicacion import Ubicacion
import carga_matrices


def cargar_matriz(archivo):
    array = list(list(map(lambda l: l.strip().split("], ["), [line for line in open(archivo, encoding='utf8')])))
    quitar_tipo = lambda l: l[1]
    array = quitar_tipo(array)
    array = list(list(map(lambda l: l.strip("[").strip("]").split(", "), [line for line in array])))
    return array


nivel_1 = cargar_matriz("continentes.txt")
nivel_2 = cargar_matriz("paises.txt")
nivel_3 = cargar_matriz("ciudades.txt")
nivel_4 = cargar_matriz("comunas.txt")
nivel_5 = cargar_matriz("calles.txt")
nivel_6 = cargar_matriz("tipos.txt")

zoom_1 = {"Continente": nivel_1, "Pais": nivel_2, "Ciudad": nivel_3, "Comuna": nivel_4, "Calle": nivel_5}
zoom = {1: nivel_1, 2: nivel_2, 3: nivel_3, 4: nivel_4, 5: nivel_5, 6: nivel_6, 0: nivel_1}
tipo_ubicaciones = ["Casa", "Plaza", "Centro Comercial", "Universidad", "Edificio"]
direcciones = {1: "arriba", 2: "abajo", 3: "izquierda", 4: "derecha"}

subgrilla = Subgrilla(0,(18,18))

class Sample:
    def __init__(self):
        subgrilla.agregar_ubic(zoom[subgrilla.zoom])
        self.lista = subgrilla.retornar_lista()
        self.centro = subgrilla.centro
        self.zoom = subgrilla.zoom

    def zooms(self, num):
        val = int(num // (100 / 6) + 1)
        subgrilla.zoom = val
        subgrilla.agregar_ubic(zoom[subgrilla.zoom])
        self.zoom = val
        self.lista = subgrilla.retornar_lista()
        self.centro = subgrilla.centro

        return self.lista

    def moverse(self, tupla):
        if tupla == (0,1):
            subgrilla.mover_centro("arriba")()
            subgrilla.agregar_ubic(zoom[subgrilla.zoom])
            self.lista = subgrilla.retornar_lista()
            self.centro = subgrilla.centro
            return self.lista
        if tupla == (0,-1):
            subgrilla.mover_centro("abajo")()
            subgrilla.agregar_ubic(zoom[subgrilla.zoom])
            self.lista = subgrilla.retornar_lista()
            self.centro = subgrilla.centro
            return self.lista
        if tupla == (1,0):
            subgrilla.mover_centro("izquierda")()
            subgrilla.agregar_ubic(zoom[subgrilla.zoom])
            self.lista = subgrilla.retornar_lista()
            self.centro = subgrilla.centro
            return self.lista
        if tupla == (-1,0):
            subgrilla.mover_centro("derecha")()
            subgrilla.agregar_ubic(zoom[subgrilla.zoom])
            self.lista = subgrilla.retornar_lista()
            self.centro = subgrilla.centro
            return self.lista


    def ubicaciones_por_region(self, tupla):
        zipped = list()
        parejas = list()
        numero = dict()
        lista_final = list()
        for i in range(len(zoom[1])):
            zipped.append(list(zip(zoom_1[tupla[1][0]][i], zoom[6][i])))
        for i in zipped:
            parejas.append(list(filter(lambda x: tupla[0][0] in x[1], [line for line in i])))
        for i in parejas:
            for j in i:
                if j[0] in numero.keys():
                    numero[j[0]] += 1
                if j[0] not in numero.keys():
                    numero[j[0]] = 1
        for i in numero:
            lista_final.append((i, numero[i]))
        return lista_final

    def region_sin_ubicacion(self, tupla):
        zipped = list()
        parejas = list()
        numero = dict()
        lista_final = list()
        for i in range(len(zoom[1])):
            zipped.append(list(zip(zoom_1[tupla[1][0]][i], zoom[6][i])))
        for i in zipped:
            for j in i:
                numero[j[0]] = 0
            parejas.append(list(filter(lambda x: tupla[0][0] in x[1], [line for line in i])))
        for i in parejas:
            for j in i:
                if j[0] in numero.keys():
                    numero[j[0]] += 1
                if j[0] not in numero.keys():
                    numero[j[0]] = 1
        for i in numero:
            if numero[i] == 0:
                lista_final.append((i))
        if len(lista_final) == 0:
            return "No hay {0} sin {1}".format(tupla[1][0],tupla[0][0])
        if len(lista_final) > 0:
            return lista_final

    def ubicacion1_ubicacion2(self, tupla):
        pass

    def cantidad_de_ubicacion(self, tupla):
        cantidad = list()
        el_centro = self.centro
        cantidad_numero = 0
        if tupla[0][0] not in tipo_ubicaciones:
            return "Acceso Prohibido"
        for k in subgrilla.retornar_lista():
            cantidad.append(list(filter(lambda x: tupla[0][0] in x, [line for line in k])))
        if tupla[1][0] == 0:
            for i in cantidad:
                cantidad_numero += i.count("'{0}'".format(tupla[0][0]))
            return int(cantidad_numero)
        for i in direcciones.keys():
            subgrilla.centro = el_centro
            subgrilla.agregar_ubic(zoom[subgrilla.zoom])
            for n in range(int(tupla[1][0])):
                subgrilla.mover_centro(direcciones[i])()
                subgrilla.agregar_ubic(zoom[subgrilla.zoom])
                for j in subgrilla.retornar_lista():
                    cantidad.append(list(filter(lambda x: tupla[0][0] in x, [line for line in j])))
        subgrilla.centro = el_centro
        for i in cantidad:
            cantidad_numero += i.count("'{0}'".format(tupla[0][0]))
        return int(cantidad_numero)

    def cantidad_subgrillas(self, tupla):
        if tupla[0][0] not in tipo_ubicaciones or self.zoom != 6:
            return "Acceso Prohibido"
        contador = 0
        contador_grillas = -1
        subgrillas = 0
        while contador < int(tupla[1][0]):
            contador = self.cantidad_de_ubicacion(([tupla[0][0]], [subgrillas]))
            contador_grillas += 1
            subgrillas += 1
            if contador_grillas > 300:
                return "El numero pedido no es posible"
        return contador_grillas










if __name__ == '__main__':
    sample = Sample()
    funciones = [sample.ubicaciones_por_region, sample.region_sin_ubicacion,
                 sample.ubicacion1_ubicacion2, sample.cantidad_de_ubicacion, sample.cantidad_subgrillas]
    interfaz = Interfaz(
        sample.zooms, sample.moverse, sample.lista, funciones)
    interfaz.full = False
    interfaz.size = 4
    interfaz.run()
