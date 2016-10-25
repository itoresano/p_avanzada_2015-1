__author__ = 'Ignacio'

import pytest
from conftest import Widget
from Clases import Suma, Resta, Multiplicacion, Division, Potencia, Logaritmo_natural, Valor_absoluto, Seno, Coseno, \
    Tangente, Minimo, Maximo
from math import pi, log, cos, sin, tan


class Test_suma:
    def setup_class(cls):
        a = Widget(2)
        b = Widget(0)
        cls.suma = Suma(valor=None, hijos=[a, b])

    def test_operacion(self):
        self.suma.operacion()
        assert self.suma.valor == 2

    def test_agregar_hijo(self):
        c = Widget(pi / 2)
        assert self.suma.agregar_hijo(c) is False


class Test_resta:
    def setup_class(cls):
        a = Widget(2)
        b = Widget(0)
        cls.resta = Resta(valor=None, hijos=[a, b])

    def test_operacion(self):
        self.resta.operacion()
        assert self.resta.valor == 2

    def test_agregar_hijo(self):
        c = Widget(pi / 2)
        assert self.resta.agregar_hijo(c.tipo.valor) is False


class Test_multiplicacion:
    def setup_class(cls):
        a = Widget(2)
        b = Widget(0)
        cls.multiplicacion = Multiplicacion(valor=None, hijos=[a, b])

    def test_operacion(self):
        self.multiplicacion.operacion()
        assert self.multiplicacion.valor == 0

    def test_agregar_hijo(self):
        c = Widget(pi / 2)
        assert self.multiplicacion.agregar_hijo(c.tipo.valor) is False


class Test_division:
    def setup_class(cls):
        a = Widget(2)
        cls.clase = Division(valor=None, hijos=[a])

    def test_agregar_hijo(self):
        b = Widget(0)
        assert self.clase.agregar_hijo(b.tipo.valor) is False

    def test_operacion(self):
        c = Widget(1)
        self.clase.hijos.append(c)
        self.clase.operacion()
        assert self.clase.valor == 2


class Test_potencia:
    def setup_class(cls):
        a = Widget(2)
        b = Widget(0)
        cls.clase = Potencia(valor=None, hijos=[a, b])

    def test_operacion(self):
        self.clase.operacion()
        assert self.clase.valor == 1

    def test_agregar_hijo(self):
        c = Widget(pi / 2)
        assert self.clase.agregar_hijo(c.tipo.valor) is False


class Test_logaritmo:
    def setup_class(cls):
        a = Widget(2)
        cls.clase = Logaritmo_natural(valor=None, hijos=[a])

    def test_operacion(self):
        self.clase.operacion()
        assert self.clase.valor == log(2)

    def test_agregar_hijo(self):
        c = Widget(pi / 2)
        assert self.clase.agregar_hijo(c.tipo.valor) is False


class Test_valor_absoluto:
    def setup_class(cls):
        a = Widget(2)
        cls.clase = Valor_absoluto(valor=None, hijos=[a])

    def test_operacion(self):
        self.clase.operacion()
        assert self.clase.valor == abs(self.clase.hijos[0].tipo.valor)

    def test_agregar_hijo(self):
        c = Widget(pi / 2)
        assert self.clase.agregar_hijo(c.tipo.valor) is False


class Test_seno:
    def setup_class(cls):
        a = Widget(2)
        cls.clase = Seno(valor=None, hijos=[a])

    def test_operacion(self):
        self.clase.operacion()
        assert self.clase.valor == sin(2)

    def test_agregar_hijo(self):
        c = Widget(pi / 2)
        assert self.clase.agregar_hijo(c.tipo.valor) is False


class Test_coseno:
    def setup_class(cls):
        a = Widget(2)
        cls.clase = Coseno(valor=None, hijos=[a])

    def test_operacion(self):
        self.clase.operacion()
        assert self.clase.valor == cos(self.clase.hijos[0].tipo.valor)

    def test_agregar_hijo(self):
        c = Widget(pi / 2)
        assert self.clase.agregar_hijo(c.tipo.valor) is False


class Test_tangente:
    def setup_class(cls):
        cls.clase = Tangente()

    def test_agregar_hijo(self):
        c = Widget(pi / 2)
        assert self.clase.agregar_hijo(c.tipo.valor) is False

    def test_operacion(self):
        a = Widget(2)
        self.clase.hijos.append(a)
        self.clase.operacion()
        assert self.clase.valor == tan(2)


class Test_maximo:
    def setup_class(cls):
        a = Widget(2)
        b = Widget(0)
        c = Widget(3)
        d = Widget(-3)
        cls.clase = Maximo(valor=None, hijos=[a, b, c, d])

    def test_operacion(self):
        self.clase.operacion()
        assert self.clase.valor == 3


class Test_minimo:
    def setup_class(cls):
        a = Widget(2)
        b = Widget(0)
        c = Widget(3)
        d = Widget(-3)
        cls.clase = Minimo(valor=None, hijos=[a, b, c, d])

    def test_operacion(self):
        self.clase.operacion()
        assert self.clase.valor == -3