__author__ = 'Ignacio'
from PyQt4 import QtGui, QtCore


def is_par(num):
    if num % 2 == 0:
        return True
    else:
        return False


def jugador(num):
    if num % 2 == 0:
        return "Jugador X"
    else:
        return "Jugador O"


class MiFormulario(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.init_GUI()

    def init_GUI(self):
        ''' Aquí se crea la grilla para ubicar los Widget de manera matricial'''
        grilla = QtGui.QGridLayout()
        self.setLayout(grilla)
        self.setGeometry(300, 150, 120, 140)

        self.contador = 0

        self.label1 = QtGui.QLabel('Turno {0}'.format(jugador(self.contador)), self)
        self.label1.move(10, 115)

        valores = [' ', ' ', ' ',
                   ' ', ' ', ' ',
                   ' ', ' ', ' ']

        posicion = [(i, j) for i in range(3) for j in range(3)]

        for posicion, valor in zip(posicion, valores):
            boton = QtGui.QPushButton(" ", self)
            boton.clicked.connect(self.boton_presionado)
            grilla.addWidget(boton, *posicion)

        self.move(300, 150)
        self.setWindowTitle('Gato')
        self.show()

    def alguien_gano(self):
        pass
    def boton_presionado(self):
        sender = self.sender()
        if is_par(self.contador) and sender.text() == " ":
            print(self.contador)
            sender.setText("X")
            self.contador += 1
            self.label1.setText('Turno {0}'.format(jugador(self.contador)))
        elif not is_par(self.contador) and sender.text() == " ":
            print(self.contador)
            sender.setText("O")
            self.contador += 1
            self.label1.setText('Turno {0}'.format(jugador(self.contador)))
        else:
            pass


if __name__ == '__main__':
    app = QtGui.QApplication([])

    ''' Se crea una ventana descendiente de QMainWindows'''
    form = MiFormulario()
    form.show()
    app.exec_()