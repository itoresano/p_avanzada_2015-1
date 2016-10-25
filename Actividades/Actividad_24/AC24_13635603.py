__author__ = 'Ignacio'
import socket
import threading, sys

class Cliente:
    def __init__(self, usuario):
        self.usuario = usuario
        self.server_name = socket.gethostname()
        self.server_port = 1500
        self.s_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.max_size = 2048
        try:
            self.s_cliente.connect((self.server_name, self.server_port))
        except socket.error:
            print("No fue posible conectarse")
            sys.exit()

    def run(self): #responder
        while True:
            msje = input("Ingresa tu mensaje a enviar al servidor")
            self.socket.sendto(msje, (self.server_name, self.server_port))

    def escuchar(self):
        while(True):
            data = self.s_cliente.recv(1024)
            print(data.decode('ascii'))

    def enviar(self, mensaje):
        msj_final = self.usuario + ": " + mensaje
        self.s_cliente.send(msj_final.encode('ascii'))


class Servidor:
    def __init__(self, usuario):
        self.usuario = usuario
        self.server_name = socket.gethostname()
        self.server_port = 1500
        self.s_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.max_size = 2048
        self.s_servidor.bind((self.server_name, self.server_port))
        self.s_servidor.listen(5)
        self.cliente = None

    def escuchar(self, cliente):
        while True:
            data = cliente.recv(1024)
            mensaje = data.decode('ascii')
            print(mensaje)

    def aceptar(self):
        cliente_nuevo, address = self.s_servidor.accept()
        self.cliente = cliente_nuevo
        thread_cliente = threading.Thread(
            target=self.escuchar, args=(cliente_nuevo,))
        thread_cliente.daemon = True
        thread_cliente.start()


    def enviar(self, mensaje):
        msj_final = self.usuario + ": " + mensaje
        self.cliente.send(msj_final.encode('ascii'))

if __name__ == "__main__":
    pick = input("Ingrese S si quiere ser servidor o C si desea ser cliente: ")
    if(pick == "S"):
        nombre = input("Ingrese el nombre del usuario: ")
        server = Servidor(nombre)
        server.aceptar()
        while(True):
            mensaje = input()
            server.enviar(mensaje)

    elif(pick == "C"):
        nombre = input("Ingrese el nombre del usuario: ")
        client = Cliente(nombre)
        escuchador = threading.Thread(target=client.escuchar, args=())
        escuchador.daemon = True
        escuchador.start()
        while(True):
            mensajes = input()
            client.enviar(mensajes)
