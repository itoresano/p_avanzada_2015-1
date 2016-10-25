import threading
import time
import random

__author__ = 'Jm'


class Godzilla(threading.Thread):

    def __init__(self, hp):
        super().__init__()
        self.hp = hp
        self.vivo = True
        self.lista = list()


    def run(self):
        while self.vivo:
            time.sleep(8)
            if self.vivo:
                self.atacar()
                print("Godzilla atacando")


    def atacado(self, guerrero):
        self.hp -= guerrero.ataque
        if self.hp <= 0:
            self.vivo = False
            print("Godzilla MURIO!!")

        else:
            print(
                "Godzilla ha sido atacado! El  Guerrero " + str(guerrero.ID) +
                " le ha hecho " + str(guerrero.ataque) + " de dano" +
                ". HP Godzilla " + str(self.hp))
            guerrero.atacado(int(guerrero.ataque / 4))

    def atacar(self):
        for i in self.lista:
            if i.vivo:
                i.hp -= 3



class Guerrero(threading.Thread):

    def __init__(self, Godzilla, velocidad, hp, ataque):
        super().__init__()
        self.vivo = True
        self.Godzilla = Godzilla
        self.velocidad = velocidad
        self.hp = hp
        self.ID = next(Guerrero.get_i)
        self.ataque = ataque

    def run(self):
        self.Godzilla.lista.append(self)
        while self.vivo and self.Godzilla.vivo:
            time.sleep(self.velocidad)
            if self.vivo and self.Godzilla.vivo:
                self.Godzilla.atacado(self)

    def atacado(self, ataque):
        self.hp -= ataque
        print("El guerrero " + str(self.ID) +
              " ha sido danado!! HP " + str(self.hp))
        if self.hp <= 0:
            self.vivo = False
            print("El guerrero " + str(self.ID) + " ha muerto :( !!!")

    def id_():
        i = 0
        while True:
            yield i
            i += 1

    get_i = id_()

class Creador_de_soldados(threading.Thread):

    def __init__(self, tiempo, Godzilla, hp, ataque, lista):
        super().__init__()
        self.tiempo = tiempo
        self.Godzilla = Godzilla
        self.ataque = ataque
        self.hp = hp
        self.lista = lista

    def run(self):
        while self.Godzilla.vivo:
            time.sleep(self.tiempo)
            if self.Godzilla.vivo:
                self.lista.append(Guerrero(self.Godzilla, random.randint(4, 19), self.hp, self.ataque))
                self.lista[-1].start()
                print("Aparecio un soldado")




if __name__ == "__main__":
    print("Comenzo la Simulacion!")
    NUMERO_SOLDADOS = 1
    lista_soldados = []
    Godzilla = Godzilla(100)
    for i in range(NUMERO_SOLDADOS):
        lista_soldados.append(Guerrero(Godzilla, random.randint(4, 19), 50, 10))
        lista_soldados[i].start()
    creador_de_soldados = Creador_de_soldados(6, Godzilla, 50, 10, lista_soldados)
    Godzilla.start()
    creador_de_soldados.start()

