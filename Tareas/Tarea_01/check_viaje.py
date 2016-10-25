__author__ = 'Ignacio'

import carga_de_datos as cdd

# Esta clase checkea que el viaje de un pasajero/carga sea posible, segun la disponibilidad de asientos, volumen,
# peso
# En teoria tambien deberia checkear si en un viaje el vehiculo asignado tiene el tamaño correspondiente a la ruta o
# por ejemplo si un avion esta asignado solo a rutas aereas y no a un viaje en carretera,
# pero no conte con los recursos para hacerlo.
def check(tipo):
    def Avion(viaje, volumen=None, peso=None, tipo_carga=None):
        contenido = list()
        contenido_carga = list()
        contenido_psjs = list()
        vol_in = 0
        peso_in = 0
        for i in cdd.it:
            if cdd.viajes[viaje].id in cdd.it[i].id_viaje:
                contenido.append(cdd.it[i].id_objeto)
        for i in contenido:
            if type(i).__name__ == "Carga":
                contenido_carga.append(i)
            if type(i).__name__ == "Pasajero":
                contenido_psjs.append(i)
        if len(contenido_psjs) + 1 > int(cdd.vehiculos[cdd.viajes[viaje].vehiculo].asientos):
            print("Asientos insuficientes")
            return False
        for i in contenido_carga:
            vol_in += float(cdd.cargas[i].volumen)
        if vol_in + float(volumen) > float(cdd.vehiculos[cdd.viajes[viaje].vehiculo].vol_max):
            print("Volumen maximo superado")
            return False
        for i in contenido_carga:
            peso_in += float(cdd.cargas[i].peso)
        if peso_in + float(peso) > float(cdd.vehiculos[cdd.viajes[viaje].vehiculo].peso_max):
            print("Peso maximo superado")
            return False
        if tipo_carga not in [cdd.vehiculos[cdd.viajes[viaje].vehiculo].tipo_carga, None]:
            print("Tipo de carga inadecuado")
            return False
        else:
            return True

    def Bus(viaje):
        contenido = list()
        for i in cdd.it:
            if cdd.viajes[viaje].id in cdd.it[i].id_viaje:
                contenido.append(cdd.it[i].id_objeto)
        if len(contenido) + 1 > cdd.vehiculos[cdd.viajes[viaje].vehiculo].asientos:
            print("Asientos insuficientes")
            return False
        else:
            return True

    def Camion(viaje, volumen, peso, tipo_carga):
        contenido = list()
        peso_in = 0
        vol_in = 0
        for i in cdd.it:
            if cdd.viajes[viaje].id in cdd.it[i].id_viaje:
                contenido.append(cdd.it[i].id_objeto)
        for i in contenido:
            peso_in += float(cdd.cargas[i].peso)
        if float(peso_in + peso) > float(cdd.vehiculos[cdd.viajes[viaje].vehiculo].peso_max):
            print("Peso maximo alcanzado")
            return False
        for i in contenido:
            vol_in += float(cdd.cargas[i].volumen)
        if float(vol_in) + float(volumen) > float(cdd.vehiculos[cdd.viajes[viaje].vehiculo].vol_max):
            print("Volumen maximo alcanzado")
            return False
        if tipo_carga != cdd.vehiculos[cdd.viajes[viaje].vehiculo].tipo_carga:
            print("Tipo de carga incompatible")
            return False
        else:
            return True

    def Barco(viaje, volumen, peso, tipo_carga):
        return Camion(viaje, volumen, peso, tipo_carga)

    def Crucero(viaje):
        return Bus(viaje)

    return locals()[tipo]






