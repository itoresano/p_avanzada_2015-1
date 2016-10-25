__author__ = "Ignacio"

from interfaz import Interfaz
from Subgrilla import Subgrilla
from Ubicacion import Ubicacion
from carga_matrices import cargar_matriz, encontrar_ubicaciones


# Pisos o niveles de la matriz de 3 dimensiones
nivel_1 = cargar_matriz("continentes.txt")
nivel_2 = cargar_matriz("paises.txt")
nivel_3 = cargar_matriz("ciudades.txt")
nivel_4 = cargar_matriz("comunas.txt")
nivel_5 = cargar_matriz("calles.txt")
nivel_6 = cargar_matriz("tipos.txt")

# diccionarios y sets relevantes para la iteracion por pisos, funciones etc.
zoom_1 = {"Continente": nivel_1, "Pais": nivel_2, "Ciudad": nivel_3, "Comuna": nivel_4, "Calle": nivel_5}
zoom = {1: nivel_1, 2: nivel_2, 3: nivel_3, 4: nivel_4, 5: nivel_5, 6: nivel_6, 0: nivel_1}
tipo_ubicaciones = encontrar_ubicaciones(nivel_6)
direcciones = {1: "arriba", 2: "abajo", 3: "izquierda", 4: "derecha"}

#Creacion de la Subgrilla inicial, zoom = 0, centro = (18,18).
subgrilla = Subgrilla(0, (18, 18))


