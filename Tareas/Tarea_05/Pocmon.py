__author__ = 'Ignacio'
from PyQt4 import QtCore, QtGui
import os, time

# Pocmon
class Pocmon(QtGui.QLabel):
    def __init__(self, parent):
        QtGui.QWidget.__init__(self, parent)
        self.parent = parent
        self.lado = 25
        self.setPixmap(QtGui.QPixmap(os.getcwd() + "\\Imagenes\\pocmon - copia.png"))
        self._x = 55
        self._y = 55
        self.alive = True
        self.direccion = None
        self.vidas = 3
        self.thread = thread(self)
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
# funcion que revisa si esque el pacman se puede mover en una direccion o no, tambien, re ajusta la posicion del pacman
# para que pueda "doblar" si esque las flechas se aprietan 5 pixeles antes o despues de que el pacman este justo
    # en la esquina
    def tryMove(self):
        if (self.x, self.y) in self.parent.monedas.keys():
            self.parent.monedas[(self.x, self.y)].atrapada()
            del self.parent.monedas[self.x, self.y]
            self.parent.update()

        if self.direccion == "Izquierda":
            if self.parent.chequear_pixel(self.x-1, self.y) and self.parent.chequear_pixel(self.x-1, self.y+24):
                self.move(self.x - 1, self.y)
                self.x -= 1
            else:
                if (self.y-30) % 25 >= 20:
                    self.move(self.x, self.y + (25-((self.y-30) % 25)))
                    self.y += (25-((self.y-30) % 25))
                elif (self.y-30) % 25 <= 5:
                    self.move(self.x, self.y - ((self.y-30) % 25))
                    self.y -= ((self.y-30) % 25)
        if self.direccion == "Derecha":
            if self.parent.chequear_pixel(self.x+24+1, self.y) and self.parent.chequear_pixel(self.x+24+1, self.y+24):
                self.move(self.x + 1, self.y)
                self.x += 1
            else:
                if (self.y-30) % 25 >= 20:
                    self.move(self.x, self.y + (25-((self.y-30) % 25)))
                    self.y += (25-((self.y-30) % 25))
                elif (self.y-30) % 25 <= 5:
                    self.move(self.x, self.y - ((self.y-30) % 25))
                    self.y -= ((self.y-30) % 25)
        if self.direccion == "Arriba":
            if self.parent.chequear_pixel(self.x, self.y-1) and self.parent.chequear_pixel(self.x+24, self.y-1):
                self.move(self.x, self.y - 1)
                self.y -= 1
            else:
                if (self.x-30) % 25 >= 20:
                    self.move(self.x + (25-((self.x-30) % 25)), self.y)
                    self.x += (25-((self.x-30) % 25))
                elif (self.x-30) % 25 <= 5:
                    self.move(self.x - ((self.x-30) % 25), self.y)
                    self.x -= ((self.x-30) % 25)
        if self.direccion == "Abajo":
            if self.parent.chequear_pixel(self.x, self.y+24+1) and self.parent.chequear_pixel(self.x+24, self.y+24+1):
                self.move(self.x, self.y + 1)
                self.y += 1
            else:
                if (self.x-30) % 25 >= 20:
                    self.move(self.x + (25-((self.x-30) % 25)), self.y)
                    self.x += (25-((self.x-30) % 25))
                elif (self.x-30) % 25 <= 5:
                    self.move(self.x - ((self.x-30) % 25), self.y)
                    self.x -= ((self.x-30) % 25)

    #cuando el pacman muere
    def muerto(self):
        if self.vidas > 0:
            self.vidas -= 1
            self.parent.vidas.setText(str(self.vidas))
            self.direccion = None
            self.move(self.parent.pocmon_x, self.parent.pocmon_y)
            print(self.parent.pocmon_x, self.parent.pocmon_y)
            self.x = self.parent.pocmon_x
            self.y = self.parent.pocmon_y
            self.parent.belenciwi.pocmon_muere()
            self.parent.patiwi.pocmon_muere()
            self.parent.marquiwi.pocmon_muere()
            self.parent.jaimiwi.pocmon_muere()
        if self.vidas < 0:
            self.alive = False


#thread que maneja el movimiento del pacman, 1 pixel, cada 0,01 segundo
class thread(QtCore.QThread):
    trigger = QtCore.pyqtSignal()

    def __init__(self, parent):
        super(thread, self).__init__(parent)
        self.parent = parent

    def __del__(self):
        self.wait()

    def run(self):
        while self.parent.vidas >= 0:
            if not self.parent.parent.paused:
                time.sleep(0.01)
                self.trigger.emit()
            if self.parent.alive is False:
                time.sleep(3)
                self.alive = True