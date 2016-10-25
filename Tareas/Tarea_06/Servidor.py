__author__ = 'Ignacio'

import re
import socket
import sys
import threading
from PyQt4 import QtGui, QtCore
import time

class Servidor:

    def __init__(self, usuario):
        self.usuario = usuario
        self.host = '127.0.0.1'
        self.port = 3490
        self.s_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s_servidor.bind((self.host, self.port))
        self.s_servidor.listen(1000)
        aceptador = threading.Thread(target=self.aceptar, args=())
        aceptador.daemon = True
        aceptador.start()

        self.cliente = {}

    def escuchar(self, cliente):
        while True:
            data = cliente.recv(4096)
            for i in self.cliente:
                self.cliente[i].send(data)


    def aceptar(self):
        while True:
            cliente_nuevo, address = self.s_servidor.accept()
            self.cliente[cliente_nuevo] = cliente_nuevo
            thread_cliente = threading.Thread(
                target=self.escuchar, args=(self.cliente[cliente_nuevo],))
            thread_cliente.daemon = True
            thread_cliente.start()
            print("cliente")