class Main:
    def __init__(self):
        subgrilla.agregar_ubic(zoom[subgrilla.zoom])
        self.lista = subgrilla.retornar_lista()
        self.centro = subgrilla.centro
        self.zoom = subgrilla.zoom

    # Funcion zoom, transforma a num (0,99) a un numero entre 1 y 6. Settea el zoom de la subgrilla inicial, y retorna
    # la nueva lista
    def zooms(self, num):
        val = int(num // (100 / 6) + 1)
        subgrilla.zoom = val
        subgrilla._lado = subgrilla.lado
        subgrilla.agregar_ubic(zoom[subgrilla.zoom])
        self.zoom = val
        self.lista = subgrilla.retornar_lista()
        self.centro = subgrilla.centro
        return self.lista

    # Funcion para moverse entre cada, subgrilla, lo que hace esta funcion es que settea un nuevo centro de la subgrilla
    # lo que hace que cambien los vertices, y por lo tanto los datos dentro de la subgrilla, creando una nueva
    # estructura de datos. Los movimientos se rigen al enunciado con respecto a las tuplas recibidas aunq estos
    # contradicen a la interfaz grafica.
    def moverse(self, tupla):
        if tupla == (0, 1):
            subgrilla.mover_centro("arriba")()
            subgrilla.agregar_ubic(zoom[subgrilla.zoom])
            self.lista = subgrilla.retornar_lista()
            self.centro = subgrilla.centro
            return self.lista
        if tupla == (0, -1):
            subgrilla.mover_centro("abajo")()
            subgrilla.agregar_ubic(zoom[subgrilla.zoom])
            self.lista = subgrilla.retornar_lista()
            self.centro = subgrilla.centro
            return self.lista
        if tupla == (1, 0):
            subgrilla.mover_centro("izquierda")()
            subgrilla.agregar_ubic(zoom[subgrilla.zoom])
            self.lista = subgrilla.retornar_lista()
            self.centro = subgrilla.centro
            return self.lista
        if tupla == (-1, 0):
            subgrilla.mover_centro("derecha")()
            subgrilla.agregar_ubic(zoom[subgrilla.zoom])
            self.lista = subgrilla.retornar_lista()
            self.centro = subgrilla.centro
            return self.lista

    # Esta funcion cuenta las ubicaciones por region, primero "zippea" la lista que contiene la informacion de la region
    # con la lista de ubicaciones, luego usa "filter" para seleccionar las parejas que cumplen con lo ingresado a la
    # funcion, despues ingresa a un diccionario los las regiones y finalmente cuenta cuantas veces estan "emparejadas" a la
    # ubicacion ingresada
    def ubicaciones_por_region(self, tupla):
        zipped = list()
        parejas = list()
        numero = dict()
        lista_final = list()
        for i in range(len(zoom[1])):
            zipped.append(list(zip(zoom_1[tupla[1][0]][i], zoom[6][i])))
        for i in zipped:
            parejas.append(list(filter(lambda x: tupla[0][0] in x[1], [line for line in i])))
        for i in parejas:
            for j in i:
                if j[0] in numero.keys():
                    # se agrega 1 al valor diccionario[region]
                    numero[j[0]] += 1
                if j[0] not in numero.keys():
                    # se crea el valor diccionario[region]
                    numero[j[0]] = 1
        for i in numero:
            lista_final.append((i, numero[i]))
        return lista_final

    # Esta funcion busca regiones sin un tipo de ubicacion particular, es muy parecida a la funcion
    # ubicaciones_por_region, pero ademas, guarda en un diccionario las regiones que no tienen estas ubicaciones:
    def region_sin_ubicacion(self, tupla):
        zipped = list()
        parejas = list()
        numero = dict()
        lista_final = list()
        for i in range(len(zoom[1])):
            zipped.append(list(zip(zoom_1[tupla[1][0]][i], zoom[6][i])))
        for i in zipped:
            for j in i:
                #Todas las regiones comienzan con valor 0
                numero[j[0]] = 0
            parejas.append(list(filter(lambda x: tupla[0][0] in x[1], [line for line in i])))
        for i in parejas:
            for j in i:
                if j[0] in numero.keys():
                    # se aumenta el valor de la region
                    numero[j[0]] += 1
        for i in numero:
            # Se rescatan las regiones que tienen no tienen la ubicacion ingresada
            if numero[i] == 0:
                lista_final.append((i))
        if len(lista_final) == 0:
            return "No hay {0} sin {1}".format(tupla[1][0], tupla[0][0])
        if len(lista_final) > 0:
            return lista_final

    # Esta funcion retorna el camino entre 2 ubicaciones dadas, esta creada una subgrilla, de dimension 300*300, en la
    # cual cada nodo es una ubicacion, que esta relacionada con sus nodos adyacentes, mi idea era utilizar un algoritmo
    # "A star Pathfinding algorithm" pero no tuve tiempo de escribir uno, teniendo en cuenta que no se pueden usar
    # librerias externas como priorityqueu o heapq. Luego cree un grafo y tratar de encontrar el camino mas corto, pero
    # no supe hacer que el algoritmo minimizara la cantidad de veces que se pasa por la ubicacion, aparte
    # con todos los algoritmos que trate, el tiempo de espera era muy alto.
    def ubicacion1_ubicacion2(self, tupla):
        centro = (abs(tupla[0][0][0] - tupla[1][0][0]) // 2, abs(tupla[0][0][1] - tupla[1][0][1]) // 2)
        lado = max(abs(tupla[0][0][0] - tupla[1][0][0]) + 1, abs(tupla[0][0][1] - tupla[1][0][1]) + 1)
        sb = Subgrilla(6, (centro))
        sb.lado = lado
        sb.agregar_ubic(zoom[sb.zoom])
        sb.entrelazar_subgrilla()
        sb.crear_grafo()

        def camino_mas_corto(grafo, inicio, final, recorrido=list()):
            recorrido += [inicio]
            if inicio == final:
                return recorrido
            if inicio not in grafo:
                return print("No existe camino entre")
            recorrido_final = None
            for node in grafo[inicio]:  #para cada nodo adyacente al incial
                if node not in recorrido:  #revisa si esque ya se paso por el nodo
                    nuevo_recorrido = camino_mas_corto(grafo, node, final, recorrido)  #recrusion con el nuevo nodo
                    if nuevo_recorrido:
                        if isinstance(recorrido_final, "list") or len(nuevo_recorrido) < len(recorrido_final):
                            recorrido_final = nuevo_recorrido
            return recorrido_final

        return camino_mas_corto(sb.grafo, tupla[0][0], tupla[1][0])

    # Esta funcion cuenta la cantidad de ubicaciones dentro de una "cruz" de subgrillas que tiene como centro la
    # subgrilla que esta en la interfaz. Se ingresa el tipo de ubicacion a contar, y la cantidad de grillas de
    # distancia que debe haber, la funcion retorna la cantidad de ubicaciones de tipo indicado en ese espacio.

    def cantidad_de_ubicacion(self, tupla):
        cantidad = list()
        el_centro = self.centro
        # se guarda el centro anterior a ejecutar la funcion
        cantidad_numero = 0
        if tupla[0][0] not in tipo_ubicaciones or self.zoom != 6:
            # Si se ingresa un tipo no existente o se hace la consulta en otro nivel de la grilla
            return "Acceso Prohibido"
        for k in subgrilla.retornar_lista():
            cantidad.append(list(filter(lambda x: tupla[0][0] in x, [line for line in k])))
        if tupla[1][0] == 0:
            # Si se ingresa el numero 0, solo se cuentan las ubicaciones en la subgrilla que esta en pantalla
            for i in cantidad:
                cantidad_numero += i.count("'{0}'".format(tupla[0][0]))
            return int(cantidad_numero)
        for i in direcciones.keys():
            subgrilla.centro = el_centro
            # se vuelve al centro anterior
            subgrilla.agregar_ubic(zoom[subgrilla.zoom])
            for n in range(int(tupla[1][0])):
                subgrilla.mover_centro(direcciones[i])()
                # se mueve el centro en una de las 4 direcciones y se crea una nueva estructura de datos (subgrilla)
                subgrilla.agregar_ubic(zoom[subgrilla.zoom])
                # se agregan las ubicaciones
                for j in subgrilla.retornar_lista():
                    cantidad.append(list(filter(lambda x: tupla[0][0] in x, [line for line in j])))
        subgrilla.centro = el_centro  # se vuelve al centro anterior
        for i in cantidad:
            cantidad_numero += i.count("'{0}'".format(tupla[0][0]))
        return int(cantidad_numero)

    # Esta funcion retorna la cantidad de subgrillas que hay que moverse para encontrar un numero n de ubicaciones.
    # En ella se ejecuta la funcion cantidad_de_ubicacion() para 0,1,...,n subgrillas y se cuentan las ubicaciones
    # obtenidas para cada n, una vez q se cuentan mas ubicaciones de las ingresadas, se retorna el numero de subgrillas

    def cantidad_subgrillas(self, tupla):
        if tupla[0][0] not in tipo_ubicaciones or self.zoom != 6:
            return "Acceso Prohibido"
        contador = 0
        contador_grillas = -1
        subgrillas = 0
        while contador < int(tupla[1][0]):  #mientras el numero de ubicaciones contado sea menor al numero pedido
            contador = self.cantidad_de_ubicacion(([tupla[0][0]], [subgrillas]))  #se llama a la funcion anterior
            contador_grillas += 1
            subgrillas += 1
            if contador_grillas > 300:  #si ya se recorre el mapa entero (desde un extremo al otro) y no se llega a n
                return "El numero pedido no es posible"  #la funcion se detiene
        return contador_grillas


if __name__ == '__main__':
    main = Main()
    funciones = [main.ubicaciones_por_region, main.region_sin_ubicacion,
                 main.ubicacion1_ubicacion2, main.cantidad_de_ubicacion, main.cantidad_subgrillas]
    interfaz = Interfaz(
        main.zooms, main.moverse, main.lista, funciones)
    interfaz.full = False
    interfaz.size = 4
    interfaz.run()
