__author__ = 'Ignacio'
from Ubicacion import Ubicacion
from carga_matrices import cargar_matriz
from collections import deque


# Esta es la clase que crea a estructura de datos para cada subgrilla que se muestra en la interfaz.
# para instanciarla solo hay q ingresar el zoom y el centro, y desde ahi la estructura se construye sola
# (al rededor del centro, con la dimension del lado dada por el zoom)

class Subgrilla():
    def __init__(self, zoom, centro):
        self._zoom = zoom
        self._centro = centro
        self.ubicaciones = dict()
        self.lista_ubic = list()
        self._lado = 38 - 6 * self._zoom
        self.grafo = dict()

    # propertys para settear y obtener los atributos de la clase
    @property
    def zoom(self):
        return self._zoom

    @zoom.setter
    def zoom(self, value):
        self._zoom = value

    @property
    def centro(self):
        return self._centro

    @property
    def lado(self):
        return 38 - 6 * self._zoom

    # Vertices o esquinas de la subgrilla, vertice_1 y vertice_2 corresponden a x, y los otros 2 a y.
    @property
    def vertice_1(self):
        return int(self._centro[0] - (self._lado / 2 - 1))

    @property
    def vertice_2(self):
        return int(self._centro[0] + self._lado / 2)

    @property
    def vertice_3(self):
        return int(self._centro[1] - (self._lado / 2 - 1))

    @property
    def vertice_4(self):
        return int(self._centro[1] + self._lado / 2)

    @centro.setter
    def centro(self, value):
        self._centro = value

    @lado.setter
    def lado(self, value):
        self._lado = value

    # Agrega los datos a la subgrilla en forma de instancias de la clase Ubicacion. Si las coordenadas traspasan los
    # limites su informacion pasa a ser Vacio
    def agregar_ubic(self, lista):
        for i in range(self.vertice_1, self.vertice_2 + 1):
            for j in range(self.vertice_3, self.vertice_4 + 1):
                if 0 <= i <= 199 and 0 <= j <= 299:
                    self.ubicaciones[j, i] = (Ubicacion(j, i, self.zoom, lista[i][j]))
                else:
                    self.ubicaciones[j, i] = Ubicacion(j, i, self.zoom, "Vacio")
                    # devuelven una lista con la informacion para poder mostrarla en la interfaz

    def retornar_lista(self):
        self.lista_ubic = [[self.ubicaciones[(n, v)].data for v in range(self.vertice_1, self.vertice_2 + 1)] for n in
                           range(self.vertice_3, self.vertice_4 + 1)]
        return self.lista_ubic

    # entrelazan cada nodo, u instancia de la clase Ubicacion que componen la subgrilla
    def entrelazar_subgrilla(self):
        for n in self.ubicaciones:
            if self.ubicaciones[n].x > self.vertice_1:
                self.ubicaciones[n].izquierda = self.ubicaciones[(n[0] - 1, n[1])]
            if self.ubicaciones[n].x <= self.vertice_1:
                self.ubicaciones[n].izquierda = None
            if self.ubicaciones[n].x < self.vertice_2:
                self.ubicaciones[n].derecha = self.ubicaciones[(n[0] + 1, n[1])]
            if self.ubicaciones[n].x >= self.vertice_2:
                self.ubicaciones[n].derecha = None
            if self.ubicaciones[n].y > self.vertice_3:
                self.ubicaciones[n].arriba = self.ubicaciones[n[0], n[1] - 1]
            if self.ubicaciones[n].y <= self.vertice_3:
                self.ubicaciones[n].arriba = None
            if self.ubicaciones[n].y < self.vertice_4:
                self.ubicaciones[n].abajo = self.ubicaciones[n[0], n[1] + 1]
            if self.ubicaciones[n].y >= self.vertice_4:
                self.ubicaciones[n].abajo = None

    # crea un grafo entre los nodos de la subgrilla
    def crear_grafo(self):
        lista = dict()
        for i in self.ubicaciones:
            if hasattr(self.ubicaciones[i].derecha, "x"):
                lista[1] = (self.ubicaciones[i].derecha.x, self.ubicaciones[i].derecha.y)
            if not hasattr(self.ubicaciones[i].derecha, "x"):
                if 1 in lista:
                    del lista[1]
            if hasattr(self.ubicaciones[i].izquierda, "x"):
                lista[2] = (self.ubicaciones[i].izquierda.x, self.ubicaciones[i].izquierda.y)
            if not hasattr(self.ubicaciones[i].izquierda, "x"):
                if 2 in lista:
                    del lista[2]
            if hasattr(self.ubicaciones[i].arriba, "x"):
                lista[3] = (self.ubicaciones[i].arriba.x, self.ubicaciones[i].arriba.y)
            if not hasattr(self.ubicaciones[i].arriba, "x"):
                if 3 in lista:
                    del lista[3]
            if hasattr(self.ubicaciones[i].abajo, "x"):
                lista[4] = (self.ubicaciones[i].abajo.x, self.ubicaciones[i].abajo.y)
            if not hasattr(self.ubicaciones[i].abajo, "x"):
                if 4 in lista:
                    del lista[4]

            self.grapho[(self.ubicaciones[i].x, self.ubicaciones[i].y)] = [n for n in lista.values()]


    # mueve el centro de la subgrilla para poder construir nuevas estructuras de datos
    def mover_centro(self, direccion):
        def arriba():
            self.centro = (self.centro[0], self.centro[1] - self.lado)

        def abajo():
            self.centro = (self.centro[0], self.centro[1] + self.lado)

        def izquierda():
            self.centro = (self.centro[0] - self.lado, self.centro[1])

        def derecha():
            self.centro = (self.centro[0] + self.lado, self.centro[1])

        def nada():
            self.centro = self.centro

        return locals()[direccion]

    # properties
    @property
    def derecha(self):
        return self._derecha

    @property
    def izquierda(self):
        return self._izquierda

    @property
    def arriba(self):
        return self._arriba

    @property
    def abajo(self):
        return self._abajo

    @derecha.setter
    def derecha(self, value):
        self._derecha = value

    @izquierda.setter
    def izquierda(self, value):
        self._izquierda = value

    @arriba.setter
    def arriba(self, value):
        self._arriba = value

    @abajo.setter
    def abajo(self, value):
        self._abajo = value










