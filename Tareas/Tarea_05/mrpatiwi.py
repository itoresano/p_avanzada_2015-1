__author__ = 'Ignacio'
from PyQt4 import QtCore, QtGui
import os, time, random

# Clase del fantasma mrpatiwi, muy parecida a pocmon
class Mrpatiwi(QtGui.QLabel):
    def __init__(self, parent):
        QtGui.QWidget.__init__(self, parent)
        self.parent = parent
        self.rest = False
        self.lado = 25
        self.setPixmap(QtGui.QPixmap(os.getcwd() + "\\Imagenes\\mrpatiwi - copia.png"))
        self.direccion = "Derecha"
        self.velocidad = 0.05
        self.thread = thread_patiwi(self)
        self.thread.trigger.connect(self.tryMove)
        self.thread.start()

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value):
        self._x = value

    @y.setter
    def y(self, value):
        self._y = value
    # el movimiento de mrpatiwi es aleatorio, cuando llega a una esquina decide si moverse hacie arriba abajo derecha
    # izquierda etc
    def tryMove(self):

        if (self.x, self.y) == (self.parent.pocmon.x, self.parent.pocmon.y):
            self.parent.pocmon.muerto()


        if self.direccion == "Izquierda":
            if self.parent.chequear_pixel(self.x-1, self.y) and self.parent.chequear_pixel(self.x-1, self.y+24):
                self.move(self.x - 1, self.y)
                self.x -= 1
            else:
                if (self.y-30) % 25 >= 20:
                    self.move(self.x, self.y + (25-((self.y-30) % 25)))
                    self.y += (25-((self.y-30) % 25))
                    self.direccion = random.choice(["Derecha", "Arriba", "Abajo"])
                elif (self.y-30) % 25 <= 5:
                    self.move(self.x, self.y - ((self.y-30) % 25))
                    self.y -= ((self.y-30) % 25)
                    self.direccion = random.choice(["Derecha", "Arriba", "Abajo"])


        if self.direccion == "Derecha":
            if self.parent.chequear_pixel(self.x+24+1, self.y) and self.parent.chequear_pixel(self.x+24+1, self.y+24):
                self.move(self.x + 1, self.y)
                self.x += 1
            else:
                if (self.y-30) % 25 >= 20:
                    self.move(self.x, self.y + (25-((self.y-30) % 25)))
                    self.y += (25-((self.y-30) % 25))
                    self.direccion = random.choice(["Izquierda", "Arriba", "Abajo"])
                elif (self.y-30) % 25 <= 5:
                    self.move(self.x, self.y - ((self.y-30) % 25))
                    self.y -= ((self.y-30) % 25)
                    self.direccion = random.choice(["Izquierda", "Arriba", "Abajo"])

        if self.direccion == "Arriba":
            if self.parent.chequear_pixel(self.x, self.y-1) and self.parent.chequear_pixel(self.x+24, self.y-1):
                self.move(self.x, self.y - 1)
                self.y -= 1
            else:
                if (self.x-30) % 25 >= 20:
                    self.move(self.x + (25-((self.x-30) % 25)), self.y)
                    self.x += (25-((self.x-30) % 25))
                    self.direccion = random.choice(["Izquierda", "Derecha", "Abajo"])
                elif (self.x-30) % 25 <= 5:
                    self.move(self.x - ((self.x-30) % 25), self.y)
                    self.x -= ((self.x-30) % 25)
                    self.direccion = random.choice(["Izquierda", "Derecha", "Abajo"])

        if self.direccion == "Abajo":
            if self.parent.chequear_pixel(self.x, self.y+24+1) and self.parent.chequear_pixel(self.x+24, self.y+24+1):
                self.move(self.x, self.y + 1)
                self.y += 1
            else:
                if (self.x-30) % 25 >= 20:
                    self.move(self.x + (25-((self.x-30) % 25)), self.y)
                    self.x += (25-((self.x-30) % 25))
                    self.direccion = random.choice(["Izquierda", "Derecha", "Arriba"])
                elif (self.x-30) % 25 <= 5:
                    self.move(self.x - ((self.x-30) % 25), self.y)
                    self.x -= ((self.x-30) % 25)
                    self.direccion = random.choice(["Izquierda", "Derecha", "Arriba"])

# cuando muere el pocmon
    def pocmon_muere(self):
        self.parent.pocmon.alive = False
        self.rest = True
        self.move(self.parent.patiwi_x, self.parent.patiwi_y)
        self.x = self.parent.patiwi_x
        self.y = self.parent.patiwi_y


class thread_patiwi(QtCore.QThread):
    trigger = QtCore.pyqtSignal()

    def __init__(self, parent):
        super(thread_patiwi, self).__init__(parent)
        self.alive = True
        self.parent = parent

    def __del__(self):
        self.wait()

    def run(self):
        time.sleep(4)
        self.parent.move(self.parent.parent.start_x, self.parent.parent.start_y)
        self.parent.x = self.parent.parent.start_x
        self.parent.y = self.parent.parent.start_y
        while self.parent.parent.pocmon.vidas >= 0:
            if not self.parent.parent.paused:
                time.sleep(0.01)
                self.trigger.emit()
            if self.parent.rest:
                time.sleep(5)
                self.parent.rest = False