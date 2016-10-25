__author__ = 'Ignacio'


class Carga:
    def __init__(self, id, nombre, peso, volumen, tipo):
        self.id = id
        self.nombre = nombre
        self.peso = peso
        self.volumen = volumen
        self.tipo = tipo

    def __str__(self):
        return "id: %s - Nombre: %s - Peso: %s - Volumen: %s - Tipo: %s" % (self.id, self.nombre, self.peso, self.volumen,
                                                                       self.tipo)


