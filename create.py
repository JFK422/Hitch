import qtawesome as qta
import animations as anim
from PyQt4 import QtGui, QtCore

#This is the main file which is used for creating the window.

class createUI():    
    def create(self):
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
        mini = QtGui.QPushButton(minIco, "", self)
        mini.setObjectName("minimize")
        mini.setMaximumSize(QtCore.QSize(30,30))
        mini.clicked.connect(self.minimize)

        quitBtn = QtGui.QPushButton(closeIco, "", self)
        quitBtn.setObjectName("quitBtn")
        quitBtn.setMaximumSize(QtCore.QSize(30,30))
        quitBtn.clicked.connect(QtCore.QCoreApplication.instance().quit)

        maxim = QtGui.QPushButton(maximIco, "", self)
        maxim.setObjectName("maxim")
        maxim.setMaximumSize(QtCore.QSize(30,30))
        maxim.clicked.connect(self.maximize)

        settings = QtGui.QPushButton(setIco, "", self)
        settings.setObjectName("settings")
        settings.setMaximumSize(QtCore.QSize(30,30))

        #Create Tool Buttons
        files = QtGui.QPushButton(filesIco, "", self)
        files.setObjectName("tools")
        files.setMaximumSize(QtCore.QSize(30,30))

        edit = QtGui.QPushButton(editIco, "", self)
        edit.setObjectName("tools")
        edit.setMaximumSize(QtCore.QSize(30,30))

        wind = QtGui.QPushButton(windIco, "", self)
        wind.setObjectName("tools")
        wind.setMaximumSize(QtCore.QSize(30,30))

        tool = QtGui.QPushButton(toolsIco, "", self)
        tool.setObjectName("tools")
        tool.setMaximumSize(QtCore.QSize(30,30))

        #Create app buttons
        cdnt = QtGui.QPushButton("", self)
        cdnt.setObjectName("cadent")
        cdnt.setMinimumSize(QtCore.QSize(50,50))
        cdnt.setMaximumSize(QtCore.QSize(90,90))
        cdnt.clicked.connect(self.animate)

        lakeside = QtGui.QPushButton("", self)
        lakeside.setObjectName("cadent")
        lakeside.setMinimumSize(QtCore.QSize(50,50))
        lakeside.setMaximumSize(QtCore.QSize(90,90))

        #Dialogs
        dial = QtGui.QMessageBox()

        #Empty Widgets
        wMenu = QtGui.QWidget()
        wMenu.setObjectName("menu")
        wMenu.setMaximumWidth(200)

        self.wStack = QtGui.QWidget()
        self.wStack.setMaximumWidth(200)
        self.wStack.setVisible(False)

        wLPart = QtGui.QWidget()
        wLPart.setObjectName("leftEdit")

        wCPart = QtGui.QWidget()
        wCPart.setObjectName("centerEdit")

        wRPart = QtGui.QWidget()
        wRPart.setObjectName("rightEdit")

        #Size
        wCPart.setMinimumWidth(500)
        wRPart.setMinimumWidth(300)
        wLPart.setMinimumWidth(300)

        wLPart.setMaximumWidth(400)
        wRPart.setMaximumWidth(400)

        #Size Policy
        #sp = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        #wLPart.setSizePolicy(sp)
        #wMenu.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum))

        #Titlebar background
        cont = QtGui.QWidget(self)
        cont.setObjectName("titlebar")
        cont.setMinimumHeight(120)
        cont.setMaximumHeight(120)


        #Layouts
        vMain = QtGui.QVBoxLayout() #Backbone lay, important because of the titlebar
        gCenter = QtGui.QGridLayout() #Central grid layout of the app beacuse every part is a widget not a layout
        vTB = QtGui.QHBoxLayout(cont) #Titlebat Layout
        vTabs = QtGui.QHBoxLayout() #Tabs Layout in the Titlebar
        winAc  = QtGui.QGridLayout() #Window actions layout (Top left buttons)
        tools = QtGui.QGridLayout() #Grid Layout for the tool actions in the titlebar
        vMenu = QtGui.QVBoxLayout() #Menu layout from the left side. Is placed on a blank widget then added to gCenter
        vLPart = QtGui.QVBoxLayout() #Left part of the editor
        vCPart = QtGui.QVBoxLayout() #Main layout of the editor
        vRPart = QtGui.QVBoxLayout() #Right part of the editor
        sMenu = QtGui.QStackedLayout() #Stack layout to show diffrent menu widgets
        #vCenter = QtGui.QVBoxLayout() Unused, former gCenter layout

        #Alignment
        vMain.setAlignment(QtCore.Qt.AlignTop)
        winAc.setAlignment(QtCore.Qt.AlignRight)
        gCenter.setAlignment(QtCore.Qt.AlignTop)
        vMenu.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)

        #Margin
        vMain.setMargin(0)
        winAc.setMargin(20)
        vMenu.setMargin(0)
        gCenter.setMargin(0)
        winAc.setContentsMargins(QtCore.QMargins(10,23,20,23))
        vTB.setContentsMargins(QtCore.QMargins(20,0,0,0))
        tools.setContentsMargins(QtCore.QMargins(0,23,30,23))
        vTabs.setContentsMargins(QtCore.QMargins(0,0,0,0))

        #Stretch
        vLPart.addStretch(1)
        vCPart.addStretch(5)
        vRPart.addStretch(1)

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
        wCPart.setLayout(vCPart)
        wRPart.setLayout(vRPart)

        vTB.addLayout(tools)
        vTB.addLayout(vTabs)
        vTB.addLayout(winAc)
        vMain.addLayout(vTB)
        #hCenter.addLayout(vMenu)
        vMain.addLayout(gCenter)
        self.setLayout(vMain)