__author__ = 'Ignacio'
from PyQt4 import QtGui, QtCore
import os, sys, time, random, datetime, pickle
import time
from Pocmon import Pocmon
from Monedas import Amarilla, Roja, Verde, Azul
from Timer import Timer
from mrpatiwi import Mrpatiwi
from belenciwi import Belenciwi
from jaimiwi import Jaimiwi
from marquiwi import Marquiwi


# clase principal
class Juego(QtGui.QMainWindow):
    def __init__(self):
        super(Juego, self).__init__()

        self.initUI()
# menu del juego

    def initUI(self):

        self._tboard = None

        self.titulo = QtGui.QLabel(self)
        self.titulo.setText("POC-MON")
        self.titulo.setGeometry(350, 100, 120, 50)
        self.titulo.sizeHint()

        self.boton1 = QtGui.QPushButton(self)
        self.boton1.setText("NUEVA PARTIDA")
        self.boton1.setGeometry(200, 300, 120, 50)

        self.boton2 = QtGui.QPushButton(self)
        self.boton2.setText("CARGAR PARTIDA")
        self.boton2.setGeometry(350, 300, 120, 50)

        self.boton3 = QtGui.QPushButton(self)
        self.boton3.setText("GUARDAR PARTIDA")
        self.boton3.setGeometry(500, 300, 120, 50)

        self.layout = QtGui.QFrame(self)
        self.layout.setGeometry(30, 30, 400, 700)
        self.texto = QtGui.QLineEdit(self)
        self.texto.setGeometry(500, 300, 120, 30)
        self.boton4 = QtGui.QPushButton(self)
        self.boton4.setGeometry(620, 300, 120, 30)
        self.boton4.setText("CARGAR")
        self.texto.hide()
        self.boton4.hide()
        self.layout.hide()

        self.boton1.clicked.connect(self.nueva_partida)
        self.boton2.clicked.connect(self.cargar_partida)
        self.boton3.clicked.connect(self.guardar_partida)

        self.statusbar = self.statusBar()

        self.resize(800, 600)
        self.center()
        self.setWindowTitle('Poc-Mon')
        self.show()

    @property
    def tboard(self):
        return self._tboard
    @tboard.setter
    def tboard(self, value):
        self._tboard = value


    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2,
                  (screen.height() - size.height()) / 2)

    def nueva_partida(self):
        self.titulo.hide()
        self.boton1.hide()
        self.boton2.hide()
        self.boton3.hide()
        self.tboard = Board(self)
        self.tboard.setLineWidth(1)
        self.tboard.setMidLineWidth(3)
        self.tboard.setFrameShape(0x0002)
        self.setStyleSheet("background-color: white")
        self.setCentralWidget(self.tboard)

    def guardar_partida(self):
        if self.tboard is None:
            return

        else:
            fecha = str(datetime.datetime.now())
            fecha = fecha.replace(" ", "_")
            fecha = fecha.replace(".", "-")
            fecha = fecha.replace(":", "-")
            with open("partidas\\{0}.pocmon".format(fecha), "wb") as file:
                pickle.dump(self.tboard, file)

    def cargar_partida(self):
        self.titulo.hide()
        self.boton1.hide()
        self.boton2.hide()
        self.boton3.hide()
        lista = []
        for i in range(len(os.listdir("partidas"))):
            lista.append(QtGui.QLabel(self.layout))
            lista[-1].setText("{1}.- {0}".format(os.listdir("partidas")[i],i))
            lista[-1].setGeometry(10, 10+i*10, 300, 20)
        self.layout.show()
        self.boton4.show()
        self.texto.show()
        self.boton4.clicked.connect(self.cargar)

    def cargar(self):
        try:
            archivo = os.listdir("partidas")[int(self.texto.text())]
        except IndexError:
            return
        except ValueError:
            return
        with open("partidas\\{0}".format(archivo), "rb") as file:
            partida_1 = pickle.load(file)
        self.layout.hide()
        self.boton4.hide()
        self.texto.hide()
        self.tboard = partida_1
        self.tboard.setLineWidth(1)
        self.tboard.setMidLineWidth(3)
        self.tboard.setFrameShape(0x0002)
        self.setStyleSheet("background-color: white")
        self.setCentralWidget(self.tboard)



