
import socket
import threading
import sys
import ChatUI
import select

class Cliente:
    def __init__(self, usuario):
        self.usuario = usuario
        self.host = '127.0.0.1'
        self.port = 3490
        self.s_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Socket cliente
        try:
            self.chat = ChatUI.Chat(usuario) #Interfaz cliente
            self.thread_wait_server = threading.Thread(target=self.wait_server)
            self.thread_wait_server.start()
            self.chat.inicializar_interfaz()

        except socket.error:
            print("No fue posible realizar la conexión")
            sys.exit()


    def wait_server(self):
        self.conectar()
        while True:
            if self.chat.subir_pressed():
                self.enviar(self.chat.get_path())

    def conectar(self):
        self.s_cliente.connect((self.host,self.port))
        self.escuchador = threading.Thread(target=self.escuchar, args=())
        self.escuchador.daemon = True
        self.escuchador.start()

    def escuchar(self):
        while True:
            data = self.s_cliente.recv(1024)
            with open("Imagenes_Prueba\\Imagen2.jpg", "wb+") as f:
                while data:
                    f.write(data)
                    ready = select.select([self.s_cliente], [], [], 0)
                    if ready[0]:
                        data = self.s_cliente.recv(1024)
                    else:
                        data = "b"
                        self.chat.update_image("Imagenes_Prueba\\Imagen2.jpg")

    def enviar(self, path):
        with open(path, "rb") as f:
            file = f.read()
            self.s_cliente.send(file)


class Servidor:
    def __init__(self, usuario):
        self.usuario = usuario
        self.host = '127.0.0.1'
        self.port = 3490
        self.s_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s_servidor.bind((self.host,self.port))
        self.s_servidor.listen(1)

        self.cliente = None #Socket cliente conectado
        self.chat = ChatUI.Chat(usuario) #Interfaz servidor

        self.thread_wait_cliente = threading.Thread(target = self.wait_cliente)
        self.thread_wait_cliente.start()
        self.chat.inicializar_interfaz()


    def wait_cliente(self):
        self.aceptar()
        while(True):
            if self.chat.subir_pressed():
                self.enviar(self.chat.get_path())

    def aceptar(self):
        cliente_nuevo, address = self.s_servidor.accept()
        self.cliente = cliente_nuevo
        thread_cliente = threading.Thread(target=self.escuchar)
        thread_cliente.daemon = True
        thread_cliente.start()

    def escuchar(self):
        while True:
            data = self.cliente.recv(1024)
            with open("Imagenes_Prueba\\Imagen.jpg", "wb+") as f:
                while data:
                    f.write(data)
                    ready = select.select([self.s_servidor], [], [], 0)[0]
                    if ready[0]:
                        data = self.cliente.recv(1024)
                    else:
                        data = "b"
                        self.chat.update_image("Imagenes_Prueba\\Imagen.jpg")



    def enviar(self, path):
        with open(path,'rb') as f:
            data = f.read()
        self.cliente.send(data)


if __name__ == "__main__":

        pick = input("Ingrese S si quiere ser servidor o C si desea ser cliente: ")
        if(pick == "S" or pick == "s"):
            server = Servidor("Servidor")

        elif(pick == "C" or pick=="c"):
            usuario = input("Ingrese nombre usuario cliente: ")
            client = Cliente(usuario)




