from PyQt5 import QtGui, QtCore, QtWidgets
import colorama as clr
import qtawesome as qta
import sys

class CarouselItem(QtWidgets.QWidget):
    
    def setup(self, name = "", imgPath = ""):
        self.name = name
        self.imgPath = imgPath

        frameWidget = QtWidgets.QWidget()
        frameWidget.setObjectName("carouselItemFrame")

        pName = QtWidgets.QLabel(name)

        backLay = QtWidgets.QHBoxLayout()
        backLay.setContentsMargins(QtCore.QMargins(0,0,0,0))
        backLay.addWidget(frameWidget)

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