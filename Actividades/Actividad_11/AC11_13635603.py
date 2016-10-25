__author__ = 'Ignacio'

from abc import ABCMeta, abstractmethod, abstractproperty
from math import sqrt

class Figura(metaclass=ABCMeta):

    @abstractproperty
    def centro(self):
        pass
    @abstractproperty
    def perimetro(self):
        pass
    @abstractproperty
    def area(self):
        pass
    @abstractmethod
    def crecer_area(self,x):
        pass
    @abstractmethod
    def crecer_perimetro(self, x):
        pass

    def vertices(self):

        pass


    def trasladar(self, x, y):
        self._centro = (self._centro[0] + x, self._centro[1] + y)

class Rectangulo(Figura):
    def __init__(self, largo, ancho, centro):
        self._largo = largo
        self._ancho = ancho
        self._centro = centro
    @property
    def centro(self):
        return self._centro
    @property
    def ancho(self):
        return self._ancho
    @property
    def largo(self):
        return self._largo
    @ancho.setter
    def ancho(self, valor):
        self._ancho = valor
    @largo.setter
    def largo(self, valor):
        self._largo = valor
    @centro.setter
    def centro(self, valor):
        self._centro = valor
    @property
    def area(self):
        return self._ancho*self._largo
    @property
    def perimetro(self):
        return self._ancho*2 + self._largo*2

    def trasladar(self, x, y):
        super().trasladar(x, y)

    def crecer_area(self, x):
        self.largo = self.largo * sqrt(x)
        self.ancho = self.ancho * sqrt(x)

    def crecer_perimetro(self, x):
        a = x / self.perimetro
        self.largo += self.largo*a
        self.ancho += self.ancho*a

    def __repr__(self):
        return "{0} - Perimetro: {1}, Area: {2}, Centro: {3}".format(self.__class__, self.perimetro, self.area,
                                                                     self.centro)


class Triangulo_Equilatero(Figura):
    def __init__(self, lado, centro):
        self._lado = lado
        self._centro = centro

    def trasladar(self, x, y):
        return super().trasladar(x, y)

    @property
    def centro(self):
        return self._centro
    @centro.setter
    def centro(self, valor):
        self._centro = valor
    @property
    def lado(self):
        return self._lado
    @lado.setter
    def lado(self, valor):
        self._lado = valor
    @property
    def area(self):
        return ((self._lado*sqrt(3)*self._lado)/4)
    @property
    def perimetro(self):
        return self._lado*3
    def crecer_area(self, x):
        self._lado = self._lado * sqrt(x)
    def crecer_perimetro(self, x):
        self._lado += x/3

    def __repr__(self):
        return "{0} - Perimetro: {1}, Area: {2}, Centro = ({3})".format(self.__class__, self.perimetro, self.area,
                                                                        self._centro)


b = Triangulo_Equilatero(6,(0,0))
print(b.lado)
b.lado = 7
print(b.lado)
b.crecer_area(2)
b.crecer_perimetro(2)
print(b.lado)
print(b.area, b.perimetro)








