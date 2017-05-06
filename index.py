import sys, os, Create
import qtawesome as qta
from PyQt4 import QtGui, QtCore

#Variables
wmHidden = True

class Window(QtGui.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,1200,700)
        self.setWindowTitle("Hitch")
        #self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        Create.createUI.create(self)
        self.icon()
        self.showMaximized()
        self.show()

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
        dur = 500
        if wmHidden==False:
            anim1 = QtCore.QPropertyAnimation(self.wMenu, "pos")
            anim1.setDuration(dur)
            anim1.setStartValue(self.wMenu.pos())
            anim1.setEndValue(QtCore.QPoint(0,self.wMenu.y()))
            anim1.start()
            wmHidden = True
            self.anim1 = anim1

        else:
            anim2 = QtCore.QPropertyAnimation(self.wMenu, "pos")
            anim2.setDuration(dur)
            anim2.setStartValue(self.wMenu.pos())
            anim2.setEndValue(QtCore.QPoint(-1000,self.wMenu.y()))
            anim2.start()
            wmHidden = False
            self.anim2 = anim2


app = QtGui.QApplication(sys.argv)
with open("stylesheet.css") as f:
    theme = f.read()
app.setStyleSheet(theme)

wid = Window()

sys.exit(app.exec_())