__author__ = 'Ignacio'

# clase Ubiacion, se inicializ con la coordenada x, coordenada y, su zoom y la informacion que contiene. Corresponde a
# los nodos de las subgrillas, y se puede acceder a las ubicaciones secantes a cada instancia.

class Ubicacion:
    def __init__(self, x, y, zoom, data):
        self.x = x
        self.y = y
        self.zoom = zoom
        self.data = data
        self._visited = False

    @property
    def izquierda(self):
        return self._izquierda

    @property
    def derecha(self):
        return self._derecha

    @property
    def arriba(self):
        return self._arriba

    @property
    def abajo(self):
        return self._abajo

    @property
    def visited(self):
        return self._visited

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

    @visited.setter
    def visited(self, value):
        self._visited = value

