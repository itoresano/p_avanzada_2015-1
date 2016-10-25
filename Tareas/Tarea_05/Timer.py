__author__ = 'Ignacio'
from PyQt4 import QtCore, QtGui
import os, time
# clase que controla el tiempo del programa
class Timer(QtGui.QLabel):
    def __init__(self, parent):
        QtGui.QWidget.__init__(self, parent)
        self.parent = parent
        self.contador = 0
        self.setText(str(self.contador))
        self.tiempo = ThreadTimer(self)
        self.tiempo.trigger.connect(self.avanzar_tiempo)
        self.tiempo.start()

    def avanzar_tiempo(self):
        self.contador += 1
        self.setText(str(self.contador))


class ThreadTimer(QtCore.QThread):
    trigger = QtCore.pyqtSignal()

    def __init__(self, parent):
        super(ThreadTimer, self).__init__(parent)
        self.parent = parent


    def run(self):
        while self.parent.parent.pocmon.vidas >= 0:
            if not self.parent.parent.paused:
                time.sleep(1)
                self.trigger.emit()