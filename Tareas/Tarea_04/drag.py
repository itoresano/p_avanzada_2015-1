__author__ = 'Ignacio'
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QApplication, QDrag, QWidget, QFrame
from PyQt4.QtCore import Qt, QMimeData

# Clases que describen el area de trabajo para que los objetos (en este caso widgets, se puedan arrastrar)

class DropBox(QFrame):
    def __init__(self, parent):
        QFrame.__init__(self, parent)
        self.parent = parent
        self.setAcceptDrops(True)  # Aceptar objetos

    def dragEnterEvent(self, event):
        # Ignorar objetos arrastrados sin información
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        # Establecer el widget en una nueva posición
        pos = event.pos()
        self.widget = event.source()
        self.widget.setParent(self)
        self.widget.setGeometry(pos.x(), pos.y(), 40, 40)
        self.widget.show()
        event.acceptProposedAction()
        self.widget.pos = [pos.x(), pos.y()]
        self.parent.update()


class DraggableWidget(QWidget):
    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.setStyleSheet("background-color: white;")
        self.label2 = QtGui.QLabel("", self)
        self.label2.setGeometry(0, 0, 40, 20)
        self.checkbox = QtGui.QCheckBox("", self)
        self.checkbox.setGeometry(0, 20, 40, 20)
        self.pos = [10, 10]
        self.tipo = None

    def mousePressEvent(self, event):
        # Inicializar el arrastre con el botón derecho
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        # Chequear que se esté presionando el botón derecho
        if not (event.buttons() and Qt.LeftButton):
            return
        # Verificar que sea una posición válida
        if ((event.pos() - self.drag_start_position).manhattanLength()
                < QApplication.startDragDistance()):
            return
        drag = QDrag(self)
        mime_data = QMimeData()
        # Establecer el contenido del widget como dato
        drag.setMimeData(mime_data)
        mime_data.setText(self.label2.text())
        # Ejecutar la acción
        self.drop_action = drag.exec_(Qt.CopyAction | Qt.MoveAction)
