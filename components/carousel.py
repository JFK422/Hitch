from PyQt5 import QtGui, QtCore, QtWidgets
import colorama as clr

class Carousel(QtWidgets.QWidget):
    
    def setup(carouselWidgets, widgetsShowAmmount = 3):
        self.cWidgets = carouselWidgets

        frameWidget = QtWidgets.QWidget()
        frameWidget.setObjectName("carouselFrame")