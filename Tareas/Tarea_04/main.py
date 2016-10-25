__author__ = 'Ignacio'

from PyQt4 import QtCore, QtGui, uic
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QPainter, QBrush, QPen
from drag import DropBox, DraggableWidget
from Clases import Numero, Instanciar, Output
from math import pi, e


lista_clases = uic.loadUiType("interfaz.ui")

# Ventana Principal
class MainWindow(lista_clases[0], lista_clases[1]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.botones = list()  # lista de botones o "numeros" dentro del area de trabajo
        self.dropbox = DropBox(self)  # area de trabajo
        self.dropbox.setLineWidth(1)
        self.dropbox.setMidLineWidth(3)
        self.dropbox.setFrameShape(0x0002)
        self.dropbox.setGeometry(180, 90, 580, 470)  # Dimensiones del area de trabajo
        self.numeros = {"pi": pi, "e": e}
        # Lista de operaciones
        self.lista = {self.radio_suma: "+", self.radio_resta: "-", self.radio_multiplicacion: "*",
                      self.radio_division: "/", self.radio_potencia: "x^n",
                      self.radio_absoluto: "||", self.radio_ln: "ln()",
                      self.radio_sen: "sen()", self.radio_cos: "cos()", self.radio_tan: "tan()",
                      self.radio_minimo: "min()", self.radio_maximo: "max()"}
        self.entradas_lista = True  # si esque hay entradas aun no conectadas
        self.push_add.clicked.connect(self.agregar_block)
        self.conexiones.clicked.connect(self.crear_conexiones)
        self.del_boton.clicked.connect(self.borrar_botones)

    # Esta funcion agregar bloques al area de trabajo segun que operacion esta seleccionada
    def agregar_block(self):
        if self.radio_input.isChecked():
            if self.lineEdit.text() in self.numeros:  # si el numero a agregar el pi o e
                self.botones.append(DraggableWidget(self.dropbox))
                self.botones[-1].label2.setText(self.lineEdit.text())
                self.botones[-1].setGeometry(10, 10, 40, 40)
                self.botones[-1].tipo = Numero(self.numeros[self.lineEdit.text()])
                self.botones[-1].show()
            elif self.lineEdit.text().isdigit() or self.lineEdit.text().isdecimal() or self.lineEdit.text().isalnum():
                self.botones.append(DraggableWidget(self.dropbox))
                self.botones[-1].label2.setText(self.lineEdit.text())
                self.botones[-1].setGeometry(10, 10, 40, 40)
                self.botones[-1].tipo = Numero(float(self.lineEdit.text()))
                self.botones[-1].show()

        elif self.radio_output.isChecked():  # Agregar un Output
            self.botones.append(DraggableWidget(self.dropbox))
            self.botones[-1].label2.setText("output")
            self.botones[-1].setGeometry(10, 10, 40, 40)
            self.botones[-1].tipo = Output()
            self.botones[-1].show()
            self.chequear_conexiones()

        else:  # agregar una operacion
            for i in self.lista:
                if i.isChecked():
                    self.botones.append(DraggableWidget(self.dropbox))
                    self.botones[-1].label2.setText(self.lista[i])
                    Instanciar(self.lista[i], self.botones[-1]) # Se define la clase a la que corresponde el bloque
                    print(self.botones[-1].tipo.hijos)
                    self.botones[-1].setGeometry(10, 10, 40, 40)
                    self.botones[-1].show()
                    self.chequear_conexiones()

    # se crean las conexiones entre los bloques que estan seleccionados
    def crear_conexiones(self):
        for i in self.botones:
            if i.checkbox.isChecked() and i.label2.text() in self.lista.values():
                for n in self.botones:
                    if n.checkbox.isChecked() and n.label2.text() not in self.lista.values()\
                            and n.label2.text() != "output":
                        if i.tipo.agregar_hijo(
                                n.tipo.valor) is False:  # se chequean que el valor ingresado sea correcto
                            # Si el usuario quiere ingresar un valor prohibido aparece la siguiente ventana
                            QtGui.QMessageBox.question(self, "", i.tipo.msje_entradas, QtGui.QMessageBox.Accepted)
                        else:
                            i.tipo.hijos.append(n)
                            self.update()
                i.tipo.operacion()
                for j in self.botones:
                    if j.checkbox.isChecked() and j.label2.text().isalpha():
                        j.tipo.hijos.append(i)
                        j.tipo.valor = i.tipo.valor
                        j.label2.setText(str(j.tipo.valor))
                        self.update()
        for m in self.botones:
            m.checkbox.setChecked(False)
        self.entradas_lista = True
        # Checkeamos si todas las entradas estan conectadas
        self.chequear_conexiones()

    # Revisa si todas las entradas estan conectadas
    def chequear_conexiones(self):
        for k in self.botones:
            if k.label2.text() in self.lista.values() or k.label2.text().isalpha():
                if len(k.tipo.hijos) < k.tipo.entradas:
                    self.entradas_lista = False
        if not self.entradas_lista:
            self.label_3.setText("No")
        else:
            self.label_3.setText("Si")

    # funcion para borrar botones seleccionados
    def borrar_botones(self):
        for i in self.botones:
            if i.checkbox.isChecked():
                i.deleteLater()
                self.botones.remove(i)
                self.update()

    # Se pintan las lineas entre los bloques que tienen conexiones:
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        for i in self.botones:
            if not isinstance(i.tipo, Numero):
                for j in i.tipo.hijos:
                    if j in self.botones:
                        painter.drawLine(i.pos[0] + 180, i.pos[1] + 20 + 90, j.pos[0] + 180 + 20, j.pos[1] + 90 + 20)
        painter.end()


if __name__ == '__main__':
    app = QtGui.QApplication([])
    form = MainWindow()
    form.show()
    app.exec_()