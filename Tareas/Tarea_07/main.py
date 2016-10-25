__author__ = 'Ignacio'
from PyQt4 import QtCore, QtGui, uic
import requests
from cargar_datos import cities, hubs, itineraries, routes, trips, colores, passengers, cargo

# crear la imagen principal sin ningun marker ni path
image_name = 'test1.png'
lista_clases = uic.loadUiType("interfaz.ui")
url = "https://maps.googleapis.com/maps/api/staticmap?center=0,-85&zoom=2&size=400x450&key=AIzaSyD7BXYqU0S0iDSX1wFd3asD7TPnkhi4pYI"
r = requests.get(url, stream=True)
if r.status_code == 200:
    with open(image_name, 'wb') as f:
        for chunk in r:
            f.write(chunk)


class MainWindow(lista_clases[0], lista_clases[1]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.image_name = "test1.png"
        # url+key para usar static map
        self.url1 = "https://maps.googleapis.com/maps/api/staticmap?center=0,-85&zoom=2&size=400x450"
        self.key1 = "&key=AIzaSyD7BXYqU0S0iDSX1wFd3asD7TPnkhi4pYI"
        #url + key para usar google directions
        self.url2 = "https://maps.googleapis.com/maps/api/directions/json?"
        self.key2 = "&key=AIzaSyDtKx1vF5S_Qgdedv0TD2Is0pkhR5652IM"
        # se setea la imagen
        self.pixmap = QtGui.QPixmap(self.image_name)
        self.label_6.setPixmap(self.pixmap)
        # cargar todos los datos desde los archivos de texto
        self.cities = cities("datos\\cities.txt")
        self.hubs = hubs("datos\\hubs.txt")
        self.itineraries = itineraries("datos\\itineraries.txt")
        self.routes = routes("datos\\routes.txt")
        self.trips = trips("datos\\trips.txt")
        self.colores = colores()
        self.passengers = passengers("datos\\passengers.txt")
        self.cargo = cargo("datos\\cargo.txt")
        # botones
        self.pushButton.clicked.connect(self.dibujar_viaje)
        self.pushButton_3.clicked.connect(self.dibujar_vehiculo)
        self.pushButton_5.clicked.connect(self.dibujar_pasajero)
        self.pushButton_4.clicked.connect(self.dibujar_carga)

    # funcion para mostrar los viajes segun su id
    def dibujar_viaje(self):

        viajes = self.lineEdit.text().split(";")
        self.url1_2 = self.url1
        for i in viajes:
            self.url2_2 = self.url2
            origen = [self.hubs[self.trips[i]["origen"]]["ciudad"],
                      self.cities[self.hubs[self.trips[i]["origen"]]["ciudad"]]["pais"]]
            color_origen = self.colores[origen[1]]
            destino = [self.hubs[self.trips[i]["destino"]]["ciudad"],
                       self.cities[self.hubs[self.trips[i]["destino"]]["ciudad"]]["pais"]]
            color_destino = self.colores[destino[1]]

            if self.routes[self.trips[i]["ruta"]]["tipo"] in ["Aerial", "Aquatic"]:
                #si la ruta es aerea se traza un camino recto entre las 2 ciudades
                marker1 = "&markers=color:{0}%7Clabel:C%7C{1},{2}".format(color_origen, origen[0], origen[1])
                marker2 = "&markers=color:{0}%7Clabel:C%7C{1},{2}".format(color_destino, destino[0], destino[1])
                path = "&path={0},{1}%7C{2},{3}".format(origen[0], origen[1], destino[0], destino[1])
                self.url1_2 += marker1 + marker2 + path
            if self.routes[self.trips[i]["ruta"]]["tipo"] == "Terrestrial":
                # si la ruta es terrestre se usa la api google directions para encontrar los puntos de la polyline
                origen1 = "origin={0},{1}".format(origen[0], origen[1])
                destino1 = "&destination={0},{1}".format(destino[0], destino[1])
                self.url2_2 += origen1 + destino1 + self.key2
                request = requests.get(self.url2_2).json()
                data_polyline = request["routes"][0]["overview_polyline"]["points"]
                #se traza el path con sus markers
                marker1 = "&markers=color:{0}%7Clabel:C%7C{1},{2}".format(color_origen, origen[0], origen[1])
                marker2 = "&markers=color:{0}%7Clabel:C%7C{1},{2}".format(color_destino, destino[0], destino[1])
                path = "&path=enc:{0}".format(data_polyline)
                self.url1_2 += marker1 + marker2 + path

        self.url1_2 += self.key1
        if len(self.url1_2) > 2048:
            QtGui.QMessageBox.question(self, "", "url demasiado larga ingrese menos viajes", QtGui.QMessageBox.Accepted)
            return
        else:
            self.change_pic(self.url1_2)

    # funcion para mostrar los viajs de los vehiculos segun su id, muestra solo el 1er viaje a cause de la restriccion
    # del largo del url
    def dibujar_vehiculo(self):
        vehiculo = self.lineEdit_3.text()
        self.url1_2 = self.url1
        for i in self.trips:
            if self.trips[i]["vehiculo"] == vehiculo:
                origen = [self.hubs[self.trips[i]["origen"]]["ciudad"],
                          self.cities[self.hubs[self.trips[i]["origen"]]["ciudad"]]["pais"]]
                color_origen = self.colores[origen[1]]
                destino = [self.hubs[self.trips[i]["destino"]]["ciudad"],
                           self.cities[self.hubs[self.trips[i]["destino"]]["ciudad"]]["pais"]]
                color_destino = self.colores[destino[1]]
                if self.routes[self.trips[i]["ruta"]]["tipo"] in ["Aerial", "Aquatic"]:
                    marker1 = "&markers=color:{0}%7Clabel:C%7C{1},{2}".format(color_origen, origen[0], origen[1])
                    marker2 = "&markers=color:{0}%7Clabel:C%7C{1},{2}".format(color_destino, destino[0], destino[1])
                    path = "&path={0},{1}%7C{2},{3}".format(origen[0], origen[1], destino[0], destino[1])
                    self.url1_2 += marker1 + marker2 + path
                    break
                if self.routes[self.trips[i]["ruta"]]["tipo"] == "Terrestrial":
                    origen1 = "origin={0},{1}".format(origen[0], origen[1])
                    destino1 = "&destination={0},{1}".format(destino[0], destino[1])
                    self.url2_2 += origen1 + destino1 + self.key2
                    request = requests.get(self.url2_2).json()
                    data_polyline = request["routes"][0]["overview_polyline"]["points"]

                    marker1 = "&markers=color:{0}%7Clabel:C%7C{1},{2}".format(color_origen, origen[0], origen[1])
                    marker2 = "&markers=color:{0}%7Clabel:C%7C{1},{2}".format(color_destino, destino[0], destino[1])
                    path = "&path=enc:{0}".format(data_polyline)
                    self.url1_2 += marker1 + marker2 + path
                    break

        self.url1_2 += self.key1
        if len(self.url1_2) > 2048:
            QtGui.QMessageBox.question(self, "", "url demasiado larga, imposible mostrar mapa",
                                       QtGui.QMessageBox.Accepted)
            return
        else:
            self.change_pic(self.url1_2)

    # funcion para mostrar los viajes de un pasajero segun su id
    def dibujar_pasajero(self):
        pasajero = self.lineEdit_5.text()
        viaje = self.itineraries[pasajero]["trips"]
        self.url1_2 = self.url1
        for i in viaje:
            self.url2_2 = self.url2
            origen = [self.hubs[self.trips[i]["origen"]]["ciudad"],
                      self.cities[self.hubs[self.trips[i]["origen"]]["ciudad"]]["pais"]]
            color_origen = self.colores[origen[1]]
            destino = [self.hubs[self.trips[i]["destino"]]["ciudad"],
                       self.cities[self.hubs[self.trips[i]["destino"]]["ciudad"]]["pais"]]
            color_destino = self.colores[destino[1]]

            if self.routes[self.trips[i]["ruta"]]["tipo"] in ["Aerial", "Aquatic"]:
                marker1 = "&markers=color:{0}%7Clabel:C%7C{1},{2}".format(color_origen, origen[0], origen[1])
                marker2 = "&markers=color:{0}%7Clabel:C%7C{1},{2}".format(color_destino, destino[0], destino[1])
                path = "&path={0},{1}%7C{2},{3}".format(origen[0], origen[1], destino[0], destino[1])
                self.url1_2 += marker1 + marker2 + path
            if self.routes[self.trips[i]["ruta"]]["tipo"] == "Terrestrial":
                origen1 = "origin={0},{1}".format(origen[0], origen[1])
                destino1 = "&destination={0},{1}".format(destino[0], destino[1])
                self.url2_2 += origen1 + destino1 + self.key2
                request = requests.get(self.url2_2).json()
                data_polyline = request["routes"][0]["overview_polyline"]["points"]

                marker1 = "&markers=color:{0}%7Clabel:C%7C{1},{2}".format(color_origen, origen[0], origen[1])
                marker2 = "&markers=color:{0}%7Clabel:C%7C{1},{2}".format(color_destino, destino[0], destino[1])
                path = "&path=enc:{0}".format(data_polyline)
                self.url1_2 += marker1 + marker2 + path

        self.url1_2 += self.key1
        if len(self.url1_2) > 2048:
            QtGui.QMessageBox.question(self, "", "url demasiado larga, imposible mostrar mapa",
                                       QtGui.QMessageBox.Accepted)
            return
        else:
            self.change_pic(self.url1_2)

    # funcion para mostrar los viajes de una carga segun su id
    def dibujar_carga(self):
        carga = self.lineEdit_4.text()
        viaje = self.itineraries[carga]["trips"]
        self.url1_2 = self.url1
        for i in viaje:
            self.url2_2 = self.url2
            origen = [self.hubs[self.trips[i]["origen"]]["ciudad"],
                      self.cities[self.hubs[self.trips[i]["origen"]]["ciudad"]]["pais"]]
            color_origen = self.colores[origen[1]]
            destino = [self.hubs[self.trips[i]["destino"]]["ciudad"],
                       self.cities[self.hubs[self.trips[i]["destino"]]["ciudad"]]["pais"]]
            color_destino = self.colores[destino[1]]

            if self.routes[self.trips[i]["ruta"]]["tipo"] in ["Aerial", "Aquatic"]:
                marker1 = "&markers=color:{0}%7Clabel:C%7C{1},{2}".format(color_origen, origen[0], origen[1])
                marker2 = "&markers=color:{0}%7Clabel:C%7C{1},{2}".format(color_destino, destino[0], destino[1])
                path = "&path={0},{1}%7C{2},{3}".format(origen[0], origen[1], destino[0], destino[1])
                self.url1_2 += marker1 + marker2 + path
            if self.routes[self.trips[i]["ruta"]]["tipo"] == "Terrestrial":
                origen1 = "origin={0},{1}".format(origen[0], origen[1])
                destino1 = "&destination={0},{1}".format(destino[0], destino[1])
                self.url2_2 += origen1 + destino1 + self.key2
                request = requests.get(self.url2_2).json()
                data_polyline = request["routes"][0]["overview_polyline"]["points"]

                marker1 = "&markers=color:{0}%7Clabel:C%7C{1},{2}".format(color_origen, origen[0], origen[1])
                marker2 = "&markers=color:{0}%7Clabel:C%7C{1},{2}".format(color_destino, destino[0], destino[1])
                path = "&path=enc:{0}".format(data_polyline)
                self.url1_2 += marker1 + marker2 + path

        self.url1_2 += self.key1
        if len(self.url1_2) > 2048:
            QtGui.QMessageBox.question(self, "", "url demasiado larga, imposible mostrar mapa",
                                       QtGui.QMessageBox.Accepted)
            return
        else:
            self.change_pic(self.url1_2)

    def change_pic(self, direccion):

        r = requests.get(direccion, stream=True)
        if r.status_code == 200:
            with open(image_name, 'wb') as f:
                for chunk in r:
                    f.write(chunk)
        self.pixmap = QtGui.QPixmap(self.image_name)
        self.label_6.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QtGui.QApplication([])
    form = MainWindow()
    form.show()
    app.exec_()