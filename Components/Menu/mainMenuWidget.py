import qtawesome as qta
from PyQt5 import QtGui, QtCore, QtWidgets

#Menu widget placed in the stack of vLPart

class mainMenu(QtWidgets.QWidget):
    def setup(self):
        vMenu = QtWidgets.QVBoxLayout()
        vMenu.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        vMenu.setContentsMargins(QtCore.QMargins(20,20,0,0))

        for i in range(5):
            lakeside = QtWidgets.QPushButton("TEST")
            vMenu.addWidget(lakeside)

        self.setObjectName("menu")
        self.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))
        self.setLayout(vMenu)