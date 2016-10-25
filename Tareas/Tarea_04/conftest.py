__author__ = 'Ignacio'

from Clases import Numero
# Clase que "sustituye" a la clase DraggableWidget ya que es mas facil inicializarla y tiene el mismo parametro de
# interes: self.tipo
class Widget:
    def __init__(self, valor):
        self.tipo = Numero(valor)