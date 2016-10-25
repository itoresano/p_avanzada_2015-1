__author__ = 'Ignacio'


class Terminal:
    def __init__(self, code, ciudad, tipo, tamaño):
        self.code = code
        self.ciudad = ciudad
        self.tipo = tipo
        self.tamaño = tamaño

    def __str__(self):
        return "Codigo: %s - Ciudad: %s - Tipo: %s - Tamaño: %s " % (self.code, self.ciudad, self.tipo, self.tamaño)

