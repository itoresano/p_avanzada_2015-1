__author__ = 'Ignacio'


class Itinerario:
    def __init__(self, id_objeto, id_viaje):
        self.id_objeto = id_objeto
        self.id_viaje = id_viaje

    def __str__(self):
        return "id Objeto: %s - id Viaje: %s" % (self.id_objeto, self.id_viaje)
