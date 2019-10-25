from PyQt5 import QtGui, QtCore, QtWidgets
from random import randint
import colorama as clr
import qtawesome as qta
import sys, os

class CarouselItem(QtWidgets.QWidget):
    
    def setup(self, name = "", path = "", existing = True):
        self.name = name
        self.projPath = path
        projImg = ""
        imgPaths = ["./resources/projectImages/pImgO.png",
        "./resources/projectImages/pImgB.png",
        "./resources/projectImages/pImgG.png",
        "./resources/projectImages/pImgI.png",
        "./resources/projectImages/pImgR.png",
        "./resources/projectImages/pImgV.png"]

        frameWidget = QtWidgets.QWidget()

        pName = QtWidgets.QLabel(name)
        pName.setObjectName("projectLabel")
        pImg = QtWidgets.QLabel("")
        pImg.setObjectName("projectLabel")
        #pImg.setScaledContents(True)

        if os.path.isfile(path + "/Resources/titleImg.png"):
            if existing:
                frameWidget.setObjectName("carouselItemFrame")
                pImg.setPixmap(QtGui.QPixmap(path + "/Resources/titleImg.png").scaled(256, 256, QtCore.Qt.KeepAspectRatio))
            else:
                frameWidget.setObjectName("carouselItemFrameNonExisting")
                pImg.setPixmap(QtGui.QPixmap(imgPaths[0]).scaled(256, 256, QtCore.Qt.KeepAspectRatio))
        else:
            if existing:
                frameWidget.setObjectName("carouselItemFrame")
                pImg.setPixmap(QtGui.QPixmap(imgPaths[randint(1, 5)]).scaled(256, 256, QtCore.Qt.KeepAspectRatio))
            else:
                frameWidget.setObjectName("carouselItemFrameNonExisting")
                pImg.setPixmap(QtGui.QPixmap(imgPaths[0]).scaled(256, 256, QtCore.Qt.KeepAspectRatio))

        mainLay = QtWidgets.QVBoxLayout()
        mainLay.setContentsMargins(QtCore.QMargins(0,0,0,0))
        mainLay.setSpacing(0)

        titleLay = QtWidgets.QVBoxLayout()
        titleLay.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        titleLay.setContentsMargins(QtCore.QMargins(0,10,0,10))
        titleWidget = QtWidgets.QWidget()
        titleWidget.setLayout(titleLay)

        imgLay = QtWidgets.QVBoxLayout()
        imgLay.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        imgLay.setContentsMargins(QtCore.QMargins(0,0,0,20))

        imgWidget = QtWidgets.QWidget()
        imgWidget.setLayout(imgLay)

        titleLay.addWidget(pName)
        imgLay.addWidget(pImg)
        
        mainLay.addWidget(titleWidget)
        mainLay.addWidget(imgWidget)
        frameWidget.setLayout(mainLay)

        backLay = QtWidgets.QHBoxLayout()
        backLay.setContentsMargins(QtCore.QMargins(0,10,0,10))
        backLay.addWidget(frameWidget)

        self.setLayout(backLay)