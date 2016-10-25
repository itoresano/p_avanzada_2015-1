__author__ = 'Ignacio'

from math import sin, cos, log, tan, pi, e

# Clases para cada operacion con sus diferentes metodos.
class Numero:
    def __init__(self, valor):
        self.valor = float(valor)


class Output:
    def __init__(self, valor=None, hijos=list()):
        self.valor = valor
        self.hijos = hijos
        self.entradas = 1
        self.msje_entradas = "Error no se le pueden agregar mas entradas al bloque"

    def agregar_hijo(self, valor):
        if len(self.hijos) == 0:
            return True
        else:
            return False


class Suma:
    def __init__(self, valor=None, hijos=list()):
        self.valor = valor
        self.hijos = hijos
        self.msje_entradas = "Error no se le pueden agregar mas entradas al bloque"
        self.entradas = 2

    def operacion(self):
        if len(self.hijos) == 2:
            self.valor = self.hijos[0].tipo.valor + self.hijos[1].tipo.valor

    def agregar_hijo(self, valor):
        if len(self.hijos) < 2:
            return True
        else:
            return False


class Resta:
    def __init__(self, valor=None, hijos=list()):
        self.valor = valor
        self.hijos = hijos
        self.msje_entradas = "Error no se le pueden agregar mas entradas al bloque"
        self.entradas = 2

    def operacion(self):
        if len(self.hijos) == 2:
            self.valor = self.hijos[0].tipo.valor - self.hijos[1].tipo.valor

    def agregar_hijo(self, valor):
        if len(self.hijos) < 2:
            return True
        else:
            return False


class Multiplicacion:
    def __init__(self, valor=None, hijos=list()):
        self.valor = valor
        self.hijos = hijos
        self.msje_entradas = "Error no se le pueden agregar mas entradas al bloque"
        self.entradas = 2

    def operacion(self):
        if len(self.hijos) == 2:
            self.valor = self.hijos[0].tipo.valor * self.hijos[1].tipo.valor

    def agregar_hijo(self, valor):
        if len(self.hijos) < 2:
            return True
        else:
            return False


class Division:
    def __init__(self, valor=None, hijos=list()):
        self.valor = valor
        self.hijos = hijos
        self.msje_entradas = "Error no se le pueden agregar mas entradas al bloque o esta tratando de dividir por cero"
        self.entradas = 2

    def operacion(self):
        if len(self.hijos) == 2 and self.hijos[1] != 0:
            self.valor = self.hijos[0].tipo.valor / self.hijos[1].tipo.valor

    def agregar_hijo(self, valor):
        if len(self.hijos) == 1 and int(valor) == 0:
            return False
        if len(self.hijos) < 2:
            return True
        else:
            return False


class Potencia:
    def __init__(self, valor=None, hijos=list()):
        self.valor = valor
        self.hijos = hijos
        self.msje_entradas = "Error no se le pueden agregar mas entradas al bloque"
        self.entradas = 2

    def operacion(self):
        if len(self.hijos) == 2:
            self.valor = self.hijos[0].tipo.valor ** self.hijos[1].tipo.valor

    def agregar_hijo(self, valor):
        if len(self.hijos) < 2:
            return True
        else:
            return False


class Valor_absoluto:
    def __init__(self, valor=None, hijos=list()):
        self.valor = valor
        self.hijos = hijos
        self.msje_entradas = "Error no se le pueden agregar mas entradas al bloque"
        self.entradas = 1

    def operacion(self):
        if len(self.hijos) == 1:
            self.valor = abs(self.hijos[0].tipo.valor)

    def agregar_hijo(self, valor):
        if len(self.hijos) == 0:
            return True
        else:
            return False


class Logaritmo_natural:
    def __init__(self, valor=None, hijos=list()):
        self.valor = valor
        self.hijos = hijos
        self.msje_entradas = "Error no se le pueden agregar mas entradas al bloque o esta tratando de calcular un valor" \
                             "que no existe: e.g ln(0)"
        self.entradas = 1

    def operacion(self):
        if len(self.hijos) == 1:
            self.valor = log(self.hijos[0].tipo.valor)

    def agregar_hijo(self, valor):
        if len(self.hijos) == 0 and valor != 0:
            return True
        else:
            return False


class Seno:
    def __init__(self, valor=None, hijos=list()):
        self.valor = valor
        self.hijos = hijos
        self.msje_entradas = "Error no se le pueden agregar mas entradas al bloque"
        self.entradas = 1

    def operacion(self):
        if len(self.hijos) == 1:
            self.valor = sin(self.hijos[0].tipo.valor)

    def agregar_hijo(self, valor):
        if len(self.hijos) == 0:
            return True
        else:
            return False


class Coseno:
    def __init__(self, valor=None, hijos=list()):
        self.valor = valor
        self.hijos = hijos
        self.msje_entradas = "Error no se le pueden agregar mas entradas al bloque"
        self.entradas = 1

    def operacion(self):
        if len(self.hijos) == 1:
            self.valor = cos(self.hijos[0].tipo.valor)

    def agregar_hijo(self, valor):
        if len(self.hijos) == 0:
            return True
        else:
            return False


class Tangente:
    def __init__(self, valor=None, hijos=list()):
        self.valor = valor
        self.hijos = hijos
        self.msje_entradas = "Error no se le pueden agregar mas entradas al bloque o el valor a calcular no existe" \
                             "(e.g tan(pi/2)"
        self.entradas = 1

    def operacion(self):
        if len(self.hijos) == 1:
            self.valor = tan(self.hijos[0].tipo.valor)

    def agregar_hijo(self, valor):
        if len(self.hijos) == 0 and valor != pi / 2:
            return True
        else:
            return False


class Maximo:
    def __init__(self, valor=None, hijos=list()):
        self.valor = valor
        self.hijos = hijos
        self.msje_entradas = "Error no se le pueden agregar mas entradas al bloque"
        self.entradas = 1

    def operacion(self):
        if len(self.hijos) > 0:
            self.valor = max(self.hijos, key=lambda x: x.tipo.valor).tipo.valor


class Minimo:
    def __init__(self, valor=None, hijos=list()):
        self.valor = valor
        self.hijos = hijos
        self.msje_entradas = "Error no se le pueden agregar mas entradas al bloque"
        self.entradas = 1

    def operacion(self):
        if len(self.hijos) > 0:
            self.valor = min(self.hijos, key=lambda x: x.tipo.valor).tipo.valor


# Perdon
def Instanciar(texto, objeto):
    if texto == "+":
        objeto.tipo = Suma(valor=None, hijos=list())
    if texto == "-":
        objeto.tipo = Resta(valor=None, hijos=list())
    if texto == "*":
        objeto.tipo = Multiplicacion(valor=None, hijos=list())
    if texto == "/":
        objeto.tipo = Division(valor=None, hijos=list())
    if texto == "x^n":
        objeto.tipo = Potencia(valor=None, hijos=list())
    if texto == "ln()":
        objeto.tipo = Logaritmo_natural(valor=None, hijos=list())
    if texto == "||":
        objeto.tipo = Valor_absoluto(valor=None, hijos=list())
    if texto == "sen()":
        objeto.tipo = Seno(valor=None, hijos=list())
    if texto == "cos()":
        objeto.tipo = Coseno(valor=None, hijos=list())
    if texto == "tan()":
        objeto.tipo = Tangente(valor=None, hijos=list())
    if texto == "max()":
        objeto.tipo = Maximo(valor=None, hijos=list())
    if texto == "min()":
        objeto.tipo = Minimo(valor=None, hijos=list())



