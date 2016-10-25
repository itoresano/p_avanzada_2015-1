__author__ = 'Ignacio'


import socket
import sys
import threading
from PyQt4 import QtGui, QtCore
import time

class Cliente(QtGui.QWidget):

    def __init__(self, usuario, parent = None):
        super(Cliente, self).__init__(parent)
        self.usuario = usuario
        self.host = '127.0.0.1'
        self.port = 3490
        self.nombre = usuario
        self.s_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s_cliente.connect((self.host, self.port))
        except socket.error:
            print("No fue posible realizar la conexión")
            sys.exit()
        self.layout = QtGui.QGridLayout(self)
        self.lineEdit = QtGui.QLineEdit(self)
        self.send = QtGui.QPushButton(self)
        self.send.setText("Enviar")
        self.layout.addWidget(self.lineEdit, 0, 0)
        self.layout.addWidget(self.send, 0, 1)
        self.chat = []
        self.n = 1
        self.thread = thread(self)
        self.thread.daemon = True
        self.thread.trigger.connect(self.escuchar)
        self.thread.start()

        self.send.clicked.connect(self.mensaje)

    def mensaje(self):
        self.enviar(self.lineEdit.text())

    def escuchar(self):
        data = self.s_cliente.recv(4096)
        if data:
            self.chat.append(QtGui.QLabel(self))
            self.chat[-1].setText(data.decode("ascii"))
            self.layout.addWidget(self.chat[-1], self.n, 0)
            self.n += 1
            self.lineEdit.clear()


    def enviar(self, mensaje):
        msj_final = self.usuario + ": " + mensaje
        self.s_cliente.send(msj_final.encode('ascii'))

# thread que maneja la funcion escuchar
class thread(QtCore.QThread):
    trigger = QtCore.pyqtSignal()

    def __init__(self, parent):
        super(thread, self).__init__(parent)
        self.parent = parent

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            time.sleep(0.5)
            self.trigger.emit()
