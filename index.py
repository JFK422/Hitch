import sys, os
import qtawesome as qta
from PyQt4 import QtGui, QtCore

class Window(QtGui.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50,50,1200,700)
        self.setWindowTitle("Company")
        #self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        self.create()
        self.icon()
        self.show()

    def create(self):
        #Create icons
        minIco = qta.icon("fa.minus", color="white")
        closeIco = qta.icon("fa.times", color="white")
        setIco = qta.icon("fa.cog", color="white")
        usrIco = qta.icon("fa.user", color="white")

        #Create window action buttons
        mini = QtGui.QPushButton(minIco, "", self)
        mini.setObjectName("minimize")
        mini.setMaximumSize(QtCore.QSize(30,30))
        mini.clicked.connect(self.minimize)

        quitBtn = QtGui.QPushButton(closeIco, "", self)
        quitBtn.setObjectName("quitBtn")
        quitBtn.setMaximumSize(QtCore.QSize(30,30))
        quitBtn.clicked.connect(QtCore.QCoreApplication.instance().quit)

        settings = QtGui.QPushButton(setIco, "", self)
        settings.setObjectName("settings")
        settings.setMaximumSize(QtCore.QSize(30,30))
        settings.clicked.connect(self.maximize)

        friendz = QtGui.QPushButton(usrIco, "", self)
        friendz.setObjectName("friendz")
        friendz.setMaximumSize(QtCore.QSize(30,30))

        #Create app buttons
        cdnt = QtGui.QPushButton("", self)
        cdnt.setObjectName("cadent")
        cdnt.setMinimumSize(QtCore.QSize(50,50))
        cdnt.setMaximumSize(QtCore.QSize(90,90))

        lakeside = QtGui.QPushButton("", self)
        lakeside.setObjectName("cadent")
        lakeside.setMinimumSize(QtCore.QSize(50,50))
        lakeside.setMaximumSize(QtCore.QSize(90,90))

        #Titlebar background
        cont = QtGui.QWidget(self)
        cont.setObjectName("titlebar")
        cont.setMinimumHeight(120)
        cont.setMaximumHeight(120)


        #Layouts
        vMain = QtGui.QVBoxLayout()
        vTB = QtGui.QHBoxLayout(cont)
        vTabs = QtGui.QHBoxLayout()
        winAc  = QtGui.QGridLayout()

        #Alignment
        vMain.setAlignment(QtCore.Qt.AlignTop)
        winAc.setAlignment(QtCore.Qt.AlignRight)

        #Margin
        vMain.setMargin(0)
        winAc.setMargin(20)
        winAc.setContentsMargins(QtCore.QMargins(10,23,20,23))
        vTB.setContentsMargins(QtCore.QMargins(20,0,0,0))
        vTabs.setContentsMargins(QtCore.QMargins(0,0,0,0))

        #Adding the Widgets
        vMain.addWidget(cont)

        winAc.addWidget(mini, 0, 0)
        winAc.addWidget(quitBtn, 0, 1)
        winAc.addWidget(settings, 1, 0)
        winAc.addWidget(friendz, 1, 1)

        vTabs.addWidget(cdnt)
        vTabs.addWidget(lakeside)

        #adding the Layouts
        vTB.addLayout(vTabs)
        vTB.addLayout(winAc)
        vMain.addLayout(vTB)
        self.setLayout(vMain)

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

app = QtGui.QApplication(sys.argv)
with open("stylesheet.css") as f:
    theme = f.read()
app.setStyleSheet(theme)

wid = Window()

sys.exit(app.exec_())