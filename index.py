import sys, os, create
import qtawesome as qta
from ProjectHandling import workareaData as wd
from PyQt5 import QtGui, QtCore, QtWidgets

#This is the MAIN file of the app. Its used for handeling hte diffrent scripts within this programm.
#Debug prints are as formatted like this: FILE; CLASS; METHOD: MESSAGE

#Variables
wmHidden = False

class Window(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super(Window, self).__init__()
        self.setGeometry(50,50,1200,700)
        self.setWindowTitle("Hitch")
        #self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint) #Use this for a frameless window. Will be used later!
        wd.Data.readTemp(self)
        create.createUI.create(self)
        self.icon()
        self.showMaximized()
        self.show()

    #Minimize and maximize methods for the new window action buttons
    def minimize(self):
        self.showMinimized()

    def maximize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def icon(self):
        #set app icon    
        app_icon = QtGui.QIcon()
        app_icon.addFile('icons/16x16.png', QtCore.QSize(16,16))
        app_icon.addFile('icons/32x32.png', QtCore.QSize(32,32))
        app_icon.addFile('icons/64x64.png', QtCore.QSize(64,64))
        app_icon.addFile('icons/128x128.png', QtCore.QSize(128,128))
        app_icon.addFile('icons/256x256.png', QtCore.QSize(256,256))
        app.setWindowIcon(app_icon)
    

    def animate(self):
        global wmHidden
        
        if wmHidden == True:
            wmHidden = False

        else:
            wmHidden = True

#Creating the QApplication
app = QtWidgets.QApplication(sys.argv)

#Set the main styling of the app
with open("./Data/configFiles/style/stylesheet.css") as f:
    theme = f.read()
app.setStyleSheet(theme)

#Misc stuff
wid = Window()
sys.exit(app.exec_())