# clase, en donde se ejecuta el juego en si
class Board(QtGui.QFrame):
    msg2Statusbar = QtCore.pyqtSignal(str)


    def __init__(self, parent):
        super(Board, self).__init__(parent)
        self.parent = parent
        self.initBoard()

    def initBoard(self):
        self.paused = False
        self.esquina = 30
        self.ancho = 475
        self.largo = 525
        self.puntos = 0
        # cada uno de los pacman, fantasmas.
        self.pocmon = Pocmon(self)
        self.patiwi = Mrpatiwi(self)
        self.belenciwi = Belenciwi(self)
        self.jaimiwi = Jaimiwi(self)
        self.marquiwi = Marquiwi(self)
        # se lee el mapa
        self.mapa = list(map(lambda l: l.strip(), [line for line in open("mapa.txt", "r")]))
        self.monedas = dict()
        for i in range(len(self.mapa)):
            for j in range(len(self.mapa[0])):
                if self.mapa[i][j] == "I":
                    self.pocmon_x = j*25 + 30 # guardar la pos.x inicial del pocmon
                    self.pocmon_y = i*25 + 30 # guarad la pos.y inicial del pocmon
                    self.pocmon.x = j*25 + 30 # setea la pos del pocmon
                    self.pocmon.y = i*25 + 30
                elif self.mapa[i][j] == " ":
                    a = random.random()
                    if a >= 0.9:
                        self.monedas[(j*25 + 30, i*25+30)] = Roja(j, i, self)
                    elif a < 0.9:
                        self.monedas[(j*25+30, i*25+30)] = Amarilla(j, i, self, 10)
                elif self.mapa[i][j] == "P":
                    self.patiwi_x = j*25 + 30 # guardar la pos.x inicial de patiwi
                    self.patiwi_y = i*25 + 30 # guarad la pos.y inicial de patiwi
                    self.patiwi.x = j*25 + 30 # setea la pos de patiwi
                    self.patiwi.y = i*25 + 30
                elif self.mapa[i][j] == "B":
                    self.belenciwi_x = j*25 + 30 # guardar la pos.x inicial
                    self.belenciwi_y = i*25 + 30 # guarad la pos.y inicial
                    self.belenciwi.x = j*25 + 30 # setea la pos de patiwi
                    self.belenciwi.y = i*25 + 30
                elif self.mapa[i][j] == "J":
                    self.jaimiwi_x = j*25 + 30 # guardar la pos.x inicial
                    self.jaimiwi_y = i*25 + 30 # guarad la pos.y inicial
                    self.jaimiwi.x = j*25 + 30 # setea la pos de patiwi
                    self.jaimiwi.y = i*25 + 30
                elif self.mapa[i][j] == "M":
                    self.marquiwi_x = j*25 + 30 # guardar la pos.x inicial
                    self.marquiwi_y = i*25 + 30 # guarad la pos.y inicial
                    self.marquiwi.x = j*25 + 30 # setea la pos de patiwi
                    self.marquiwi.y = i*25 + 30
                elif self.mapa[i][j] == "S":
                    self.start_x = j*25 + 30
                    self.start_y = i*25 + 30 - 25



        # se setean los fanstasmas + pocmon
        self.pocmon.setGeometry(self.pocmon_x, self.pocmon_y, self.pocmon.lado, self.pocmon.lado)
        self.patiwi.setGeometry(self.patiwi_x, self.patiwi_x, self.patiwi.lado, self.patiwi.lado)
        self.belenciwi.setGeometry(self.belenciwi_x, self.belenciwi_y, self.belenciwi.lado, self.belenciwi.lado)
        self.jaimiwi.setGeometry(self.jaimiwi_x, self.jaimiwi_y, self.jaimiwi.lado, self.jaimiwi.lado)
        self.marquiwi.setGeometry(self.marquiwi_x, self.marquiwi_y, self.marquiwi.lado, self.marquiwi.lado)
        self.pocmon.show()
        self.patiwi.show()
        self.belenciwi.show()
        self.jaimiwi.show()
        self.marquiwi.show()

        # etiquetas del tiempo, puntaje, vidas etc
        self.tiempo = QtGui.QLabel(self)
        self.tiempo.setGeometry(550, 120, 50, 30)
        self.tiempo.setText("Tiempo:")
        self.tiempo.show()

        self.timer = Timer(self)
        self.timer.setGeometry(600, 120, 30, 30)
        self.timer.show()

        self.puntaje = QtGui.QLabel(self)
        self.puntaje.setGeometry(550, 80, 50, 30)
        self.puntaje.setText("Puntaje:")
        self.contador = QtGui.QLabel(self)
        self.contador.setGeometry(600, 80, 30, 30)
        self.contador.setText(str(self.puntos))
        self.puntaje.show()
        self.contador.show()

        self.texto_vidas = QtGui.QLabel(self)
        self.texto_vidas.setGeometry(550, 160, 50, 30)
        self.texto_vidas.setText("Vidas:")
        self.vidas = QtGui.QLabel(self)
        self.vidas.setGeometry(600, 160, 50, 30)
        self.vidas.setText(str(self.pocmon.vidas))
        self.vidas.show()
        self.texto_vidas.show()

        self.setFocusPolicy(QtCore.Qt.StrongFocus)


    def keyPressEvent(self, event):

        key = event.key()
        if key == QtCore.Qt.Key_Left:
            if self.chequear_pixel(self.pocmon.x-1,self.pocmon.y+5) and \
                    self.chequear_pixel(self.pocmon.x-1, self.pocmon.y+24-5):
                self.pocmon.direccion = "Izquierda"


        if key == QtCore.Qt.Key_Right:
            if self.chequear_pixel(self.pocmon.x+24+1, self.pocmon.y+5) and \
                    self.chequear_pixel(self.pocmon.x+24+1, self.pocmon.y+24-5):
                self.pocmon.direccion = "Derecha"


        if key == QtCore.Qt.Key_Down:
            if self.chequear_pixel(self.pocmon.x+5, self.pocmon.y+24+1) and \
                    self.chequear_pixel(self.pocmon.x+24-5, self.pocmon.y+24+1):
                self.pocmon.direccion = "Abajo"


        if key == QtCore.Qt.Key_Up:
            if self.chequear_pixel(self.pocmon.x+5, self.pocmon.y-1) and \
                    self.chequear_pixel(self.pocmon.x+24-5, self.pocmon.y-1):
                self.pocmon.direccion = "Arriba"

        if key == QtCore.Qt.Key_P:
            if not self.paused:
                self.paused = True
                self.mostrar_menu_pausa()
            elif self.paused:
                self.paused = False
                self.parent.titulo.hide()
                self.parent.boton1.hide()
                self.parent.boton2.hide()
                self.parent.boton3.hide()
