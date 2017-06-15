import sys, os, create, createWorkarea
import qtawesome as qta
import animations as anim
from PyQt5 import QtGui, QtCore, QtWidgets, QtMultimedia

#This is the main file which is used for creating the window.

class createUI():    
    def create(self):
        print("create: Creating the main window layout")
        print("create: Creating widgets")

        #Create icons
        minIco = qta.icon("fa.minus", color="white")
        closeIco = qta.icon("fa.times", color="white")
        setIco = qta.icon("fa.sliders", color="white")
        maximIco = qta.icon("fa.arrows-alt", color="white")
        filesIco = qta.icon("fa.file-text-o", color="white")
        editIco = qta.icon("fa.pencil", color="white")
        windIco = qta.icon("fa.square-o", color="white")
        toolsIco = qta.icon("fa.cog", color="white")

        #Create window action buttons
        mini = QtWidgets.QPushButton(minIco, "", self)
        mini.setObjectName("minimize")
        mini.setMaximumSize(QtCore.QSize(30,30))
        mini.clicked.connect(self.minimize)

        quitBtn = QtWidgets.QPushButton(closeIco, "", self)
        quitBtn.setObjectName("quitBtn")
        quitBtn.setMaximumSize(QtCore.QSize(30,30))
        quitBtn.clicked.connect(QtCore.QCoreApplication.instance().quit)

        maxim = QtWidgets.QPushButton(maximIco, "", self)
        maxim.setObjectName("maxim")
        maxim.setMaximumSize(QtCore.QSize(30,30))
        maxim.clicked.connect(self.maximize)

        settings = QtWidgets.QPushButton(setIco, "", self)
        settings.setObjectName("settings")
        settings.setMaximumSize(QtCore.QSize(30,30))

        #Create Tool Buttons
        files = QtWidgets.QPushButton(filesIco, "", self)
        files.setObjectName("tools")
        files.setMaximumSize(QtCore.QSize(30,30))

        edit = QtWidgets.QPushButton(editIco, "", self)
        edit.setObjectName("tools")
        edit.setMaximumSize(QtCore.QSize(30,30))

        wind = QtWidgets.QPushButton(windIco, "", self)
        wind.setObjectName("tools")
        wind.setMaximumSize(QtCore.QSize(30,30))

        tool = QtWidgets.QPushButton(toolsIco, "", self)
        tool.setObjectName("tools")
        tool.setMaximumSize(QtCore.QSize(30,30))

        #Create app buttons
        cdnt = QtWidgets.QPushButton("", self)
        cdnt.setObjectName("cadent")
        cdnt.setMinimumSize(QtCore.QSize(50,50))
        cdnt.setMaximumSize(QtCore.QSize(90,90))
        cdnt.clicked.connect(self.animate)

        lakeside = QtWidgets.QPushButton("", self)
        lakeside.setObjectName("cadent")
        lakeside.setMinimumSize(QtCore.QSize(50,50))
        lakeside.setMaximumSize(QtCore.QSize(90,90))

        """
        Audio Test (doesnt work!)
        url= QtCore.QUrl.fromLocalFile("./Tobu - Amplified.mp3")
        content= QtMultimedia.QMediaContent(url)
        player = QtMultimedia.QMediaPlayer()
        player.setMedia(content)
        player.play()
        """

        #Dialogs
        dial = QtWidgets.QMessageBox()

        #Empty Widgets
        wMenu = QtWidgets.QWidget()
        wMenu.setObjectName("menu")
        wMenu.setMaximumWidth(200)

        self.wStack = QtWidgets.QWidget()
        self.wStack.setMaximumWidth(200)
        self.wStack.setVisible(False)

        wLPart = QtWidgets.QWidget()
        wLPart.setObjectName("leftEdit")

        wCPart = QtWidgets.QWidget()
        wCPart.setObjectName("centerEdit")

        wRPart = QtWidgets.QWidget()
        wRPart.setObjectName("rightEdit")

        #Size
        wCPart.setMinimumWidth(500)
        wRPart.setMinimumWidth(300)
        wLPart.setMinimumWidth(300)

        wLPart.setMaximumWidth(400)
        wRPart.setMaximumWidth(400)

        #Size Policy
        sp = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        wLPart.setSizePolicy(sp)
        #wMenu.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum))

        #Titlebar background
        cont = QtWidgets.QWidget(self)
        cont.setObjectName("titlebar")
        cont.setMinimumHeight(120)
        cont.setMaximumHeight(120)

        print("create: Creating layouts")

        #Layouts
        vMain = QtWidgets.QVBoxLayout() #Backbone lay, important because of the titlebar
        gCenter = QtWidgets.QGridLayout() #Central grid layout of the app beacuse every part is a widget not a layout
        vTB = QtWidgets.QHBoxLayout(cont) #Titlebat Layout
        vTabs = QtWidgets.QHBoxLayout() #Tabs Layout in the Titlebar
        winAc  = QtWidgets.QGridLayout() #Window actions layout (Top left buttons)
        tools = QtWidgets.QGridLayout() #Grid Layout for the tool actions in the titlebar
        vMenu = QtWidgets.QVBoxLayout() #Menu layout from the left side. Is placed on a blank widget then added to gCenter
        vLPart = QtWidgets.QVBoxLayout() #Left part of the editor
        self.vCPart = QtWidgets.QVBoxLayout() #Main layout of the editor
        vRPart = QtWidgets.QVBoxLayout() #Right part of the editor
        sMenu = QtWidgets.QStackedLayout() #Stack layout to show diffrent menu widgets
        #vCenter = QtWidgets.QVBoxLayout() Unused, former gCenter layout

        #Alignment
        vMain.setAlignment(QtCore.Qt.AlignTop)
        winAc.setAlignment(QtCore.Qt.AlignRight)
        gCenter.setAlignment(QtCore.Qt.AlignTop)
        vMenu.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)

        #Margin
        vMain.setContentsMargins(QtCore.QMargins(0,0,0,0))
        winAc.setContentsMargins(QtCore.QMargins(0,0,0,0))
        vMenu.setContentsMargins(QtCore.QMargins(0,0,0,0))
        gCenter.setContentsMargins(QtCore.QMargins(0,0,0,0))
        self.vCPart.setContentsMargins(QtCore.QMargins(0,0,0,0))
        winAc.setContentsMargins(QtCore.QMargins(10,23,20,23))
        vTB.setContentsMargins(QtCore.QMargins(20,0,0,0))
        tools.setContentsMargins(QtCore.QMargins(0,23,30,23))
        vTabs.setContentsMargins(QtCore.QMargins(0,0,0,0))

        #Stretch
        #vLPart.addStretch(1)
        #self.vCPart.addStretch(5)
        #vRPart.addStretch(1)

        #Adding the Widgets
        vMain.addWidget(cont)

        winAc.addWidget(mini, 0, 0)
        winAc.addWidget(quitBtn, 0, 1)
        winAc.addWidget(maxim, 1, 0)
        winAc.addWidget(settings, 1, 1)

        tools.addWidget(files, 0, 0)
        tools.addWidget(edit, 0, 1)
        tools.addWidget(wind, 1, 0)
        tools.addWidget(tool, 1, 1)

        vMenu.addWidget(lakeside)
        #vMenu.addWidget(cdnt)
        
        wWorkarea = createWorkarea.createArea()
        self.vCPart.addWidget(wWorkarea)

        gCenter.addWidget(self.wStack, 0, 0)
        gCenter.addWidget(wLPart, 0, 1)
        gCenter.addWidget(wCPart, 0, 2)
        gCenter.addWidget(wRPart, 0, 3)

        sMenu.addWidget(wMenu)

        vTabs.addWidget(cdnt)
        #vTabs.addWidget(lakeside)

        #adding the Layouts
        wMenu.setLayout(vMenu)
        self.wStack.setLayout(sMenu)
        wLPart.setLayout(vLPart)
        wCPart.setLayout(self.vCPart)
        wRPart.setLayout(vRPart)

        vTB.addLayout(tools)
        vTB.addLayout(vTabs)
        vTB.addLayout(winAc)
        vMain.addLayout(vTB)
        #hCenter.addLayout(vMenu)
        vMain.addLayout(gCenter)
        self.setLayout(vMain)