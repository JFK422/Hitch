from PyQt5 import QtGui, QtCore, QtWidgets
import colorama as clr
import qtawesome as qta
import sys

class CarouselItem(QtWidgets.QWidget):
    
    def setup(self, name = "", path = "", existing = True):
        self.name = name
        self.projPath = path
        projFile = open(path, "r")
        projImg = QtGui.QPixmap(projFile.read().split("\n")[3].split("=")[1])

        frameWidget = QtWidgets.QWidget()
        if existing:
            frameWidget.setObjectName("carouselItemFrame")
        else:
            frameWidget.setObjectName("carouselItemFrameNonExisting")

        pName = QtWidgets.QLabel(name)
        pName.setObjectName("projectLabel")
        pImg = QtWidgets.QLabel("")
        pImg.setObjectName("projectLabel")
        pImg.setPixmap(projImg)

        mainLay = QtWidgets.QVBoxLayout()
        mainLay.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignCenter)
        mainLay.setContentsMargins(QtCore.QMargins(0,10,0,10))
        frameWidget.setLayout(mainLay)

        mainLay.addWidget(pName)
        mainLay.addWidget(pImg)

        backLay = QtWidgets.QHBoxLayout()
        backLay.setContentsMargins(QtCore.QMargins(0,10,0,10))
        backLay.addWidget(frameWidget)

        self.setLayout(backLay)