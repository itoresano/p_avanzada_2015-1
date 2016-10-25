from estaciones_metro import Direccion, MapaMetro, Estacion


# Retornar true si existe un camino desde la estacion_origen a
# la estacion_destino, false en caso contrario.
# Solo puede controlar las variables estacion_origen y
# estacion_destino , no el mapa.

# Por ejemplo puedes hacer:
# estacion_origen.izquierda.izquierda
inicio = 0
estacion_visitada = []
direcciones = []
reset = 0
contador = 0
reseteado = False


def camino(estacion_origen, estacion_destino):

    i = 0

    global contador
    global reset
    global reseteado
    print(estacion_visitada)
    print(direcciones)
    print(reset)
    print(contador)
    print(reseteado)
    global inicio

    if inicio == 0:
        estacion_visitada.append(estacion_origen)
        inicio = 1

    if estacion_origen == estacion_destino:

        i = 1
        return True, estacion_visitada


    while i == 0:
        if estacion_origen.derecha and estacion_origen.derecha not in estacion_visitada:
            if reseteado == True and direcciones[contador - 1] == "derecha":
                reseteado = False
                direcciones.pop()
                continue
            else:
                estacion_visitada.append(estacion_origen.derecha)
                direcciones.append("derecha")
                contador += 1
            return camino(estacion_origen.derecha, estacion_destino)
        if estacion_origen.izquierda and estacion_origen.izquierda not in estacion_visitada:
            if reseteado == True and direcciones[contador - 1] == "izquierda":
                reseteado = False
                direcciones.pop()
                continue
            else:
                estacion_visitada.append(estacion_origen.izquierda)
                direcciones.append("izquierda")
                contador += 1
            return camino(estacion_origen.izquierda, estacion_destino)
        elif estacion_origen.arriba and estacion_origen.arriba not in estacion_visitada:
            if reseteado == True and direcciones[contador - 1] == "arriba":
                reseteado = False
                direcciones.pop()
                continue
            else:
                estacion_visitada.append(estacion_origen.arriba)
                direcciones.append("arriba")
                contador += 1
            return camino(estacion_origen.arriba, estacion_destino)
        elif estacion_origen.abajo and estacion_origen.abajo not in estacion_visitada:
            if reseteado == True and direcciones[contador - 1] == "abajo":
                reseteado = False
                direcciones.pop()
                continue
            else:
                estacion_visitada.append(estacion_origen.abajo)
                direcciones.append("abajo")
                contador += 1
            return camino(estacion_origen.abajo, estacion_destino)
        else:
            reseteado = True
            reset += 1
            del estacion_visitada[reset:]
            del direcciones[reset+1:]
            contador = len(estacion_visitada)
            return camino(estacion_visitada[reset-1], estacion_destino)


            # ==========
            # COMPLETAR
            # ==========
        return False


if __name__ == "__main__":
    mapa = MapaMetro.mapa_de_ejemplo()
    #print(camino(mapa.primera_estacion, mapa.estaciones[0]))
    #print(camino(mapa.estaciones[1], mapa.primera_estacion))
    print(camino(mapa.estaciones[0], mapa.estaciones[17]))
    #print(estacion_visitada)
    #print(camino(mapa.primera_estacion, mapa.primera_estacion))
    #print(camino(mapa.primera_estacion, mapa.ultima_estacion))


