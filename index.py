import sys, os
import qtawesome as qta
from components import create
from components import introductionWindow
from PyQt5 import QtGui, QtCore, QtWidgets
import colorama as clr

#This is the MAIN file of the app. Its used for handeling hte diffrent scripts within this programm.
#Debug prints are as formatted like this: FILE; CLASS; METHOD: MESSAGE

#Variables

class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,1200,700)
        self.setWindowTitle("Hitch")
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint) #Use this for a frameless window. Will be used later!
        create.CreateUI.create(self)
        #init colorama
        clr.init()
        #Set the app icon, maximize the window, show it and the startup window.
        self.icon()
        self.showMaximized()
        self.show()
        self.startup = introductionWindow.Introduction()
        self.startup.show()

    #Minimize and maximize methods for the new window action buttons
    def minimize(self):
        self.showMinimized()

    def maximize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def icon(self):
        #Set app icon    
        app_icon = QtGui.QIcon()
        app_icon.addFile('resources/icons/16x16.png', QtCore.QSize(16,16))
        app_icon.addFile('resources/icons/32x32.png', QtCore.QSize(32,32))
        app_icon.addFile('resources/icons/64x64.png', QtCore.QSize(64,64))
        app_icon.addFile('resources/icons/128x128.png', QtCore.QSize(128,128))
        app_icon.addFile('resources/icons/256x256.png', QtCore.QSize(256,256))
        app.setWindowIcon(app_icon)


if __name__ == '__main__':
    #Creating the QApplication
    app = QtWidgets.QApplication(sys.argv)

    #Set the main styling of the app
    #Yes its all in this file!
    with open("./appearance/style/stylesheet.css") as f:
        theme = f.read()
    app.setStyleSheet(theme)

    #Misc stuff
    window = Window()
    sys.exit(app.exec_())