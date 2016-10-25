__author__ = ['Bastian','Jm']
import threading
import time
import random


class MegaGodzilla(threading.Thread):

    ###
    # Tienen que completar la clase (piensen en los locks necesarios)
    ###
    lock = threading.Lock()
    def __init__(self, hp):
        super().__init__()
        self.hp = hp
        self.lista = list()

    @property
    def vivo(self):
        if self.hp > 0:
            return True
        return False

    ###
    def run(self):
        while self.vivo:
            time.sleep(random.randint(3, 6))
            ataque = random.randint(0, 1)
            if ataque == 0:
                self.atacar()
            if ataque == 1:
                dormido = False
                for n in self.lista:
                    if n.vivo and n.dormido:
                        dormido = True
                        break
                if dormido:
                    self.atacar()
                else:
                    self.ataque_ultimate()
    ###

    def atacado(self, soldado):
        self.hp -= soldado.ataque
        if not self.vivo:
            print("MegaGodzilla ha muerto!!")
        else:
            print(
                "Mega-Godzilla ha sido atacado! El soldado le ha hecho " + str(
                    soldado.ataque) + " de dano" +
                ". HP Godzilla " + str(self.hp))
            soldado.atacado(int(soldado.ataque / 4))

    ###
    def atacar(self):
        print("ataque normal")
        for i in self.lista:
            if i.vivo:
                i.atacado(3)

    def ataque_ultimate(self):
        MegaGodzilla.lock.acquire()
        print("ataque ultimate")
        for i in self.lista:
            if i.vivo:
                i.atacado(6)
                i.dormido = True

        MegaGodzilla.lock.release()




    ###


class Soldado(threading.Thread):

    ###
    # Tienen que completar la clase (piensen en los locks necesarios)
    ###

    def __init__(self, MegaGodzilla, velocidad, hp, ataque):
        super().__init__()
        self.MegaGodzilla = MegaGodzilla
        self.velocidad = velocidad
        self.hp = hp
        self.ID = next(Soldado.get_i)
        self.ataque = ataque
        self.dormido = False

    @property
    def vivo(self):
        if self.hp > 0:
            return True
        return False

    ###
    def run(self):
        while self.vivo and self.MegaGodzilla.vivo:
            if not self.dormido:
                time.sleep(random.randint(4,self.velocidad))
                self.MegaGodzilla.lock.acquire()
                try:

                    if self.vivo and self.MegaGodzilla.vivo and not self.dormido:
                        time.sleep(random.randint(1,3))
                        self.MegaGodzilla.atacado(self)
                    if self.dormido:
                        time.sleep(10)
                        self.dormido = False
                finally:
                    self.MegaGodzilla.lock.release()
            else:
                time.sleep(10)
                self.dormido = False
    ###

    def atacado(self, ataque):
        self.hp -= ataque
        print("El soldado" + str(self.ID) +
              " ha sido danado!!  HP " + str(self.hp))
        if not self.vivo:
            print("El soldado" + str(self.ID) + " ha muerto :( !!!")



    def id_():
        i = 0
        while True:
            yield i
            i += 1

    get_i = id_()


if __name__ == "__main__":
    print("Comenzo la Simulacion!")

    ###
    MegaGodzilla = MegaGodzilla(500)
    MegaGodzilla.start()
    for i in range(3):
        MegaGodzilla.lista.append(Soldado(MegaGodzilla, 19, 40, 20))
        MegaGodzilla.lista[-1].start()
    ###
