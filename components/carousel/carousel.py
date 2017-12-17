from PyQt5 import QtGui, QtCore, QtWidgets
import colorama as clr
import qtawesome as qta
import sys

class Carousel(QtWidgets.QWidget):
    
    def setup(self, carouselWidgets = "", widgetsShowAmmount = 3):
        self.cWidgets = carouselWidgets

        frameWidget = QtWidgets.QWidget()
        frameWidget.setObjectName("carouselFrame")

        left = qta.icon("fa.caret-left", color="#f9f9f9")
        right = qta.icon("fa.caret-right", color="#f9f9f9")

        goLeft = QtWidgets.QPushButton(left, "")
        goLeft.setObjectName("carouselSideButtons")
        goLeft.setIconSize(QtCore.QSize(64, 64))
        goLeft.setMaximumWidth(100)
        goLeft.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))

        goRight = QtWidgets.QPushButton(right, "")
        goRight.setObjectName("carouselSideButtons")
        goRight.setIconSize(QtCore.QSize(64, 64))
        goRight.setMaximumWidth(100)
        goRight.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding))

        backLay = QtWidgets.QHBoxLayout()
        backLay.setContentsMargins(QtCore.QMargins(0,0,0,0))
        backLay.addWidget(frameWidget)

        cLay = QtWidgets.QGridLayout()
        cLay.setContentsMargins(QtCore.QMargins(0,0,0,0))
        cLay.addWidget(goLeft, 0, 0)
        cLay.addWidget(goRight, 0, 2)
        frameWidget.setLayout(cLay)


        self.setLayout(backLay)

#For executing this file standalone
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    
    #Set the main styling of dis window aswell
    with open("../appearance/style/stylesheet.css") as f:
        theme = f.read()
    app.setStyleSheet(theme)
    gui = Carousel()
    gui.show()
    app.exec_()