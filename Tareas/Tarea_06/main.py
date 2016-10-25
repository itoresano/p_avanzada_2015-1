__author__ = 'Ignacio'

from PyQt4 import QtCore, QtGui
import sys
from hashnsalt import hash_salt, check_password
import pickle
import re
import Servidor
import threading
from Cliente import Cliente
from Servidor import Servidor
nombre = "server"
server = Servidor(nombre)
class Inicio(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Inicio, self).__init__(parent)

        self.userNameText = QtGui.QLineEdit(self)
        self.passwordNameText = QtGui.QLineEdit(self)

        self.pushButtonWindow = QtGui.QPushButton(self)
        self.pushButtonWindow.setText("Iniciar Sesión")
        self.pushButtonSign = QtGui.QPushButton(self)
        self.pushButtonSign.setText("Crear cuenta nueva")

        self.usernameLabel = QtGui.QLabel("Username", self)
        self.passwordLabel = QtGui.QLabel("Password", self)
        self.signinLabel = QtGui.QLabel("¿No tienes una cuenta?")

        self.layout = QtGui.QVBoxLayout(self)
        self.layout.addWidget(self.usernameLabel)
        self.layout.addWidget(self.userNameText)
        self.layout.addWidget(self.passwordLabel)
        self.layout.addWidget(self.passwordNameText)
        self.layout.addWidget(self.pushButtonWindow)
        self.layout.addWidget(self.signinLabel)
        self.layout.addWidget(self.pushButtonSign)

        self.pushButtonWindow.clicked.connect(self.login)
        self.pushButtonSign.clicked.connect(self.signin)




    def login(self):
        real = False
        with open("passwords.420", "rb") as f:
            usuarios = pickle.load(f)
        if self.userNameText.text() not in usuarios.keys():
            QtGui.QMessageBox.question(self, "", "la contraseña o el usuario son invalidos",QtGui.QMessageBox.Accepted)
            return
        else:
            for i in usuarios:
                if check_password(usuarios[i], self.passwordNameText.text()) and self.userNameText.text() == i:
                    real = True
                    print("correcto")
            if not real:
                QtGui.QMessageBox.question(self, "", "la contraseña o el usuario son invalidos",QtGui.QMessageBox.Accepted)
                return
        self.hide()
        self.cliente = Cliente(self.userNameText.text())
        self.hide()

        self.cliente.show()

    def signin(self):
        self.signin = Signin()
        self.hide()
        self.signin.show()

class Signin(QtGui.QWidget):
    def __init__(self, parent=None):
        super(Signin, self).__init__(parent)

        self.mailLabel = QtGui.QLabel("e-mail uc", self)
        self.usernameLabel = QtGui.QLabel("Username", self)
        self.passwordLabel = QtGui.QLabel("Password", self)
        self.passwordLabel2 = QtGui.QLabel("Password", self)

        self.mailText = QtGui.QLineEdit(self)
        self.userNameText = QtGui.QLineEdit(self)
        self.passwordNameText = QtGui.QLineEdit(self)
        self.passwordNameText2 = QtGui.QLineEdit(self)

        self.pushButtonWindow = QtGui.QPushButton(self)
        self.pushButtonWindow.setText("Sign in!")

        self.pushButtonWindow.clicked.connect(self.checkear_username)

        self.layout = QtGui.QVBoxLayout(self)
        self.layout.addWidget(self.mailLabel)
        self.layout.addWidget(self.mailText)
        self.layout.addWidget(self.usernameLabel)
        self.layout.addWidget(self.userNameText)
        self.layout.addWidget(self.passwordLabel)
        self.layout.addWidget(self.passwordNameText)
        self.layout.addWidget(self.passwordLabel2)
        self.layout.addWidget(self.passwordNameText2)
        self.layout.addWidget(self.pushButtonWindow)

    def checkear_username(self):
        mail = self.mailText.text()
        if re.search(r".+@puc\.\w+$", mail) is not None or re.search(r".+@uc\.\w+$", mail) is not None:
            QtGui.QMessageBox.question(self, "", "El mail es incorrecto",QtGui.QMessageBox.Accepted)
            return
        if self.passwordNameText.text() != self.passwordNameText2.text():
            QtGui.QMessageBox.question(self, "", "Las contraseñas no son iguales",QtGui.QMessageBox.Accepted)
            return
        with open("passwords.420", "rb") as f:
            usuarios = pickle.load(f)
            if self.userNameText.text() in usuarios.keys():
                QtGui.QMessageBox.question(self, "", "Usuario ya ocupado",QtGui.QMessageBox.Accepted)
                return
            else:
                usuarios[self.userNameText.text()] = hash_salt(self.passwordNameText.text())
        with open("passwords.420", "wb") as file:
            pickle.dump(usuarios, file)
            QtGui.QMessageBox.question(self, "", "Registro Exitoso!",QtGui.QMessageBox.Accepted)
            self.hide()
            self.inicio = Inicio()
            self.inicio.show()












if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    app.setApplicationName('Log-in iChat-DCC')

    main = Inicio()
    main.show()

    sys.exit(app.exec_())