# menu pausa
    def mostrar_menu_pausa(self):
        self.boton5 = QtGui.QPushButton(self)
        self.boton5.setText("NUEVA PARTIDA")
        self.boton5.setGeometry(550, 300, 120, 50)
        self.boton5.show()

        self.boton6 = QtGui.QPushButton(self)
        self.boton6.setText("CARGAR PARTIDA")
        self.boton6.setGeometry(550, 400, 120, 50)
        self.boton6.show()

        self.boton7 = QtGui.QPushButton(self)
        self.boton7.setText("GUARDAR PARTIDA")
        self.boton7.setGeometry(550, 500, 120, 50)
        self.boton7.show()

        self.boton5.clicked.connect(self.nueva_partida)
        self.boton6.clicked.connect(self.cargar_partida)
        self.boton7.clicked.connect(self.parent.guardar_partida)

    def nueva_partida(self):
        self.boton5.hide()
        self.boton6.hide()
        self.boton7.hide()
        self.monedas = {}
        for i in range(len(self.mapa)):
            for j in range(len(self.mapa[0])):

                if self.mapa[i][j] == " ":
                    a = random.random()
                    if a >= 0.9:
                        self.monedas[(j*25 + 30, i*25+30)] = Roja(j, i, self)
                    elif a < 0.9:
                        self.monedas[(j*25+30, i*25+30)] = Amarilla(j, i, self, 10)
        self.pocmon.move(self.pocmon_x, self.pocmon_y)
        self.timer.contador = 0
        self.pocmon.vidas = 3
        self.vidas.setText(str(self.pocmon.vidas))
        self.timer.setText(str(self.timer.contador))
        self.puntos = 0
        self.contador.setText(str(self.puntos))
        self.update()
        self.paused = False




    def cargar_partida(self):
        self.boton5.hide()
        self.boton6.hide()
        self.boton7.hide()
        self.pacman.alive = False
        self.parent.cargar_partida()


    def guardar_partida(self):
        self.paren.guardar_partida()

    def paintEvent(self, event):
        # dibuja el laberinto
        painter = QtGui.QPainter()
        painter.begin(self)
        for i in range(len(self.mapa)):
            for j in range(len(self.mapa[0])):
                if self.mapa[i][j] == "#":
                    painter.fillRect(25 * j + 30, 25 * i + 30, 25, 25, 9)
                if self.mapa[i][j] == "G":
                    painter.fillRect(25 * j + 40, 25 * i + 30, 10, 25, 13)
        for n in self.monedas:
            if isinstance(self.monedas[n], Amarilla):
                painter.fillRect(self.monedas[n].x+10, self.monedas[n].y+10, 5, 5, 18)
            elif isinstance(self.monedas[n], Roja):
                painter.fillRect(self.monedas[n].x+10, self.monedas[n].y+10, 5, 5, 7)

        painter.drawLine(self.esquina, self.esquina, self.esquina, self.esquina+self.largo)
        painter.drawLine(self.esquina, self.esquina, self.esquina+self.ancho, self.esquina)
        painter.drawLine(self.esquina, self.esquina+self.largo, self.esquina+self.ancho, self.esquina+self.largo)
        painter.drawLine(self.esquina+self.ancho, self.esquina+self.largo, self.esquina+self.ancho, self.esquina)

        painter.end()
 # funcion que cheuquea q tipo de pixel es segun la posicion, es decir muralla o camino
    def chequear_pixel(self, x, y):
        if self.mapa[int((y-30)//25)][int((x-30)//25)] == " " or self.mapa[int((y-30)//25)][int((x-30)//25)] == "I":
            return True
        else:
            return False


def main():
    app = QtGui.QApplication([])
    pacman = Juego()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()















