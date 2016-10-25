__author__ = 'Ignacio'
from PyQt4 import QtGui, uic
import random

lista_clases = uic.loadUiType("interfaz.ui")

class MainWindow(lista_clases[0], lista_clases[1]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_nuevo_juego.clicked.connect(self.poner_signos)
        self.btn_resultado.clicked.connect(self.resultado)



    def poner_signos(self):
        signos = ["suma", "resta", "multiplicacion", "division"]
        signos_1 = {"suma":"+","resta":"-", "multiplicacion":"*", "division":"/" }
        for rb_id in signos:
            if getattr(self, 'rbt_' + str(rb_id)).isChecked():
                self.label_signo.setText("{0}".format(signos_1[rb_id]))
                self.calcular()


    def calcular(self):
        if self.label_signo.text() == "+":
            self.primer_num.setText(str(random.randint(0, 20)))
            self.segundo_num.setText(str(random.randint(0, 20)))

        if self.label_signo.text() == "-":
            self.primer_num.setText(str(random.randint(0,20)))
            self.segundo_num.setText(str(random.randint(0,int(self.primer_num.text()))))

        if self.label_signo.text() == "*":
            self.primer_num.setText(str(random.randint(0,20)))
            self.segundo_num.setText(str(random.randint(0,20)))

        if self.label_signo.text() == "/":
            self.primer_num.setText(str(random.randint(0,20)))
            self.segundo_num.setText(str(random.randint(1,20)))



    def resultado(self):
        if self.label_signo.text() == "+":
            solucion = int(self.primer_num.text()) + int(self.segundo_num.text())

        if self.label_signo.text() == "-":
            solucion = int(self.primer_num.text()) - int(self.segundo_num.text())

        if self.label_signo.text() == "*":
            solucion = int(self.primer_num.text()) * int(self.segundo_num.text())

        if self.label_signo.text() == "/":
            solucion = int(self.primer_num.text()) // int(self.segundo_num.text())

        if solucion == int(self.ingreso_resultado.text()):
            QtGui.QMessageBox.question(self, "", "Esta Correcto",QtGui.QMessageBox.Accepted)
            return
        elif solucion != int(self.ingreso_resultado.text()):
            QtGui.QMessageBox.question(self, "", "Incorrecto:\n {0}{1}{2}={3}".format(self.primer_num.text(),
                                                                                      self.label_signo.text(),
                                                                                      self.segundo_num.text(),
                                                                                      solucion),
                                       QtGui.QMessageBox.Accepted)
            return


if __name__ == '__main__':
    app = QtGui.QApplication([])
    form = MainWindow()
    form.show()
    app.exec_()