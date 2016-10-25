__author__ = 'Ignacio'
import math
import matplotlib.pyplot as plt

def calcular_energia(tipo):

    def eolica(tiempo):
        if tiempo < 720:
            return math.sin(tiempo)/3 + math.asin(3*tiempo)/3 + 1/2
        else:
            return 1

    def solar(tiempo):
        if 360 <= tiempo < 720:
            return (math.cos(tiempo))**2
        else:
            return 1

    def nuclear(tiempo):
        return 22 * math.exp(-0.05*tiempo)

    return locals()[tipo]

print(calcular_energia("solar")(500))

def energia_acumulada(tipo):
    n = 5
    k = 0
    yield calcular_energia(tipo)(k/n)
    if k <= 1440:
        k += 1


def devolver_tiempo():
    n = 5
    k = 0
    yield k/n
    k += 1

s1 = energia_acumulada("solar")
lista_solar = [next(s1) for i in range(1440)]
e1 = energia_acumulada("eolica")
lista_eolica = [next(e1) for i in range(1440)]
n1 = energia_acumulada("nuclear")
lista_nuclear = [next(n1) for i in range(1440)]

t1 = devolver_tiempo()
lista_tiempo = [next(t1) for i in range(1440)]

grafico_solar = plt.scatter(lista_solar, lista_tiempo, c="red", edgecolors= "None")
grafico_solar.plt.show()

grafico_eolico = plt.scatter(lista_eolico, lista_tiempo, c="red", edgecolors= "None")
grafico_eolico.plt.show()

grafico_nuclear = plt.scatter(lista_nuclear, lista_tiempo, c="red", edgecolors= "None")
grafico_nuclear.plt.show()










