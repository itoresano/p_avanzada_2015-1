__author__ = 'Ignacio'


class Pasajero:

    def __init__(self, nombre, apellido, rut):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut

    def __str__(self):
        return "Rut: %s - Nombre: %s - Apellido %s" % (self.rut, self.nombre, self.apellido)








