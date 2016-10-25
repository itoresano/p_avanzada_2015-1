__author__ = 'Ignacio'

# Estas 2 funciones sirven para:
# cargar_matriz: crear listas multidimensionales que contengan los datos entregados en los archivos de texto
# encontrar_ubicaciones: encontrar las ubicaciones distintas para cada piso de la matriz original, gracias a los sets
# e.g saber cuantos continentes, paises, ubicaciones etc hay en los datos entregados.


def cargar_matriz(archivo):
    array = list(list(map(lambda l: l.strip().split("], ["), [line for line in open(archivo, encoding='utf8')])))
    quitar_tipo = lambda l: l[1]
    array = quitar_tipo(array)
    array = list(list(map(lambda l: l.strip("[").strip("]").split(", "), [line for line in array])))
    return array


def encontrar_ubicaciones(lista):
    ubicaciones = set()
    for i in lista:
        for j in i:
            ubicaciones.add(j.strip("'"))
    return ubicaciones















