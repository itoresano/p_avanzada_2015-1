__author__ = 'Ignacio'
# tipos de monedas
class Moneda:
    def __init__(self, x, y, parent):
        self.x = x*25 + 30
        self.y = y*25 + 30
        self.parent = parent

class Amarilla(Moneda):
    def __init__(self, x, y, parent, puntaje):
        super().__init__(x, y, parent)
        self.puntaje = puntaje

    def atrapada(self):
        self.parent.puntos += self.puntaje
        self.parent.contador.setText(str(self.parent.puntos))

class Roja(Moneda):
    def __init__(self, x, y, parent):
        super().__init__(x, y, parent)

    def atrapada(self):
        if self.parent.pocmon.vidas < 5:
            self.parent.pocmon.vidas += 1
            self.parent.vidas.setText(str(self.parent.pocmon.vidas))
        else:
            return

class Verde(Moneda):
    def __init__(self, x, y, parent):
        super().__init__(x, y, parent)

class Azul(Moneda):
    def __init__(self, x, y, parent):
        super().__init__(x, y, parent)




