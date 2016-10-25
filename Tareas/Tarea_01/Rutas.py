__author__ = 'Ignacio'


class Ruta:
    def __init__(self, id, ciudad1, ciudad2, tipo, largo, tamaño, costo):
        self.id = id
        self.ciudad1 = ciudad1
        self.ciudad2 = ciudad2
        self.tipo = tipo
        self.largo = largo
        self.tamaño = tamaño
        self.costo = costo

    def __str__(self):
        return "id: %s - Ciudad 1: %s - Ciudad 2: %s - Tipo: %s - Largo: %s - Tamaño: %s - Costo: %s " % (self.id,
                                                                                                          self.ciudad1,
                                                                                                          self.ciudad2,
                                                                                                          self.tipo,
                                                                                                          self.largo,
                                                                                                          self.tamaño,
                                                                                                          self.costo)

