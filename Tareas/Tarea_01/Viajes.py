__author__ = 'Ignacio'


class Viaje:
    def __init__(self, id, origen, destino, ruta, hora_partida, vehiculo):
        self.id = id
        self.origen = origen
        self.destino = destino
        self.ruta = ruta
        self.hora_partida = hora_partida
        self.vehiculo = vehiculo

    def __str__(self):
        return "Id: %s - Origen: %s - Destino: %s - Ruta: %s - Hora Partida: %s - Vehiculo %s" % (self.id, self.origen,
                                                                                                  self.destino,
                                                                                                  self.ruta,
                                                                                                  self.hora_partida,
                                                                                                  self.vehiculo)

