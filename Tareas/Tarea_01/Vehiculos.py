__author__ = 'Ignacio'


class Vehiculo:
    def __init__(self, modelo, nombre, tipo, tamaño, velocidad, costo, **kwargs):
        self.modelo = modelo
        self.nombre = nombre
        self.tipo = tipo
        self.tamaño = tamaño
        self.velocidad = velocidad
        self.costo = costo



class Transporte_carga(Vehiculo):
    def __init__(self, vol_max, peso_max, tipo_carga, **kwargs):
        super().__init__(**kwargs)
        self.vol_max = vol_max
        self.peso_max = peso_max
        self.tipo_carga = tipo_carga


class Transporte_pasajeros(Vehiculo):
    def __init__(self, asientos, **kwargs):
        super().__init__(**kwargs)
        self.asientos = asientos


class Avion(Transporte_carga, Transporte_pasajeros):
    def __init__(self, alcance, **kwargs):
        super().__init__(**kwargs)
        self.alcance = alcance



class Bus(Transporte_pasajeros):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Camion(Transporte_carga):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Barco(Transporte_carga):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Crucero(Transporte_pasajeros):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)



