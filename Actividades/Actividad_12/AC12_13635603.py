__author__ = 'Ignacio'

from collections import deque
from random import choice, randrange
from random import expovariate

cajas = [1, 2]

#Variables de estado:
# tiempo de simulacion, tiempo de atencion de cada caja, tarea_actual de cada caja, tiempo maximo del sistema, la tasa
# de llegada de personas al banco, tiempo_proximo_auto tiempo de llegada del proximo auto, tiempo_atencion: cuando se
# atiende un auto, tiempo_espera: tiempo de espera de cada caja, cola_espera: colas de cada caja

# Eventos relevantes:
# - Llega una persona al banco
# - Elige una cola
# - Una persona es atendida por la caja 1 o 2
# - Una persona sale de la caja 1 o 2
# - una persona se cambia de cola

class Persona:
    def __init__(self, tiempo_llegada=0):
        self.tiempo_llegada = tiempo_llegada
        self.tipo = "Persona"


class Caja:
    def __init__(self, numero):
        self.numero = numero
        self.tarea_actual = None
        self.tiempo_atencion = 0

    def ocupado(self):
        return self.tarea_actual != None

    def atender_persona(self, persona):
        self.atencion_actual = persona
        self.tiempo_atencion = randrange(1, 11)

    def __repr(self):
        return " CAJA {0} Se atiende a {1} con un tiempo de atencion {2}".format(self.numero, self.atencion_actual.tipo,
                                                                                 self.tiempo_atencion)


class Simulacion:
    def __init__(self, tiempo_maximo, tasa_llegada):
        self.tiempo_maximo_sim = tiempo_maximo
        self.tasa_llegada = tasa_llegada
        self.tiempo_simulacion = 0
        self.tiepo_proxima_persona = 0
        self.tiempo_atencion = {1: 0, 2: 0}
        self.tiempo_espera = {1: 0, 2: 0}
        self.caja = {1: Caja(1), 2: Caja(2)}
        self.cola_espera = [deque(), deque()]
        self.personas_atendidas = 0

    def proxima_persona(self, tasa_llegada):
        self.tiempo_proxima_persona = self.tiempo_simulacion + (randrange(tasa_llegada) + 1)

    def run(self):
        self.proxima_persona(self.tasa_llegada)

        while True:
            for i in cajas:
                if (self.caja[i].ocupado() and self.tiempo_proxima_persona < self.tiempo_atencion[i]) or (not self.caja[i].ocupado()):
                    self.tiempo_simulacion = self.tiempo_proxima_persona
                else:
                    self.tiempo_simulacion = self.tiempo_atencion[i]

            if self.tiempo_simulacion > self.tiempo_maximo_sim:
                break

            print("[SIMULACION] tiempo: {0} min".format(self.tiempo_simulacion))

            if self.tiempo_simulacion == self.tiempo_proxima_persona:
                if len(self.cola_espera[i]) < len(self.cola_espera[-i]):
                    self.cola_espera[i].append(Persona(self.tiempo_simulacion))
                    self.proxima_persona(self.tasa_llegada)
                if len(self.cola_espera[i]) > len(self.cola_espera[-i]):
                    self.cola_espera[-i].append(Persona(self.tiempo_simulacion))
                    self.proxima_persona(self.tasa_llegada)
                else:
                    self.cola_espera[0].append(Persona(self.tiempo_simulacion))
                    self.proxima_persona(self.tasa_llegada)
                print("[COLA] caja {0} llega persona en tiempo simulacion: {1} min".format(i, self.tiempo_simulacion))

                if not self.caja[i].ocupado() and len(self.cola_espera[i]) > 0:
                    proxima_persona = self.cola_espera[i].popleft()
                    self.caja[i].atender_persona(proxima_persona)

                    self.tiempo_atencion[i] = self.tiempo_simulacion + self.caja[i].tiempo_atencion[i]
                    print(self.caja[i])
                if len(self.cola_espera[i]) - 1 > len(self.cola_espera[-i]):
                    self.cola_espera[-i].append(self.cola_espera[i].pop())
                if len(self.cola_espera[i]) - 1 < len(self.cola_espera[-i]):
                    self.cola_espera[-i].append(self.cola_espera[i].pop())

            else:
                print("[CAJA] {0} Sale: Persona a los {1} min.".format(i, self.tiempo_simulacion))
                self.tiempo_espera[i] += self.tiempo_simulacion - self.caja[i].tarea_actual.tiempo_llegada
                self.caja[i].tarea_actual = None
                self.personas_atendidas += 1

if __name__ == "__main__":
    tasa_llegada_personas = 3
    s = Simulacion(80, tasa_llegada_personas)
    s.run()















